from orm import session, student  # Import the Student model

# Update a student record with ID 3
session.query(student).filter(student.id == 3).update({"name": "Ken", "age": 50})  # ORM

# Update student records with the name "Jon" to "Gita" and age to 12
session.query(student).filter(student.name == "Jon").update({"name": "Gita", "age": 12})  # ORM

# Commit the changes to the database
session.commit()

# Print a message to confirm that the updates were successful
print("Student Updated Successfully !!")