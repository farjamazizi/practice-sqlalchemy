from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


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
    text = Column(Text, default='')
    sender_id = Column(Integer, ForeignKey('member.id'))

    sender = relationship(
        'Member',
        back_populates='messages'
    )


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

# messages query

message1 = Message(
     text='Hello world',
)

DBsession.add(message1)

message2 = Message(
    text = 'Hello python'
)

DBsession.add(message2)

message3 = Message(
    text = 'Hello pycharm'
)

DBsession.add(message3)

message4 = Message(
    text = 'notebook'
)

DBsession.add(message4)

message5 = Message(
    text = 'pencil'
)

DBsession.add(message5)

message6 = Message(
    text = 'book'
)

DBsession.add(message6)

member5 = Member(
    first_name='firstname 5',
    last_name='lastname 5',
    user_name='username5',
    password='1390',
    messages=[message4, message5]
)

DBsession.add(member5)

member6 = Member(
    first_name='firstname 6',
    last_name='lastname 6',
    user_name='username6',
    password='1396',
    messages=[message6]
)

DBsession.add(member6)
DBsession.commit()

member1.messages=[message1]

print(member1.messages)

member2.messages=[message2, message3]

print(member2.messages)

count_of_message = DBsession.query(Message) \
   .count()

print(count_of_message)

added_member_message=DBsession.query(Member)  \
    .filter(member5.messages==[message4, message5]) \
    .first()

print(added_member_message)

added_message_text = DBsession.query(Message)\
    .filter_by(text = 'Hello pycharm')\
    .first()

print(added_message_text)

ordered_member_by_message =DBsession.query(Member) \
    .order_by(Member.messages)

print(ordered_member_by_message)

member_of_message = DBsession.query(Member) \
    .filter(Member.id == message5.sender_id)

print(member_of_message)

message_of_member = DBsession.query(Message)\
    .filter(Message.sender_id == member5.id)\
    .count()

print(message_of_member)

another_message_of_member = DBsession.query(Message)\
    .filter(Message.sender_id == member6.id)\
    .count()

print(another_message_of_member)
