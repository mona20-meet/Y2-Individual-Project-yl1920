from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///Data.db", connect_args={'check_same_thread': False})
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(Email, Password ):
	new_user=Stuff(Email=Email , Password=Password)
	session.add(new_user)
	session.commit()
def add_article(Title, Discription, Photo, Content, Like, Dislike):
	new_article=Article(Title=Title, Discription=Discription, Photo=Photo, Content=Content, Like=Like, Dislike=Dislike)
	session.add(new_article)
	session.commit()

def like():
	pass

def dislike():
	pass

