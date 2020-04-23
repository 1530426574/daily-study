import sqlalchemy, time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__, self.id, self.name, self.age)


class Session:
    @classmethod
    def create_engine(cls):
        user = 'wei'
        password = '123456'
        host = '192.168.37.141'
        port = 3306
        database = 'test1'
        s = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, database)
        engine = sqlalchemy.create_engine(s, echo=True)
        return engine

    @classmethod
    def drop_create(cls, engine):
        Base.metadata.drop_all(engine)
        time.sleep(5)
        Base.metadata.create_all(engine)

    @classmethod
    def create_instance(cls, name, age):
        s = Student(name=name)
        s.age = age
        return s

    @classmethod
    def create_session(cls, engine):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
