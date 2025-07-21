# ساخت همه جدول ها
# main.py or database_init.py

from base import Base
from db import engine

from equipment import Equipment
from technician import Technician
from maintenance import MaintenanceRecord
from failure import Failure
from SparePart import SparePart
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

#engine = create_engine("sqlite:///maintenance.db")  # or PostgreSQL / SQL Server
#SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
Base.metadata.create_all(bind= engine)
print("All tables are created")
