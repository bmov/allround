import time
from components.render_json import message
from connexion import request

from components.token import Token, TokenRefresher
from components.password import Password
from components.user import SignupError, User


class UserApi:
    @staticmethod
    async def get(username, token_info):
        """
        Get user information
        """

        user = User()
        find_username = await user.findUserByUsername(username)

        if not find_username:
            return message(None,
                           message='Username not found.',
                           code=400)  # Username not found

        if token_info:
            if type(token_info) is not dict:
                return message(None,
                               message='Invalid token.',
                               code=401)  # Invalid token

            if token_info['username'] == username:
                # Signed user and get user are same
                return {
                    'username': username,
                    'name': find_username.name,
                    'email': find_username.email,
                    'intro_text': find_username.intro_text,
                    'signdate': find_username.signdate
                }
            else:
                return {
                    'username': username,
                    'name': find_username.name,
                    'intro_text': find_username.intro_text,
                    'signdate': find_username.signdate,
                }

        # Not signed
        return {
            'username': username,
            'signdate': find_username.signdate,
        }

    @staticmethod
    async def put(username, payload):
        """
        Sign up
        """

        passwd = payload['passwd']

        pw = Password()
        pw.passwd = passwd
        passwd_hash = pw.password_hash()

        name = payload['name']
        email = payload['email']
        intro_text = payload['intro_text']
        signdate = time.time()
        confirm = 1
        confirm_key = ''

        try:
            signup = await User.signup({
                'username': username,
                'passwd': passwd_hash,
                'name': name,
                'email': email,
                'intro_text': intro_text,
                'signdate': signdate,
                'confirm': confirm,
                'confirm_key': confirm_key
            })
        except SignupError as error:
            return message(None,
                           message=str(error), code=400)

        return signup

    @staticmethod
    def delete(username):
        """
        Remove account
        """

        return {}


class SignInApi:
    @staticmethod
    async def post(payload):
        """
        Sign in
        """

        username = payload['username']
        passwd = payload['passwd']

        # Sign in
        user = User()
        find_username = await user.findUserByUsername(username)

        if not find_username:
            return message(None,
                           message='Username not found.',
                           code=400)  # Username not found

        pw = Password()
        pw.passwd = passwd

        if pw.verify_passwd(find_username.passwd):
            if find_username.confirm:
                # success
                access_token = Token.createAccessToken(
                    find_username.username)
                refresh_token = await TokenRefresher.createRefreshToken(
                    find_username.username)

                return {
                    'status': True,
                    'accessToken': access_token,
                    'refreshToken': refresh_token
                }
            else:
                return message(None,
                               message='Not a verified user.',
                               code=401)  # Not a verified user

        return message(None,
                       message='Username or password doesn\'t match.',
                       code=400)  # Username or password doesn't match


class ResetAccountApi:
    @staticmethod
    async def post():
        """
        Reset account
        """

        return {}


class SessionApi:
    @staticmethod
    async def get(token_info):
        if not token_info:
            return message(None,
                           message='Please sign in first.',
                           code=401)

        result = await TokenRefresher.getRefreshTokens(token_info['username'])

        if result:
            return {
                'result': result
            }

        return {}


class RefreshApi:
    @staticmethod
    async def post(payload):
        result = await TokenRefresher.refreshAccessToken(payload['refreshToken'])

        if result:
            return result

        return message(None,
                       message='Unable to refresh.',
                       code=400)
