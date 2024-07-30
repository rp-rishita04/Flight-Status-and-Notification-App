from flask import Blueprint, jsonify, request
from app.services.flight_service import get_all_flights, update_flight_status

flights_blueprint = Blueprint('flights', __name__)

@flights_blueprint.route('/api/flights', methods=['GET'])
def get_flights():
    flights = get_all_flights()
    return jsonify([flight.to_dict() for flight in flights])

@flights_blueprint.route('/api/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    data = request.get_json()
    status = data.get('status')
    flight = update_flight_status(flight_id, status)
    if flight:
        return jsonify(flight.to_dict()), 200
    return jsonify({'error': 'Flight not found'}), 404
