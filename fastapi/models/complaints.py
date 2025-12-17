from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Complaints(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey("users.id"))
    collector_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    category = Column(String)
    officer_name = Column(String)

    village = Column(String)
    district = Column(String)

    incident_date = Column(Date)
    description = Column(String)

    is_anonymous = Column(Boolean, default=False)

    contact_name = Column(String, nullable=True)
    contact_phone = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)

    # Relationships
    actions = relationship("Actions", back_populates="complaint")
