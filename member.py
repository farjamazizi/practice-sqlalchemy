from sqlalchemy import Column, Integer, String, Date, extract
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import column_property
from datetime import date


engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker()
Session.configure(bind=engine)
DBsession = Session()

Base = declarative_base()


class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String, unique=True)
    password = Column(String)
    birth_date =Column(Date, default=date.today())
    age = column_property(date.today().year - extract('year', birth_date))
    fullname = column_property(first_name + ' ' + last_name)


    def __repr__(self):
        return "<Member('%s','%s', '%s', '%s')>" % \
               (self.first_name, self.last_name, self.user_name, self.password)


Base.metadata.create_all(engine)

