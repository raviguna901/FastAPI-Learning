from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    company = Column(String)
    role = Column(String)
    location = Column(String)
    status = Column(String)
    salary = Column(String)
    application_date = Column(Date)
    job_link = Column(String)
    notes = Column(String)