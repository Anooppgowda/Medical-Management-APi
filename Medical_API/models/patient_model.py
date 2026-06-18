from pydantic import BaseModel, Field
from datetime import date

# This model defines what data our API expects when adding a new patient (POST request)
class PatientCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., example=30)
    gender: str = Field(..., example="Male")
    disease: str = Field(..., example="Flu")
    doctor_name: str = Field(..., example="Dr. Smith")
    admission_date: date = Field(..., example="2026-06-18")
    phone_number: str = Field(..., example="1234567890")

# This model defines what data our API sends back (Includes the automatic ID from MySQL)
class PatientResponse(PatientCreate):
    id: int