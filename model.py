from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Stuff(Base):
	__tablename__= "Users"
	Id= Column(Integer, primary_key=True)
	Email= Column(String )
	Password=Column(String)
	'''
	def __repr__(self):
		return ("Email: {}\n"
				"Password: {} ").format(
					self.Email, self.Password)
					'''

# class Article(Base):
# 	__tablename__= "Articles"
# 	Id= Column(Integer, primary_key=True)
# 	Title= Column(String)
# 	Description=Column(String)
# 	Photo=Column(String)
# 	link=Column(String)
# 	Like=Column(Integer)
	# Dislike=Column(Integer)
