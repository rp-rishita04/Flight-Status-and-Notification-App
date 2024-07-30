from app.models.flight import Flight
from app.utils.database import db

def get_all_flights():
    return Flight.query.all()

def update_flight_status(flight_id, status):
    flight = Flight.query.get(flight_id)
    if flight:
        flight.status = status
        db.session.commit()
        return flight
    return None
