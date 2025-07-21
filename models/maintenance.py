from sqlalchemy import Column, Integer, ForeignKey, Date, String, Text
from sqlalchemy.orm import relationship
from base import Base

class MaintenanceRecord(Base):
    __tablename__ = 'maintenance_record'

    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    date = Column(Date)
    performed_by = Column(String)
    description = Column(Text)

    equipment = relationship("Equipment", backref= "maintenance_records")
    