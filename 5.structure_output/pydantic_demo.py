from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # name: str
    name: str = "Nitish"  #default value
    age: Optional[int] = None
    email: EmailStr  # builtin validation
    cgpa: float = Field(gt=0, lt=10, description="Decimal value reprenting CGPA")

# new_student = {'name': "nitish"}
# new_student = {'name': 32} # error
# new_student = {'age':10}
new_student = {'age':"10"} # still it will work, Its auto converting the str to int. Its called as type coercing 

student = Student(**new_student)

print(student)