from sqlalchemy import Column, Integer, String
from base import Base

class Technician(Base):
    __tablename__ = 'technician'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    expertise = Column(String)
    