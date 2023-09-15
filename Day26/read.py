from orm import session, student

# reading all data at once
results = session.query(student).all()  # [obj1, obj2, obj3]  # ORM (Object Relational Mapping)
print(results)

s2 = results[1]
print(s2.name)

for s in results:  # Use a different variable name here
    print(s.name)
    print(s.age)

filtered_students = session.query(student).filter(student.id == 3).all()  # [obj3]
for s in filtered_students:  # Use the correct variable name here
    print(s.name)






