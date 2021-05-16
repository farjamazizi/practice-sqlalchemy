from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = "member"
    member_id = Column(Integer, primary_key= True)
    first_name = Column(String)
    Last_name = Column(String)
    room_id = Column(Integer, primary_key= True)
