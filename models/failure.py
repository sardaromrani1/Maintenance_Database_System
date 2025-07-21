from sqlalchemy import Column, Integer, ForeignKey, Date, String
from base import Base
from sqlalchemy.orm import relationship

class Failure(Base):
    __tablename__ = 'failure'

    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    date = Column(Date)
    failure_type = Column(String)
    severity = Column(String)
    reported_by = Column(String)

    equipment = relationship("Equipment", backref="failures")