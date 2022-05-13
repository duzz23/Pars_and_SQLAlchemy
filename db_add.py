import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, TikTokUserDB, TikTokVideoDB
from parser import addcategories

data = json.loads(addcategories()).get('search')[0]

engine = create_engine("sqlite:///tiktok.sqlite3", echo=True)
session = sessionmaker(bind=engine)
s = session()


s.add_all([
    TikTokUserDB(avatar_link=data.get('avatar_link')),
    TikTokUserDB(name=data.get('name')),
    TikTokUserDB(username=data.get('username')),
    TikTokUserDB(description=data.get('description')),
    TikTokUserDB(following_count=data.get('following_count')),
    TikTokUserDB(followers_count=data.get('followers_count')),
    TikTokUserDB(verified=data.get('verified')),
    TikTokUserDB(videos=data.get('videos_date')),


])

s.commit()

s.add_all([
    TikTokVideoDB(created_time=data.get('created_time')),
    TikTokVideoDB(description=data.get('description')),
    TikTokVideoDB(play_count=data.get('play_count')),
    TikTokVideoDB(share_count=data.get('share_count')),
    TikTokVideoDB(likes_count=data.get('likes_count')),
    TikTokVideoDB(comments=data.get('comments')),

])

s.commit()