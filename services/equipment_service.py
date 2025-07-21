from models.equipment import Equipment
from decorators.decorators import use_session, cache_query, handle_exceptions
from datetime import date

#@handle_exceptions
@use_session
#@cache_query(timeout=300)
def get_active_equipment(session):
    return session.query(Equipment).filter_by(status= "Active").all()


@handle_exceptions
@use_session
def get_equipment_due_for_service(session):
    today = date.today()
    return session.query(Equipment).filter(Equipment.next_service_date <= today).all()