from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
Session = sessionmaker()

engine = create_engine('sqlite:///:memory:', echo=True)

Session.configure(bind=engine)
sess = Session()

Base = declarative_base()


class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String)

    def __repr__(self):
        return "<Member('%s','%s', '%s', '%s')>" % \
               (self.first_name, self.last_name, self.user_name, self.password)


Base.metadata.create_all(engine)


member1 = Member(
    id=1,
    first_name='ali',
    last_name='kalan',
    user_name='ali.ka',
    password='1370',
)
sess.add(member1)
sess.commit()

member = sess.query(Member).filter(Member.id == 1).one_or_none()
print(member.last_name)
