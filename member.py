from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Text

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

class Member(Base):
    __tablename__ = "member"
    member_id = Column(Integer, primary_key= True)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)

    def __init__(self):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.first_name, self.last_name, self.password)

class Email(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key= True)
    email_address = Column(String(100), nullable= False)

    member_id = Column(Integer, ForeignKey('members.id'))
    member = relationship("Member", 'email', order_by= id)

Base.metadata.creat_all(engine)




