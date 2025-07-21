# seed_data.py
from models.db import get_engine, SessionLocal, Base
from models.equipment import Equipment

engine = get_engine()
Base.metadata.create_all(bind= engine)

session = SessionLocal()

# Create sample equipment
equipment1 = Equipment(name= "Pump A", manufacturer= "Flowserve", status= "Active")
equipment2 = Equipment(name= "Valve B", manufacturer= "ABB", status= "Inactive")

session.add_all([equipment1, equipment2])
session.commit()
session.close()

print("Sample equipment added...")