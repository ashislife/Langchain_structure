from pydantic import BaseModel, ValidationError, Field

class Student(BaseModel):
    name: str 

new_student = {"name": "Ashish"} 

student=Student(**new_student)

print(student)  # Output: name='Ashish'
print(type(student))  