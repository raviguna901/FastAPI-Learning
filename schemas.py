from pydantic import BaseModel
from datetime import date

class ApplicationCreate(BaseModel):
    id: int
    company: str
    role: str
    location: str
    status: str
    salary: str
    application_date: date
    job_link: str
    notes: str

    class Config:
        from_attributes = True