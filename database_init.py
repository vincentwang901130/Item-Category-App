import datetime

from database_setup import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Catagory).delete()
session.query(Items).delete()
session.query(User).delete()

user1 = User(name="Vincent Wang",
             email="vincentwang1130@gmail.com",
             picture="https://plus.google.com/u/0/photos/"
             "108682973839556116579/albums/profile/6387569522704376114")
session.add(user1)
session.commit()

catagory1 = Catagory(name='Soccer', user_id=1)
session.add(catagory1)
session.commit()

catagory2 = Catagory(name='Basketball', user_id=1)
session.add(catagory2)
session.commit()

catagory3 = Catagory(name='Baseball', user_id=1)
session.add(catagory3)
session.commit()

catagory4 = Catagory(name='Frisbee', userid=1)
session.add(catagory4)
session.commit()

catagory5 = Catagory(name='Snowboarding', userid=1)
session.add(catagory5)
session.commit()

catagory6 = Catagory(name='Rock Climbing', userid=1)
session.add(catagory6)
session.commit()

catagory7 = Catagory(name='Foosball', userid=1)
session.add(catagory7)
session.commit()

catagory8 = Catagory(name='Skating', userid=1)
session.add(catagory8)
session.commit()

catagory9 = Catagory(name='Hockey', userid=1)
session.add(catagory9)
session.commit()

item1 = Items(name='Stick',
              date=datetime.datetime.now(),
              description="Our selection of hockey sticks "
              "will have you shooting better and scoring more. "
              "High quality composite, wood and goalie sticks.",
              catagory_id=9,
              user_id=1)
session.add(item1)
session.commit()

item2 = Items(name='Goggles',
              date=datetime.datetime.now(),
              description="Superior color and contrast enhancement "
              "comes standard in our lineup of Happy Lens snow goggles.",
              catagory_id=5,
              user_id=1)
session.add(item2)
session.commit()


item3 = Items(name='Snowboard',
              date=datetime.datetime.now(),
              description="There is no mountain large enough to scare away "
              "the K2 Ultra Splitboard. "
              "This burly, stiff deck has a directional shape "
              "tuned for the best descents of your life.",
              catagory_id=5,
              user_id=1)
session.add(item3)
session.commit()

item4 = Items(name='Two shinguards',
              date=datetime.datetime.now(),
              description=" Shin guards and socks are required "
              "for legal play in nearly all soccer leagues.",
              catagory_id=1,
              user_id=1)
session.add(item4)
session.commit()

item5 = Items(name='Shinguards',
              date=datetime.datetime.now(),
              description="Shin guards and socks are required "
              "for legal play in nearly all soccer leagues.",
              catagory_id=1,
              user_id=1)
session.add(item5)
session.commit()

item6 = Items(name='Frisbee',
              date=datetime.datetime.now(),
              description="We spent 30 hours testing flying discs and "
              "decided that the Discraft UltraStar is the best "
              "recreational flying disc.",
              catagory_id=4,
              user_id=1)
session.add(item6)
session.commit()

item7 = Items(name='Bat',
              date=datetime.datetime.now(),
              description="A baseball bat is a smooth wooden or metal club "
              "used in the sport of baseball to hit the ball after "
              "it is thrown by the pitcher.",
              catagory_id=3,
              user_id=1)
session.add(item7)
session.commit()

item8 = Items(name='Jersey',
              date=datetime.datetime.now(),
              description="We have it here! Get a matching jersey "
              "to go along with your kids favorite team, "
              "check out our entire collection of Soccer Jerseys.",
              catagory_id=1,
              user_id=1)
session.add(item8)
session.commit()

item9 = Items(name='Soccer Cleats',
              date=datetime.datetime.now(),
              description="urf shoes have identical uppers to traditional "
              "soccer boots, but the outsoles differ in "
              "that they make up the cleat portion.",
              catagory_id=1,
              user_id=1)
session.add(item9)

print "Data base dummy data injected"
