import datetime

from database_setup import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Category).delete()
session.query(Items).delete()
session.query(User).delete()

user1 = User(name="Vincent Wang",
             email="vincentwang1130@gmail.com",
             picture="https://plus.google.com/u/0/photos/"
             "108682973839556116579/albums/profile/6387569522704376114")
session.add(user1)
session.commit()

category1 = Category(name='Soccer', user_id=1)
session.add(category1)
session.commit()

category2 = Category(name='Basketball', user_id=1)
session.add(category2)
session.commit()

category3 = Category(name='Baseball', user_id=1)
session.add(category3)
session.commit()

category4 = Category(name='Frisbee', userid=1)
session.add(category4)
session.commit()

category5 = Category(name='Snowboarding', userid=1)
session.add(category5)
session.commit()

category6 = Category(name='Rock Climbing', userid=1)
session.add(category6)
session.commit()

category7 = Category(name='Foosball', userid=1)
session.add(category7)
session.commit()

category8 = Category(name='Skating', userid=1)
session.add(category8)
session.commit()

category9 = Category(name='Hockey', userid=1)
session.add(category9)
session.commit()

item1 = Items(name='Stick',
              date=datetime.datetime.now(),
              description="Our selection of hockey sticks "
              "will have you shooting better and scoring more. "
              "High quality composite, wood and goalie sticks.",
              category_id=9,
              user_id=1)
session.add(item1)
session.commit()

item2 = Items(name='Goggles',
              date=datetime.datetime.now(),
              description="Superior color and contrast enhancement "
              "comes standard in our lineup of Happy Lens snow goggles.",
              category_id=5,
              user_id=1)
session.add(item2)
session.commit()


item3 = Items(name='Snowboard',
              date=datetime.datetime.now(),
              description="There is no mountain large enough to scare away "
              "the K2 Ultra Splitboard. "
              "This burly, stiff deck has a directional shape "
              "tuned for the best descents of your life.",
              category_id=5,
              user_id=1)
session.add(item3)
session.commit()

item4 = Items(name='Two shinguards',
              date=datetime.datetime.now(),
              description=" Shin guards and socks are required "
              "for legal play in nearly all soccer leagues.",
              category_id=1,
              user_id=1)
session.add(item4)
session.commit()

item5 = Items(name='Shinguards',
              date=datetime.datetime.now(),
              description="Shin guards and socks are required "
              "for legal play in nearly all soccer leagues.",
              category_id=1,
              user_id=1)
session.add(item5)
session.commit()

item6 = Items(name='Frisbee',
              date=datetime.datetime.now(),
              description="We spent 30 hours testing flying discs and "
              "decided that the Discraft UltraStar is the best "
              "recreational flying disc.",
              category_id=4,
              user_id=1)
session.add(item6)
session.commit()

item7 = Items(name='Bat',
              date=datetime.datetime.now(),
              description="A baseball bat is a smooth wooden or metal club "
              "used in the sport of baseball to hit the ball after "
              "it is thrown by the pitcher.",
              category_id=3,
              user_id=1)
session.add(item7)
session.commit()

item8 = Items(name='Jersey',
              date=datetime.datetime.now(),
              description="We have it here! Get a matching jersey "
              "to go along with your kids favorite team, "
              "check out our entire collection of Soccer Jerseys.",
              category_id=1,
              user_id=1)
session.add(item8)
session.commit()

item9 = Items(name='Soccer Cleats',
              date=datetime.datetime.now(),
              description="urf shoes have identical uppers to traditional "
              "soccer boots, but the outsoles differ in "
              "that they make up the cleat portion.",
              category_id=1,
              user_id=1)
session.add(item9)
session.commit()

print "Filling database, done"
