from orm import session, student  # Import the Student model

session.query(student).filter(student.id == 3).delete()  

session.commit()

print("A row has been deleted !!")