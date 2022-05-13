from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

engine = create_engine("sqlite:///tiktok.sqlite3", echo=True)
Base = declarative_base()


class TikTokUserDB(Base):
    __tablename__ = "tiktok_users"
    id = Column(Integer, primary_key=True)
    avatar_link = Column(String)
    name = Column(String)
    username = Column(String)
    description = Column(String)
    following_count = Column(Integer)
    followers_count = Column(Integer)
    verified = Column(Integer)

    videos = Column(Integer)

    children = relationship("TikTokVideoDB", lazy="noload")


class TikTokVideoDB(Base):
    __tablename__ = "tiktok_videos"

    id = Column(Integer, primary_key=True)

    user_id = Column(String)
    created_time = Column(DateTime)
    description = Column(String)

    play_count = Column(Integer)
    share_count = Column(Integer)
    likes_count = Column(Integer)

    comments = Column(Integer)

    parent_id = Column(Integer, ForeignKey('tiktok_users.id'))
    #parent_id = relationship("TikTokUserDB", back_populates="children")



Base.metadata.create_all(engine)
