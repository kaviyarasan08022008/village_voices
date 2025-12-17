from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from schemas.complaints import ComplaintCreate, ComplaintResponse  
from models.complaints import Complaints


router = APIRouter(
    prefix="/complaints",
    tags=["complaints"]
)

@router.get("/all_complaints")
def get_all_complaints(db: Session = Depends(connect_to_db)):
    return db.query(Complaints).all()


@router.post("/complaints/")
def create_complaint(complaint: ComplaintCreate, db: Session = Depends(connect_to_db)):

    new_complaint = Complaints(
        
    category = complaint.category,
    officer_name = complaint.officer_name,
    village = complaint.village,
    district = complaint.district,
    incident_date = complaint.incident_date,
    description = complaint.description,
    is_anonymous = complaint.is_anonymous,
    contact_name = complaint.contact_name,    
    contact_phone = complaint.contact_phone,
    contact_email = complaint.contact_email)
    
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)
    return new_complaint        

@router.get("/{complaint_id}")
def read_complaint(complaint_id: int, db: Session = Depends(connect_to_db)):
    return db.query(Complaints).filter(
        Complaints.id == complaint_id
    ).first()

@router.put("/{complaint_id}")
def update_complaint(
    complaint_id: int,
    updated_data: ComplaintCreate,
    db: Session = Depends(connect_to_db)
):
    complaint = db.query(Complaints).filter(
        Complaints.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    for key, value in updated_data.dict().items():
        setattr(complaint, key, value)

    db.commit()
    db.refresh(complaint)
    return complaint

@router.delete("/{complaint_id}")
def delete_complaint(complaint_id: int, db: Session = Depends(connect_to_db)):
    complaint = db.query(Complaints).filter(
        Complaints.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    db.delete(complaint)
    db.commit()
    return {"message": "Complaint deleted"}