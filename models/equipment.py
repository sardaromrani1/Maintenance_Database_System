from sqlalchemy import Column, Integer, String, Date, Boolean
from models.db import Base


class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    model = Column(String)
    serial_number= Column(String, unique=True)
    installation_date= Column(Date)
    status= Column(String, default="Active")    # Active / Inactive / OutOfService
    calibrated= Column(Boolean, default=False)
    next_service_date= Column(Date)

    def __repr__(self):
        return f"<Equipment(id={self.id}), name='{self.name}')>"