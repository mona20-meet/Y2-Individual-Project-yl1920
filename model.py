from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Stuff(Base):


	__tablename__= "Users"
	Email= Column(String, primary_key=True)
	Password=Column(String)
	
	def __repr__(self):
		return ("Email: {}\n"
				"Password: {} ").format(
					self.Email, self.Password)
class Articles(Base):


	__tablename__= "articles"
	Title= Column(String, primary_key=True)
	Discription=Column(String)
	Photo=Column(String)
	Content=Column(String)
	Like=Column(Integer)
	Dislike=Column(Integer)
	def __repr__(self):
		return ("Title: {}\n"
				"Discription: {}\n"
				"Photo: {}\n"
				"Content: {}\n "
				'Like:{}\n'
				"Dislike:{}").format(
					self.Title, self.Discription, self.Photo, self.Content, self.Like , self.Dislike)

