from tortoise import fields, models
from enum import Enum
from datetime import datetime

class RegistrationStatus(str, Enum):
    PENDING = "pending" 
    TEMPORARY = "temporary"
    COMPLETE = "complete"

class Student(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100) 
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=255)
    department = fields.CharField(max_length=100)
    registration_no = fields.CharField(max_length=20, unique=True , null=True)
    phone = fields.CharField(max_length=15, null=True)
    registration_status = fields.CharEnumField(RegistrationStatus,default=RegistrationStatus.PENDING )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "students"
    def __str__(self):
        return f"{self.name} ({self.registration_no})"















