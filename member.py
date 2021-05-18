from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo= True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Member(Base):
    __tablename__ = "member"
    member_id = Column(Integer, primary_key= True)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String)

    def __repr__(self):
        return "<Member('%s','%s', '%s', '%s')>" % (self.first_name, self.last_name, self.user_name, self.password)

member1 = Member(
    first_name = 'ali',
    last_name = 'kalan',
    user_name ='ali.ka',
    password = 1370,
)

session.add(member1)
session.commit()


