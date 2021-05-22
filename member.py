from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    def __repr__(self):
        return "<Member('%s','%s', '%s', '%s')>" % \
               (self.first_name, self.last_name, self.user_name, self.password)


Base.metadata.create_all(engine)


member1 = Member(
    first_name='ali',
    last_name='kalan',
    user_name='ali.ka',
    password='1370',
)
DBsession.add(member1)
DBsession.commit()

added_member = DBsession.query(Member) \
    .filter(Member.user_name == 'ali.ka') \
    .one_or_none()

print(added_member.last_name)


