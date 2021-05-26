from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker()
Session.configure(bind=engine)
DBsession = Session()

Base.metadata.create_all(bind=engine)

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, default='')
    owner_id =Column(Integer, ForeignKey('member.id'))

    owner = relationship(
        'Member',
        back_populates= 'messages'
    )

    def __repr__(self):
        return "<Message('%s')" % \
               (self.text)


Base.metadata.create_all(engine)


message1 = Message(
     text='Hello world',
 )

DBsession.add(message1)
DBsession.commit()


