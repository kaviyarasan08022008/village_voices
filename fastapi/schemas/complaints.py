from pydantic import BaseModel
from typing import Optional
from datetime import date

class ComplaintBase(BaseModel):
    category: str
    officer_name: str
    village: str
    district: str
    incident_date: date
    description: str
    is_anonymous: bool = False

    contact_name: str
    contact_phone: str
    contact_email: str

class ComplaintCreate(ComplaintBase):
    people_id: int
    collector_id: int

class ComplaintResponse(ComplaintBase):
    id: int
    people_id: int
    collector_id: int