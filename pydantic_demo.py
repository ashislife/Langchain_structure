# from pydantic import BaseModel, ValidationError, Field

# class Student(BaseModel):
#     name: str 

# new_student = {"name": "Ashish"} 

# student=Student(**new_student)

# print(student)  # Output: name='Ashish'
# print(type(student))  


# --------------------<>-------------------------------

# from pydantic import BaseModel, ValidationError, Field

# class Student(BaseModel):
#     name: str ='Ashish'

# new_student = {} 

# student=Student(**new_student)

# print(student.name)  # Output: Ashish


# --------------------<>-------------------------------

# if the input data is empty then it will take the default value of the field.
# from pydantic import BaseModel
# from typing import Optional 


# class Student(BaseModel):
#     name: str ='Ashish'
#     age: Optional[int] = None

# new_student = {} 

# student=Student(**new_student)

# print(student)  


# -----------------------------------------<>-----------------------------------------
# automatic type conversion and validation of the input data.
# typecorsing is done by pydantic automatically.

# from pydantic import BaseModel
# from typing import Optional 


# class Student(BaseModel):
#     name: str ='Ashish'
#     age: Optional[int] = None

# new_student = {'age': '20'} # bydefault it will convert into intezer 

# student=Student(**new_student)

# print(student) 






#----------------------------------<>----------------------------------------
# automatic validate the gmail address using pydantic EmailStr type.

# from pydantic import BaseModel, EmailStr
# from typing import Optional 


# class Student(BaseModel):
#     name: str ='Ashish'
#     age: Optional[int] = None
#     mail: Optional[EmailStr] = None

# new_student = {'age': '20', 'mail': 'ashish'}  # validate the eamil id and raise the error bc pydantic use validation 

# student=Student(**new_student)

# print(student) 


# -------------------------------<>------------------------------------------
# Apply field function using pandamic (add constraints using Field)

from pydantic import BaseModel, EmailStr,Field
from typing import Optional 


class Student(BaseModel):
    name: str ='Ashish'
    age: Optional[int] = None
    mail: Optional[EmailStr] = None

    # apply constrants on range (0-10)
    cgpa:float=Field(gt=0,lt=10)

    # add description on constraints 
    # sgpa:float=Field(gt=0,lt=20,description="Decimal value represention the SGPA of a student")

new_student = {'age': '20','mail':'ashishk00047@gmail.com','cgpa':9}  

student=Student(**new_student)

# convert into dictionary 
student_dict=dict(student)


# fetch the individual data 
print(student_dict['age'])


# convert into json file 
student_json=student.model_dump_json()