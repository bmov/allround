import jwt
import time
import uuid

from app.environment import env
from app.models import TokenRefreshers
from app.models import db

secret = env['APP_SECRET']
jwt_lifetime = env['JWT_LIFETIME']
jwt_algo = 'HS256'


class Token:
    def decodeToken(self, token):
        try:
            decoded = jwt.decode(token, secret, algorithms=jwt_algo)
        except (jwt.exceptions.DecodeError,
                jwt.exceptions.ExpiredSignatureError) as error:
            return f'{type(error).__name__}: {error}'

        expired = decoded['exp']

        if expired > time.time():
            return decoded

    def createAccessToken(self, username):
        expire = time.time() + int(jwt_lifetime)
        data = {
            'username': username,
            'exp': expire,
        }

        token = jwt.encode(data, secret, jwt_algo)

        return token

    def createRefreshToken(self, username):
        refresh_token = self.getRefreshToken(username)

        if refresh_token:
            return refresh_token

        new_token = str(uuid.uuid4())
        expire = time.time() + int(jwt_lifetime)

        refresh = TokenRefreshers(username=username,
                                  refresh_token=new_token,
                                  expire=expire)
        db.session.add(refresh)
        db.session.commit()

        return new_token

    def refreshAccessToken(self, refresh_token):
        find_exists = TokenRefreshers.query.filter_by(
            refresh_token=refresh_token).first()

        if find_exists:
            check_expire = find_exists.expire

            # if it valid
            if check_expire > time.time():
                token = self.createAccessToken(find_exists.username)

                return {
                    'success': True,
                    'accessToken': token,
                    'refreshToken': refresh_token
                }
            else:
                db.session.delete(find_exists)
                db.session.commit()

        return None

    def getRefreshToken(self, username):
        find_exists = TokenRefreshers.query.filter_by(
            username=username).first()

        if find_exists:
            check_expire = find_exists.expire

            # if it valid
            if check_expire > time.time():
                # return the current refreshToken
                return find_exists.refresh_token
            else:
                db.session.delete(find_exists)
                db.session.commit()

        return None
