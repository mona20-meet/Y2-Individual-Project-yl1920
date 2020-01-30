#from model import Article, Stuff
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///Data.db", connect_args={'check_same_thread': False}, echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
scoped_session(sessionmaker(bind=engine,autoflush=False))
def add_user(Email, Password):
	new_user=Stuff(Email=Email , Password=Password)
	session.add(new_user)
	session.commit()

# def add_article(Title, Description, Photo, link, Like, Dislike):
# 	new_article = Article(
# 		Title=Title, 
# 		Description=Description, 
# 		Photo=Photo, 
# 		link=link, 
# 		Like=Like, 
# 		Dislike=Dislike
# 		)
# 	session.add(new_article)
# 	session.commit()

#def getlikes():
	# likes = session.query(Article).all()
	# return likes

def like():
	pass

def dislike():
	pass

# add_article("math 101", "pass math and get top grades in your class ", ".../static/math3.jpg", "matharticle.html", 0, 0)
# add_article('biology 101', 'pass biology and get top grades in your class ', '/home/student/Desktop/Y2-Individual-Project-yl1920/static/bio2.jpg', 'bioarticle.html', 0, 0)
# add_article('math for dummies', 'ACE your class with the help of just these simple steps', '/home/student/Desktop/Y2-Individual-Project-yl1920/static/math3.jpg', 'matharticle.html', 0, 0)