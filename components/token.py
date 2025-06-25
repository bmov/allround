import jwt
import time
import uuid

from app.environment import env
from app.models import TokenRefresherModel
from app.database import async_session

from sqlalchemy.sql.expression import select
from sqlalchemy.exc import IntegrityError

from starlette.exceptions import HTTPException

secret = env['APP_SECRET']
jwt_lifetime = env['JWT_LIFETIME']
jwt_algo = 'HS256'
jwt_refresh_lifetime = env['JWT_REFRESH_LIFETIME']


class Token():
    @staticmethod
    def decodeToken(token):
        try:
            return jwt.decode(token, secret, algorithms=[jwt_algo])
        except (jwt.exceptions.DecodeError,
                jwt.exceptions.ExpiredSignatureError) as error:
            raise HTTPException(
                status_code=400, detail=f'{type(error).__name__}: {error}')

    @staticmethod
    def createAccessToken(username):
        expire = time.time() + int(jwt_lifetime)
        data = {
            'username': username,
            'exp': expire,
        }

        token = jwt.encode(data, secret, jwt_algo)

        return token

    @staticmethod
    def getAccessToken(request) -> str | None:
        auth_header = request.headers.get('Authorization')

        if auth_header:
            token = auth_header.replace('Bearer ', '')
            return token

        return None

    def getAuthPayload(self, request):
        access_token = self.getAccessToken(request)

        if access_token:
            decoded_token = self.decodeToken(access_token)
            return decoded_token

        return None


class TokenRefresher(TokenRefresherModel):
    @staticmethod
    async def createRefreshToken(username):
        new_token = str(uuid.uuid4())
        expire = time.time() + int(jwt_refresh_lifetime)

        refresh = TokenRefresher(username=username,
                                 refresh_token=new_token,
                                 expire=expire)

        try:
            async with async_session() as session:
                session.add(refresh)
                await session.commit()
        except IntegrityError:
            return TokenRefresher.createRefreshToken(username)

        return new_token

    @staticmethod
    async def refreshAccessToken(refresh_token):
        async with async_session() as session:
            find_exists = await session.scalars(
                select(TokenRefresher).
                filter_by(refresh_token=refresh_token).
                limit(1)
            )

            find_exists = find_exists.first()

            if find_exists:
                check_expire = find_exists.expire

                # if it valid
                if check_expire > time.time():
                    token = Token.createAccessToken(find_exists.username)
                    return {
                        'success': True,
                        'accessToken': token,
                        'refreshToken': refresh_token
                    }
                else:
                    await session.delete(find_exists)
                    await session.commit()

        return None

    @classmethod
    async def getRefreshTokens(cls, username):
        async with async_session() as session:
            tokens = await session.execute(
                select(cls).
                where(cls.username == username,
                      cls.expire >= 2).
                order_by(cls.id.desc())
            )

            result = tokens.scalars().all()
            tokens_list = []

            if tokens:
                for t in result:
                    tokens_list.append({
                        'id': t.id,
                        'username': t.username,
                        'refresh_token': t.refresh_token,
                        'expire': t.expire
                    })

                return tokens_list

        return []

    @staticmethod
    async def getRefreshToken(username):
        async with async_session() as session:
            find_exists = await session.scalars(
                select(TokenRefresher).
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
                    await session.delete(find_exists)
                    await session.commit()
        return None
