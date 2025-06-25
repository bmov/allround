from app.database import async_session
from app.models import UserModel

from sqlalchemy.sql.expression import select


class SignupError(Exception):
    def __str__(self):
        return 'Failed to create user.'


class User(UserModel):
    @staticmethod
    async def findUserByUsername(username: str):
        async with async_session() as session:
            get = await session.scalars(
                select(User).
                filter_by(username=username).
                limit(1)
            )

        return get.first()

    @staticmethod
    async def signup(form):
        """
        Sign up
        """
        signup = User(username=form['username'],
                      passwd=form['passwd'],
                      name=form['name'],
                      email=form['email'],
                      intro_text=form['intro_text'],
                      signdate=form['signdate'],
                      confirm=form['confirm'],
                      confirm_key=form['confirm_key'])

        async with async_session() as session:
            session.add(signup)
            try:
                await session.commit()
            except Exception:
                raise SignupError()

        return {'status': True}
