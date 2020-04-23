import sqlalchemy, time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


def create_engine():
    global s, engine
    user = 'wei'
    password = '123456'
    host = '192.168.37.141'
    port = 3306
    database = 'test1'
    s = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, database)
    engine = sqlalchemy.create_engine(s, echo=True)
    return engine


# print(sqlalchemy.__version__)
# 1 creare engine


# 2 create base
Base = declarative_base()


# 3 create entity class
class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__, self.id, self.name, self.age)


def drop_create():
    Base.metadata.drop_all(engine)
    time.sleep(5)
    Base.metadata.create_all(engine)


def create_instance(name, age):
    global s
    # print(Student)
    # print(repr(Student.__tablename__))
    s = Student(name=name)
    # print(s.name)
    s.age = age
    # print(s.age)
    return s


# create_instance('louis',20)

# 4 create session


def create_session(engine):
    global session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


create_session(create_engine())

# def commit(instance):
#     session.add(s)
#     # print(1, instance)
#     session.commit()
# print(2, instance)

# 5 commit
# drop_create()

# s1 =create_instance('louis',20)
# s2 =create_instance('jim',30)
# s3 = create_instance('tim',25)
# slist = [s1,s2,s3]
# for i,v in  enumerate('abcdefg'):
#     slist.append(create_instance('{}s'.format(v),'{}0'.format(i+1)))
# print(slist)
# commit(s)
