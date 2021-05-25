from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref


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
    messages = relationship("Message", back_populates='member')

    def __repr__(self):
        return "<Member('%s','%s', '%s', '%s')>" % \
               (self.first_name, self.last_name, self.user_name, self.password)


Base.metadata.create_all(engine)


member1 = Member(
    first_name='firstname 1',
    last_name='lastname 1',
    user_name='username 1',
    password='1370',
)

DBsession.add(member1)

member2 = Member(
    first_name='firstname 2',
    last_name='lastname 2',
    user_name='username 2',
    password='1375',
)

DBsession.add(member2)

member3 = Member(
    first_name='firstname 3',
    last_name='lastname 3',
    user_name='username 3',
    password='1369',
)

DBsession.add(member3)

member4 = Member(
    first_name='firstname 4',
    last_name='lastname 4',
    user_name='firstname 4lastname 4',
    password='1374',
)

DBsession.add(member4)
DBsession.commit()

added_member = DBsession.query(Member) \
    .filter(Member.user_name == member1.user_name) \
    .one_or_none()

print(added_member.last_name)

list_of_members = DBsession.query(Member)

for member in list_of_members:
    print(member.user_name, member.last_name)

added_of_members_ordered_by_names = DBsession.query(Member) \
    .order_by(Member.user_name) \
    .all()

for member in added_of_members_ordered_by_names:
    print(member.user_name)

record = DBsession.query(Member) \
    .filter(Member.user_name == member4.first_name + member4.last_name) \
    .first()

print(record)

count_of_member = DBsession.query(Member) \
   .count()

print(count_of_member)

count_of_member_filtered = DBsession.query(Member) \
    .filter(Member.first_name == member4.first_name) \
    .count()

print(count_of_member_filtered)


