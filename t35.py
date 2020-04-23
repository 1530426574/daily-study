from t36 import Student, Session

session = Session.create_session(Session.create_engine())

s = session.query(Student)
s2 = s.get(1)
# session.delete(s1)
print(s2)

# s2 =Student()
# s2.name ='kim'
# s2.age = 1000
# session.add(s2)
# session.commit()
