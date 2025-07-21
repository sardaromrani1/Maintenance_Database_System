# Maintenance Database System
This project is a structured relational database using SQLAlchemy to manage maintenance operations in an industrial or technical environment. It covers core aspects of asset management, maintenance tracking, failure logging, spare parts inventory, and technician assignments.

## Project Overview
The **Maintenance Database System** is built using Python and SQLAlchemy ORM. It models a comprehensive and normalized schema suitable for maintenance departments in plants, refineries, or industrial facilities.

---

## Database Tables
### 1. 'equipment' - Main Assets
Represents the key assets or machines being maintained. Each asset can have multiple maintenance records and failures associated with it.

### 2. 'maintenance_record' - Maintenance Logs
Captures the historical records of maintenance tasks, including technician responsible, date, type of maintenance, and description.

### 3. 'failure' - Failure Events
Stores failure incidents related to equipment. Includes failure date, description, and any relevant observations.

### 4. 'spare_part' - Inventory
Contains information about spare parts linked to specific equipment, including quantity and specifications.

### 5. 'technician' - Personnel
Represents the technical staff involved in maintenance activities. Each technician may be linked to several maintenance records.

---

## Relationships Summary

**One-to-Many:**
- 'equipment' > 'maintenance_record'
- 'equipment' > 'failure'
- 'equipment' > 'spare_part'
- 'technician' > 'maintenance_record'
These relationships reflect the natural connection between assets and the maintenance process.

---

## Topologies Used

- Python 3.x
- SQLAlchemy (ORM)
- SQLite / PostgreSQL ( You can configure your database engine )
- Optional: Alembic for migrations

---

## Getting Started

1. Clone the repository:
   '''bash
   git clone https://github.com/sardaromrani1/maintenance_database_system.git

2. Set up a virtual environment (optional)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the database script
   python main.py



# Folder Structure (Example)

maintenance_database_system/
|
|__ models/    # SQLAlchemy ORM classes
|__ decorators/    # Session and utility decorators
|__ database/    # DB connection and engine setup
|__ utils/    # Helper functions
|__ main.py    # Entry point
|__ README.md    # Project documentation


# License
This project is open source and available under the MIT License.


# Contact
For questions and feedback, please contact [sardaromrani@gmail.com]
