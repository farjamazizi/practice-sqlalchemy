from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func


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

member2 = Member(
    first_name='himan',
    last_name='falahi',
    user_name='himan.falah',
    password='1375',
)

DBsession.add(member2)

member3 = Member(
    first_name='mohammad',
    last_name='sheykhiyan',
    user_name='mohammad.sheykh',
    password='1369',
)

DBsession.add(member3)

member4 = Member(
    first_name='mina',
    last_name='minai',
    user_name='mina.ka',
    password='1374',
)

DBsession.add(member4)
DBsession.commit()

added_member = DBsession.query(Member) \
    .filter(Member.user_name == 'ali.ka') \
    .one_or_none()

print(added_member.last_name)

list_of_members = DBsession.query(Member) \
    .all()

for member in list_of_members:
    print(member.user_name, member.last_name)

added_of_members_ordered_by_names = DBsession.query(Member) \
    .order_by(Member.user_name) \
    .all()

for member in added_of_members_ordered_by_names:
    print(member.user_name)

added_one_of_their_member_list = DBsession.query(Member) \
    .filter(Member.user_name == 'mohammad.sheykh') \
    .first()

added_one_of_their_member_list = DBsession.query(func.count(Member.last_name)) \
    .group_by(Member.user_name)

print(added_one_of_their_member_list)

order_count_of_member = DBsession.query(Member) \
   .count()

print(order_count_of_member)


