from fastapi import FastAPI, HTTPException, status
from typing import List
from config.database import get_db_connection
from models.patient_model import PatientCreate, PatientResponse

app = FastAPI(title="Medical Management API")

@app.get("/patients", response_model=List[PatientResponse], status_code=status.HTTP_200_OK)
def get_all_patients():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM patients")
            return cursor.fetchall()
    finally:
        connection.close()

@app.get("/patients/{id}", response_model=PatientResponse, status_code=status.HTTP_200_OK)
def get_patient_by_id(id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM patients WHERE id = %s", (id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail=f"Patient with ID {id} not found")
            return result
    finally:
        connection.close()

@app.post("/patients", status_code=status.HTTP_201_CREATED)
def add_patient(patient: PatientCreate):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO patients (name, age, gender, disease, doctor_name, admission_date, phone_number) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (
                patient.name, patient.age, patient.gender, 
                patient.disease, patient.doctor_name, 
                patient.admission_date, patient.phone_number
            ))
            connection.commit()
            return {"message": "Patient record added successfully!"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()