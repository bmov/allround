from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Column, String, Integer, Text, BigInteger, \
    Boolean, Numeric, Float, Double, ForeignKey

Base = declarative_base()


class Users(Base):
    """
    Create an Users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True,
                                          unique=True, nullable=False)
    passwd: Mapped[str] = mapped_column(String(128), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(
        String(64), index=True, unique=True, nullable=False)
    intro_text: Mapped[str] = mapped_column(Text(), nullable=True)
    signdate: Mapped[int] = mapped_column(Integer, nullable=False)
    confirm: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    confirm_key: Mapped[str] = mapped_column(
        String(64), index=True, nullable=True)


class Docs(Base):
    """
    Create an Docs table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'docs'

    id: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    content: Mapped[str] = mapped_column(Text(), nullable=False)
    username: Mapped[str] = mapped_column(
        String(64), index=True, nullable=True)
    date: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    update_date: Mapped[int] = mapped_column(
        Integer, index=True, nullable=True)


class TokenRefreshers(Base):
    """
    Create an TokenRefreshers table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'token_refreshers'

    id: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    username: Mapped[str] = mapped_column(
        String(64), index=True, nullable=False)
    refresh_token: Mapped[str] = mapped_column(
        String(36), index=True, unique=True, nullable=False)
    expire: Mapped[int] = mapped_column(
        Integer, index=True, default=0, nullable=False)


class Pages(Base):
    """
    Create an Pages table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'pages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    folder_id: Mapped[int] = mapped_column(
        Integer, default=0, index=True, nullable=False)
    page_type: Mapped[str] = mapped_column(
        String(32), index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=True)


class PageFolders(Base):
    """
    Create an PageFolders table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'page_folders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    parent: Mapped[int] = mapped_column(
        Integer, default=0, index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
