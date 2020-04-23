from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SessonMaker:

    def __init__(self, user, password, host, port, database):
        con_str = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, database)
        self.engine = create_engine(con_str, echo=True)

    @property
    def session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()
