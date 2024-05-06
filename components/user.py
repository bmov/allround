from app.database import async_session
from app.models import Users

from sqlalchemy.sql.expression import select


class User:
    async def findUserByUsername(self, username: str):
        async with async_session() as session:
            get = await session.scalars(
                select(Users).
                filter_by(username=username).
                limit(1)
            )

        return get.first()
