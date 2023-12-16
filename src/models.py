import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#class Person(Base):
#    __tablename__ = 'person'
#    # Here we define columns for the table person
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)
#
#class Address(Base):
#    __tablename__ = 'address'
#    # Here we define columns for the table address.
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)
#
#    def to_dict(self):
#        return {}

class Follower(Base):
    __tablename__="follower"

    id = Column(Integer, primary_key=True)
    Name = Column(String(120), unique=True, nullable = False)
    
    

class User(Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True)
    userName = Column(String(120), unique=True, nullable = False)
    firstName = Column(String(50), unique=False, nullable=False) 
    lastName = Column(String(50), unique=False, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    follwerId = Column(Integer, ForeignKey("follower.id"))
    follower = relationship("Follower")

class Media(Base):
    __tablename__="media"

    id = Column(Integer, primary_key=True)
    Name = Column(String(120), unique=True, nullable = False)
    postId = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post",back_populates="comment")
    

class Post(Base):
    __tablename__="post"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=False, nullable = False)
    content = Column(String(300), unique=False, nullable = False)
    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="post")

class Comment(Base):
    __tablename__="comment"

    id = Column(Integer, primary_key=True)
    Name = Column(String(120), unique=True, nullable = False)
    rotation_period = Column(Integer, unique=False, nullable=False)
    authorId = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="post") 
    postId = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post",back_populates="comment")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
