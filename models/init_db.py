from models.db import engine, Base
from models.equipment import Equipment

def init_db():
    Base.metadata.create_all(bind= engine)

if __name__ == "__main__":
    init_db()