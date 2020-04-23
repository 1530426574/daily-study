from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()


class MyEnum(enum.Enum):
    M = 'M'
    F = 'F'


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__, self.id, self.name, self.age)


class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    departments = relationship('Dept_emp')
    title = relationship('Title')

    # 关键在哪呢，在于最后查询集，返回的是什么，是类实例。
    # 关键在于我查询的那个表，同时又想看哪张表的数据，就关联哪张表。
    def __repr__(self):
        return '{}(no={},name={},gender={},title={},depts={},)'.format(self.__class__.__name__, self.emp_no,
                                                                       self.first_name, self.gender, self.title,
                                                                       self.departments, )


class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), nullable=False)

    def __repr__(self):
        return '{}(no={},name={})'.format(self.__class__.__name__, self.dept_no, self.dept_name)


class Dept_emp(Base):
    __tablename__ = 'dept_emp'

    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    dept_no = Column(String, ForeignKey('departments.dept_no', ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    department = relationship('Department')

    def __repr__(self):
        return '{}(empno={},deptno={},department={})'.format(self.__class__.__name__, self.emp_no, self.dept_no,
                                                             self.department)


class Title(Base):
    __tablename__ = 'titles'

    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    title = Column(String(50), primary_key=True)
    from_date = Column(Date, primary_key=True)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return '{}(empno={},title={})'.format(self.__class__.__name__, self.emp_no, self.title)
