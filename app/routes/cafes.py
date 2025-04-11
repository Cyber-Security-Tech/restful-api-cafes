from flask import Blueprint, jsonify, request
from app.models import Cafe
from app import db
import random

cafes_bp = Blueprint('cafes', __name__)

# -------------------- GET RANDOM --------------------
@cafes_bp.route('/random', methods=['GET'])
def get_random_cafe():
    cafes = Cafe.query.all()
    if not cafes:
        return jsonify(error="No cafes found."), 404
    cafe = random.choice(cafes)
    return jsonify(cafe=cafe.to_dict())

# -------------------- GET ALL --------------------
@cafes_bp.route('/all', methods=['GET'])
def get_all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

# -------------------- POST ADD --------------------
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

# -------------------- GET SEARCH BY LOCATION --------------------
@cafes_bp.route('/cafes/search', methods=['GET'])
def search_cafes_by_location():
    location_query = request.args.get('location')
    if not location_query:
        return jsonify(error="Please provide a location query using ?location=CityName"), 400

    results = Cafe.query.filter(Cafe.location.ilike(f"%{location_query}%")).all()
    
    if not results:
        return jsonify(message="No cafes found for that location."), 404
    
    return jsonify(results=[cafe.to_dict() for cafe in results])
