from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Column, String, Integer, Text, BigInteger, \
    Boolean, Numeric, Float, Double, ForeignKey

Base = declarative_base()


class UserModel(Base):
    """
    Create an Users table
    """

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
    signdate: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), nullable=False)
    confirm: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    confirm_key: Mapped[str] = mapped_column(
        String(64), index=True, nullable=True)


class DocModel(Base):
    """
    Create an Docs table
    """

    __tablename__ = 'docs'

    id: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    uuid: Mapped[str] = mapped_column(
        String(36), index=True, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    content: Mapped[str] = mapped_column(Text(), nullable=False)
    username: Mapped[str] = mapped_column(
        String(64), index=True, nullable=True)
    date: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), index=True, nullable=False)
    update_date: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), index=True, nullable=True)


class TokenRefresherModel(Base):
    """
    Create an TokenRefreshers table
    """

    __tablename__ = 'token_refreshers'

    id: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    username: Mapped[str] = mapped_column(
        String(64), index=True, nullable=False)
    refresh_token: Mapped[str] = mapped_column(
        String(36), index=True, unique=True, nullable=False)
    expire: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), index=True, default=0, nullable=False)


class PageModel(Base):
    """
    Create an Pages table
    """

    __tablename__ = 'pages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uuid: Mapped[str] = mapped_column(
        String(36), index=True, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    folder_id: Mapped[int] = mapped_column(
        Integer, default=0, index=True, nullable=False)
    page_type: Mapped[str] = mapped_column(
        String(32), index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    date: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), index=True, nullable=False)
    update_date: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), index=True, nullable=True)


class PageFolderModel(Base):
    """
    Create an PageFolders table
    """

    __tablename__ = 'page_folders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uuid: Mapped[str] = mapped_column(
        String(36), index=True, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    parent: Mapped[int] = mapped_column(
        Integer, default=0, index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    date: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), index=True, nullable=False)
    update_date: Mapped[int] = mapped_column(BigInteger().with_variant(
        Integer, 'sqlite'), index=True, nullable=True)
