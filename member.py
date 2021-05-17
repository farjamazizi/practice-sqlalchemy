from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = "member"
    member_id = Column(Integer, primary_key= True)
    first_name = Column(String)
    Last_name = Column(String)
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)



    def __repr__(self):
        return "<Member(first_name = '%s', last_name = 's%')>" % (
                                 self.first_name, self.last_name)
