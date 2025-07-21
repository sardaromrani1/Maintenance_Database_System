#from services.equipment_service import get_active_equipment

#equipments = get_active_equipment()
#for eq in equipments:
 #   print(eq.name, eq.status)

#########################################################################
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.equipment_service import get_active_equipment

def main():
    print(get_active_equipment)
    #print(get_active_equipment())
    equipments = get_active_equipment()
    if not equipments:
        print("No active equipments found")
        return
    
    print("Active Equipments:")
    for eq in equipments:
        print(eq.name)
        
if __name__ == "__main__":
    main()
        
