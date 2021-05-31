from sqlalchemy import Column, Integer, String, Text, ForeignKey, \
    Date, extract
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import column_property
from datetime import date
from datetime import datetime


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
    birth_date = Column(Date, default=date.today())
    age = column_property(date.today().year - extract('year', birth_date))
    fullname = column_property(first_name + ' ' + last_name)


    messages = relationship(
        "Message",
        back_populates='sender'
    )

    def __repr__(self):
        return "<Member('%s','%s', '%s', '%s')>" % \
               (self.first_name, self.last_name, self.user_name, self.password)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    sender_id = Column(Integer, ForeignKey('member.id'))

    sender = relationship(
        'Member',
        back_populates='messages'
    )


Base.metadata.create_all(engine)


member1 = Member(
    first_name='firstname1',
    last_name='lastname1',
    user_name='username1',
    password='1370',
    birth_date=datetime.strptime('1996-01-01','%Y-%m-%d'),
)

DBsession.add(member1)

member2 = Member(
    first_name='firstname2',
    last_name='lastname2',
    user_name='username2',
    password='1375',
    birth_date=datetime.strptime('1997-02-02','%Y-%m-%d'),
)

DBsession.add(member2)

member3 = Member(
    first_name='firstname3',
    last_name='lastname3',
    user_name='username3',
    password='1369',
    birth_date=datetime.strptime('1998-03-03','%Y-%m-%d'),
)

DBsession.add(member3)

member4 = Member(
    first_name='firstname4',
    last_name='lastname4',
    user_name='firstname4lastname 4',
    password='1374',
    birth_date=datetime.strptime('1999-04-04','%Y-%m-%d'),
)

DBsession.add(member4)

member5 = Member(
    first_name='firstname5',
    last_name='lastname5',
    user_name='username5',
    password='1390',
    birth_date=datetime.strptime('2000-05-05','%Y-%m-%d'),
)

DBsession.add(member5)

member6 = Member(
    first_name='firstname6',
    last_name='lastname6',
    user_name='username6',
    password='1396',
    birth_date=datetime.strptime('2001-06-06','%Y-%m-%d'),
)

DBsession.add(member6)

# messages query

message1 = Message(
     text='Hello world',
     sender_id=member1.id,
)

DBsession.add(message1)

message2 = Message(
    text='Hello python',
    sender_id=member2.id,
)

DBsession.add(message2)

message3 = Message(
    text='Hello pycharm',
    sender_id=member2.id,
)

DBsession.add(message3)

message4 = Message(
    text='notebook',
    sender_id=member5.id,
)

DBsession.add(message4)

message5 = Message(
    text='pencil',
    sender_id=member5.id,
)

DBsession.add(message5)

message6 = Message(
    text='book',
    sender_id=member6.id,
)

DBsession.add(message6)
DBsession.commit()

added_member_birth = DBsession.query(Member) \
    .filter(Member.user_name == member1.user_name) \
    .first()

print(added_member_birth.birth_date)

added_member_fullname = DBsession.query(Member) \
    .filter(Member.user_name == member1.user_name) \
    .first()

print(added_member_fullname.fullname)

added_member_age = DBsession.query(Member) \
    .filter(Member.user_name == member1.user_name) \
    .one_or_none()

print(added_member_age.age)

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

count_of_message = DBsession.query(Message) \
   .count()

print(count_of_message)

added_message_text = DBsession.query(Message) \
    .filter_by(text = 'Hello pycharm') \
    .first()

print(added_message_text)

member_of_message = DBsession.query(Member) \
    .filter(Member.id == message5.sender_id) \
    .one_or_none()

print(member_of_message)

count_message_of_member5 = DBsession.query(Message) \
    .filter(Message.sender_id == member5.id) \
    .count()

print(count_message_of_member5)

count_message_of_member6 = DBsession.query(Message) \
    .filter(Message.sender_id == member6.id) \
    .count()

print(count_message_of_member6)

