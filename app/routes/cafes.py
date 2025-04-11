from flask import Blueprint, jsonify, request
from app.models import Cafe
from app import db
import random
from app.utils.auth import is_authorized

cafes_bp = Blueprint('cafes', __name__)

@cafes_bp.route('/random', methods=['GET'])
def get_random_cafe():
    cafes = Cafe.query.all()
    if not cafes:
        return jsonify(error="No cafes found."), 404
    cafe = random.choice(cafes)
    return jsonify(cafe=cafe.to_dict())

@cafes_bp.route('/add', methods=['POST'])
def add_cafe():
    data = request.form
    new_cafe = Cafe(
        name=data.get('name'),
        location=data.get('location'),
        has_wifi=bool(int(data.get('has_wifi', 0))),
        has_sockets=bool(int(data.get('has_sockets', 0))),
        has_toilet=bool(int(data.get('has_toilet', 0))),
        coffee_price=data.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe added."}), 201

@cafes_bp.route('/cafes/search', methods=['GET'])
def search_cafes_by_location():
    location_query = request.args.get('location')
    if not location_query:
        return jsonify(error="Please provide a location query using ?location=CityName"), 400

    results = Cafe.query.filter(Cafe.location.ilike(f"%{location_query}%")).all()
    
    if not results:
        return jsonify(message="No cafes found for that location."), 404
    
    return jsonify(results=[cafe.to_dict() for cafe in results])

@cafes_bp.route('/cafes', methods=['GET'])
def get_filtered_cafes():
    query = Cafe.query

    has_wifi = request.args.get('has_wifi')
    if has_wifi is not None:
        query = query.filter(Cafe.has_wifi == (has_wifi.lower() == "true"))

    has_sockets = request.args.get('has_sockets')
    if has_sockets is not None:
        query = query.filter(Cafe.has_sockets == (has_sockets.lower() == "true"))

    sort_by = request.args.get('sort')
    if sort_by == 'name':
        query = query.order_by(Cafe.name.asc())
    elif sort_by == 'coffee_price':
        query = query.order_by(Cafe.coffee_price.asc())

    limit = request.args.get('limit')
    if limit is not None:
        try:
            limit = int(limit)
            query = query.limit(limit)
        except ValueError:
            return jsonify(error="Invalid limit. Must be an integer."), 400

    cafes = query.all()
    if not cafes:
        return jsonify(message="No cafes match the given filters."), 404

    return jsonify(filtered_results=[cafe.to_dict() for cafe in cafes])

@cafes_bp.route('/cafes/<int:cafe_id>/update-price', methods=['PATCH'])
def update_cafe_price(cafe_id):
    if not is_authorized(request):
        return jsonify(error="Unauthorized. Missing or invalid API key."), 403

    new_price = request.args.get('new_price')
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": f"Updated cafe {cafe.name} price to {new_price}."})
    else:
        return jsonify(error="Cafe not found."), 404

@cafes_bp.route('/cafes/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    if not is_authorized(request):
        return jsonify(error="Unauthorized. Missing or invalid API key."), 403

    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": f"Cafe {cafe.name} deleted."})
    else:
        return jsonify(error="Cafe not found."), 404

@cafes_bp.route('/docs', methods=['GET'])
def api_docs():
    docs = {
        "endpoints": [
            {
                "route": "/random",
                "method": "GET",
                "description": "Returns a random cafe."
            },
            {
                "route": "/cafes",
                "method": "GET",
                "description": "Returns all cafes with optional filters, sorting, and limit.",
                "query_params": {
                    "has_wifi": "true/false",
                    "has_sockets": "true/false",
                    "sort": "name / coffee_price",
                    "limit": "integer"
                }
            },
            {
                "route": "/cafes/search",
                "method": "GET",
                "description": "Search cafes by location.",
                "query_params": {
                    "location": "string (e.g. New York)"
                }
            },
            {
                "route": "/add",
                "method": "POST",
                "description": "Add a new cafe.",
                "form_fields": ["name", "location", "has_wifi", "has_sockets", "has_toilet", "coffee_price"]
            },
            {
                "route": "/cafes/<id>/update-price",
                "method": "PATCH",
                "description": "Update the coffee price of a cafe.",
                "query_params": {
                    "new_price": "string (e.g. $2.99)"
                },
                "headers": {
                    "x-api-key": "TopSecretAPIKey"
                }
            },
            {
                "route": "/cafes/<id>",
                "method": "DELETE",
                "description": "Delete a cafe by ID.",
                "headers": {
                    "x-api-key": "TopSecretAPIKey"
                }
            }
        ]
    }
    return jsonify(docs)
