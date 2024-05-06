import time
from components.render_json import message
from connexion import request

from app.models import Users
from app.database import async_session
from components.token import Token
from components.password import Password
from components.user import User


class UserApi:
    async def get(username):
        """
        Get user information
        """

        user = User()
        find_username = await user.findUserByUsername(username)

        if not find_username:
            return message(None,
                           message='Username not found.',
                           code=400)  # Username not found

        access_token = request.headers.get('X-Access-Token')

        if access_token:
            token = Token()
            decoded_token = token.decodeToken(access_token)

            if type(decoded_token) is not dict:

                return message(None,
                               message='Invalid token.',
                               code=401)  # Invalid token

            if decoded_token['username'] == username:
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
        signup = Users(username=username,
                       passwd=passwd_hash,
                       name=name,
                       email=email,
                       intro_text=intro_text,
                       signdate=signdate,
                       confirm=confirm,
                       confirm_key=confirm_key)

        async with async_session() as session:
            session.add(signup)
            try:
                await session.commit()
            except Exception:
                return message(None,
                               message='Failed to create user.',
                               code=500)  # error

        return {'status': True}

    def delete(username):
        """
        Remove account
        """

        return {}


class SignInApi:
    async def post(payload):
        """
        Sign in
        """

        username = payload['username']
        passwd = payload['passwd']

        token = Token()

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
                access_token = token.createAccessToken(
                    find_username.username)
                refresh_token = await token.createRefreshToken(
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
    def post():
        """
        Reset account
        """

        return {}
