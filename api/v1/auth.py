import time
from flask import request
from flask_restx import fields, Resource, Namespace, abort

from app.models import db, Users
from components.token import Token
from components.password import Password

Auth = Namespace('Auth')

model_access_token = Auth.model('AccessToken', {
    'accessToken': fields.String(description='Access token',
                                 required=False)
})
model_signin_data = Auth.model('SignInForm', {
    'username': fields.String(description='The username of the user to '
                              'sign in.',
                              required=True),
    'passwd': fields.String(description='Password',
                            required=True),
})
model_signup_data = Auth.model('SignUpForm', {
    'passwd': fields.String(description='Password',
                            required=True),
    'name': fields.String(description='Display name',
                          required=True),
    'email': fields.String(description='Email address',
                           required=True),
    'intro_text': fields.String(description='Status messages',
                                required=False)

})

header_access_token = Auth.parser()
header_access_token.add_argument('X-Access-Token', location='headers')


@Auth.route('/user/<string:username>')
@Auth.doc(params={
    'username': 'Username'
})
class User(Resource):
    @Auth.expect(header_access_token)
    def get(self, username):
        """
        Get user information
        """

        find_username = Users.query.filter_by(username=username).first()
        if not find_username:
            return abort(404, status=False)  # Username not found

        access_token = request.headers.get('X-Access-Token')

        if access_token:
            token = Token()
            decoded_token = token.decodeToken(access_token)

            if type(decoded_token) is not dict:
                # Invalid token
                return abort(500, decoded_token, status=False)

            if decoded_token['username'] == username:
                # Signed user and get user are same
                return {
                    'username': username,
                    'name': find_username.name,
                    'email': find_username.email,
                    'intro_text': find_username.intro_text,
                    'signdate': find_username.signdate,
                    'token': decoded_token
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

    @Auth.expect(model_signup_data)
    def put(self, username):
        """
        Sign up
        """

        passwd = request.json.get('passwd')

        pw = Password()
        pw.passwd = passwd
        passwd_hash = pw.password_hash()

        name = request.json.get('name')
        email = request.json.get('email')
        intro_text = request.json.get('intro_text')
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
        db.session.add(signup)
        db.session.commit()
        return {'status': True}

    @Auth.expect(model_access_token)
    def delete(self, username):
        """
        Remove account
        """

        return {}


@Auth.route('/signin')
class SignIn(Resource):
    @Auth.expect(model_signin_data)
    def post(self):
        """
        Sign in
        """

        username = request.json.get('username')
        passwd = request.json.get('passwd')

        token = Token()

        # Sign in
        find_username = Users.query.filter_by(username=username).first()
        if not find_username:
            return abort(401, status=False)  # Username not found

        pw = Password()
        pw.passwd = passwd

        if pw.verify_passwd(find_username.passwd):
            if find_username.confirm:
                # success
                return {
                    'status': True,
                    'accessToken': token.createAccessToken(
                        find_username.username),
                    'refreshToken': token.createRefreshToken(
                        find_username.username),
                }
            else:
                # Not a verified user
                return abort(401, 'Not a verified user', status=False)

        return abort(401, status=False)


@Auth.route('/reset')
class ResetAccount(Resource):
    def post(self):
        """
        Reset account
        """

        return {}
