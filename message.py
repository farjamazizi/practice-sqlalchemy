from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker()
Session.configure(bind=engine)
DBsession = Session()

Base = declarative_base()


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, default='')

    def __repr__(self):
        return "<Message('%s')" % \
               (self.text)


Base.metadata.create_all(engine)


message1 = Message(
    text='Hello world',
)

DBsession.add(message1)
DBsession.commit()


