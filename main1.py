from fastapi import FastAPI, HTTPException

from database import SessionLocal
from models import Application
from schemas import ApplicationCreate

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Interview Application Tracker API"}


# CREATE
@app.post("/applications")
def create_application(application: ApplicationCreate):

    db = SessionLocal()

    existing = db.query(Application).filter(
        Application.id == application.id
    ).first()

    if existing:
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Application already exists"
        )

    new_app = Application(
        id=application.id,
        company=application.company,
        role=application.role,
        location=application.location,
        status=application.status,
        salary=application.salary,
        application_date=application.application_date,
        job_link=application.job_link,
        notes=application.notes
    )

    db.add(new_app)
    db.commit()
    db.refresh(new_app)

    db.close()

    return {"message": "Application Added Successfully"}


# READ ALL
@app.get("/applications")
def get_applications():

    db = SessionLocal()

    applications = db.query(Application).all()

    db.close()

    return applications


# READ ONE
@app.get("/applications/{application_id}")
def get_application(application_id: int):

    db = SessionLocal()

    application = db.query(Application).filter(
        Application.id == application_id
    ).first()

    db.close()

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application


# UPDATE
@app.put("/applications/{application_id}")
def update_application(
    application_id: int,
    updated_data: ApplicationCreate
):

    db = SessionLocal()

    application = db.query(Application).filter(
        Application.id == application_id
    ).first()

    if not application:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    application.company = updated_data.company
    application.role = updated_data.role
    application.location = updated_data.location
    application.status = updated_data.status
    application.salary = updated_data.salary
    application.application_date = updated_data.application_date
    application.job_link = updated_data.job_link
    application.notes = updated_data.notes

    db.commit()

    db.close()

    return {"message": "Application Updated Successfully"}


# DELETE
@app.delete("/applications/{application_id}")
def delete_application(application_id: int):

    db = SessionLocal()

    application = db.query(Application).filter(
        Application.id == application_id
    ).first()

    if not application:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    db.delete(application)
    db.commit()

    db.close()

    return {"message": "Application Deleted Successfully"}