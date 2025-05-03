from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

STUDENTS_SERVICE_URL = os.getenv("STUDENTS_SERVICE_URL", "http://students:8000")

@app.post("/api/v1_0/register_student")
async def register_student(student_data: dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{STUDENTS_SERVICE_URL}/api/students/v1_0/register_student",
                json=student_data
            )
            response.raise_for_status()  # Raise exception for 4xx and 5xx responses
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"Service unavailable: {str(exc)}")
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)