import jwt
import time
import uuid

from app.environment import env
from app.models import TokenRefreshers
from app.database import async_session

from sqlalchemy.sql.expression import select
from sqlalchemy.exc import IntegrityError

secret = env['APP_SECRET']
jwt_lifetime = env['JWT_LIFETIME']
jwt_algo = 'HS256'
jwt_refresh_lifetime = env['JWT_REFRESH_LIFETIME']


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

    async def createRefreshToken(self, username):
        refresh_token = await self.getRefreshToken(username)

        if refresh_token:
            return refresh_token

        new_token = str(uuid.uuid4())
        expire = time.time() + int(jwt_refresh_lifetime)

        refresh = TokenRefreshers(username=username,
                                  refresh_token=new_token,
                                  expire=expire)

        try:
            async with async_session() as session:
                session.add(refresh)
                await session.commit()
        except IntegrityError:
            return await self.createRefreshToken(username)

        return new_token

    async def refreshAccessToken(self, refresh_token):
        async with async_session() as session:
            find_exists = await session.scalars(
                select(TokenRefreshers).
                filter_by(refresh_token=refresh_token).
                limit(1)
            )

            find_exists = find_exists.first()

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
                    session.delete(find_exists)
                    await session.commit()

        return None

    async def getRefreshToken(self, username):
        async with async_session() as session:
            find_exists = await session.scalars(
                select(TokenRefreshers).
                filter_by(username=username).
                limit(1)
            )

            find_exists = find_exists.first()

            if find_exists:
                check_expire = find_exists.expire

                # if it valid
                if check_expire > time.time():
                    # return the current refreshToken
                    return find_exists.refresh_token
                else:
                    session.delete(find_exists)
                    await session.commit()
        return None
