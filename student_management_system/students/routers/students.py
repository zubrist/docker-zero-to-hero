from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from db.models.students import Student, RegistrationStatus
from tortoise.contrib.pydantic import pydantic_model_creator

router = APIRouter()


# Create Pydantic model for Student
StudentPydantic = pydantic_model_creator(Student, name="Student")

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    department: str
    registration_no: Optional[str]  = None
    phone: Optional[str]  = None

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str
    registration_no: str
    registration_status: RegistrationStatus
    phone: Optional[str]  = None

    class Config:
        orm_mode = True



@router.post("/v1_0/register_student", status_code=status.HTTP_201_CREATED)
async def register_student(student: StudentCreate):
    # Here you would add password hashing logic
    student_obj = await Student.create(
        name=student.name,
        email=student.email,
        password_hash=student.password,  # Remember to hash this!
        department=student.department,
        registration_no=student.registration_no,
        phone=student.phone
    )
    #return await StudentResponse.from_tortoise_orm(student_obj)
    return {
        "status": "success",
        "data": student_obj
    }





@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int):
    try:
        return await Student.get(id=student_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

@router.get("/", response_model=List[StudentResponse])
async def get_students():
    return await Student.all()