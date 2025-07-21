from sqlalchemy import Column, Integer, String
from base import Base

class SparePart(Base):
    __tablename__ = 'spare_part'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    part_number = Column(String)
    stock_quantity = Column(Integer)