from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from db.config import TORTOISE_ORM
from routers import students

app = FastAPI(title="Student Management System")

# Register Tortoise ORM
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

# Include routers
app.include_router(students.router, prefix="/api/students", tags=["students"])

@app.get("/")
async def root():
    return {"message": "Student Management System API"}