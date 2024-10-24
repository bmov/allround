from sqlalchemy.orm import declarative_base, relationship
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

    id = Column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    username = Column(String(64), index=True,
                      unique=True, nullable=False)
    passwd = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    email = Column(String(64), index=True, unique=True, nullable=False)
    intro_text = Column(Text(), nullable=True)
    signdate = Column(Integer, nullable=False)
    confirm = Column(Integer, default=0, nullable=False)
    confirm_key = Column(String(64), index=True, nullable=True)


class Docs(Base):
    """
    Create an Docs table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'docs'

    id = Column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    name = Column(String(128), nullable=False)
    content = Column(Text(), nullable=False)
    username = Column(String(64), index=True, nullable=True)
    date = Column(Integer, index=True, nullable=False)
    update_date = Column(Integer, index=True, nullable=True)


class TokenRefreshers(Base):
    """
    Create an TokenRefreshers table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'token_refreshers'

    id = Column(BigInteger().with_variant(
        Integer, 'sqlite'), primary_key=True)
    username = Column(String(64), index=True, nullable=False)
    refresh_token = Column(String(36), index=True, unique=True, nullable=False)
    expire = Column(Integer, index=True, default=0, nullable=False)


class Pages(Base):
    """
    Create an Pages table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True, nullable=False)
    folder_id = Column(Integer, default=0, index=True, nullable=False)
    page_type = Column(String(32), index=True, nullable=False)
    description = Column(Text(), nullable=True)


class PageFolders(Base):
    """
    Create an PageFolders table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'page_folders'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True, nullable=False)
    parent = Column(Integer, default=0, index=True, nullable=False)
    description = Column(Text(), nullable=True)
