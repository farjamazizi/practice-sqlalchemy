import sqlalchemy

#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///:memory:', echo=True)

#from sqlalchemy.orm import declarative_base
#Base = declarative_base()

#from sqlalchemy import Column, Integer, String
#class User(Base):
    #__tablename__ = 'users'
    #id = Column(Integer, primary_key=True)
    #name = Column(String)
    #fullname = Column(String)
    #nickname = Column(String)

    #def __repr__(self):
        #return "<User(name = '%s', fullname = '%s', nickname = '%s' )>" % (self.name, self.fullname, self.nickname)
#from sqlalchemy import Column, Integer, String
#class User(Base):
    #__tablename__ = 'User'
    #id = Column(Integer, primary_key= True)
    #name = Column(String)
    #fullname = Column(String)
    #nickname = Column(String)

    #def __repr__(self):
        #return "<User(name = '%s', fullname = '%s', nickname = '%s' ) > " % (self.name, self.fullname, self.nickname)

#User.__table__
#Table('users', MetaData(),
            #Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
            #Column('name', String(), table=<users>),
            #Column('fullname', String(), table=<users>),
            #Column('nickname', String(), table=<users>), schema=None)
#Base.metadata.create_all(engine)
#BEGIN...
#CREATE TABLE users (
    #id INTEGER NOT NULL,
    #name VARCHAR,
    #fullname VARCHAR,
    #nickname VARCHAR,
    #PRIMARY KEY (id)
#)
#[...] ()
#COMMIT

#from sqlalchemy import Sequence
#Column(Integer, Sequence('user_id_seq'), primary_key=True)
#class User(Base):
    #__tablename__ = 'users'
    #id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    #name = Column(String(50))
    #fullname = Column(String(50))
    #nickname = Column(String(50))

    #def __repr__(self):
        #return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                #self.name, self.fullname, self.nickname)

#ed_user = User(name = 'ed', fullname= 'ed jones', nickname = 'edsnickname')

#from sqlalchemy.orm import sessionmaker
#Session = sessionmaker(bind= engine)
#Session = sessionmaker()
#Session.configure(bind= engine) #once engine is available
#session = Session()

#from sqlalchemy import Column, Integer, String, ForeignKey, Table
#from sqlalchemy.orm import relationship, backref
#from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()

#author_publisher = Table(
    #"author_publisher",
    #Base.metadata,
    #Column("author_id", Integer, ForeignKey("author.author_id")),
    #Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
#)

#book_publisher = Table(
    #"book_publisher",
    #Base.metadata,
    #Column("book_id", Integer, ForeignKey("book.book_id")),
    #Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
#)

#class Author(Base):
    #__tablename__ = "author"
    #author_id = Column(Integer, primary_key=True)
    #first_name = Column(String)
    #last_name = Column(String)
    #books = relationship("Book", backref=backref("author"))
    #publishers = relationship(
        #"Publisher", secondary=author_publisher, back_populates="authors"
    #)

#class Book(Base):
    #__tablename__ = "book"
    #book_id = Column(Integer, primary_key=True)
    #author_id = Column(Integer, ForeignKey("author.author_id"))
    #title = Column(String)
    #publishers = relationship(
        #"Publisher", secondary=book_publisher, back_populates="books"
    #)

#class Publisher(Base):
    #__tablename__ = "publisher"
    #publisher_id = Column(Integer, primary_key=True)
    #name = Column(String)
    #authors = relationship(
        #"Author", secondary=author_publisher, back_populates="publishers"
    #)
    # books = relationship(
    #     "Book", secondary=book_publisher, back_populates="publishers"
    # )
# ----------------------------------------------------------------------------------------
#tamrin table member


# from sqlalchemy import Column, Integer, String, ForeignKey, Table
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
# class Member(Base):
#     __tablename__ = "member"
#     member_id = Column(Integer, primary_key= True)
#     first_name = Column(String)
#     Last_name = Column(String)
#     room_id = Column(Integer, primary_key= True)












































