from model import Employee, Dept_emp, Department, Student, MyEnum, Title
from create_orm_session import SessonMaker
from sqlalchemy import func
from sqlalchemy.orm.query import Query

s = SessonMaker('wei', '123456', '192.168.37.141', 3306, 'test')
session = s.session


# emps = session.query(Employee).filter((Employee.emp_no>10015)&(Employee.gender==MyEnum.M))
# emps = session.query(Employee).filter((Employee.emp_no>10018)|(Employee.emp_no<10003))
# emps = session.query(Employee).filter(~(Employee.emp_no>10003))
# emps = session.query(Employee).filter(Employee.emp_no.in_([10001,10002,10003]))
# emps = session.query(Employee).filter(Employee.emp_no.notin_([10001,10002,10003]))
# a= list(emps).file
# emps = session.query(Employee).filter(Employee.last_name.like('P%'))
# emps = session.query(Employee).filter(Employee.emp_no>10015).order_by(Employee.emp_no.desc())
# print(list(emps))
# emps = session.query(Employee).limit(4).offset(18)

def show(a):
    for i in a:
        print(i)


# show(emps)

# emps= session.query(Employee).join(Dept_emp).filter(Employee.emp_no==Dept_emp.emp_no)

# print(1,len(list(emps)))
# print(2,emps.count())
# print(3,emps.all())
# print(4,emps.first())
# show(emps)
# query = session.query(func.count(Employee.emp_no))
# print(1,query.one())
# query = session.query(func.max(Employee.emp_no))
# query = session.query(func.min(Employee.emp_no))
# query = session.query(func.avg(Employee.emp_no))
# query = session.query(Employee.gender,func.max(Employee.emp_no)).group_by(Employee.gender)
# print(2,query.all())

# results = session.query(Employee).join(Dept_emp,Employee.emp_no==Dept_emp.emp_no).filter(Employee.emp_no==10010)

#
# def show_results():
#     for x in results:
#         print(1, x.emp_no)
#         print(2, x.departments)
#         print(3, x.title)
#         print(4, x)
# show_results()
# show(results)
# results = session.query(Employee).join(Title,Employee.emp_no==Title.emp_no).filter(Employee.emp_no==10010)
# show(results)
# show_results()


# 返回的是一个查询集，可以迭代。这个查询集装的是类的实例，也即表的一条条记录。

results = session.query(Employee).join(Dept_emp, Employee.emp_no == Dept_emp.emp_no).join(Department,
                                                                                          Department.dept_no == Dept_emp.dept_no).filter(
    Employee.emp_no == 10009)
# show(results)
print(0.0, type(results))
for x in results:
    print(0, type(x))
    print(1, x.departments[0].department)

# print(results.departments.__dict__)
