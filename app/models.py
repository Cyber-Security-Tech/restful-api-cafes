"""
models.py – SQLAlchemy model definitions for the Café REST API.
"""

from . import db

class Cafe(db.Model):
    """
    Cafe model representing a café location and its amenities.
    Used for storing and serving data via the RESTful API.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each cafe
    name = db.Column(db.String(100), nullable=False)  # Name of the cafe
    location = db.Column(db.String(100), nullable=False)  # Address or area
    has_wifi = db.Column(db.Boolean, default=False)  # Whether the cafe has Wi-Fi
    has_sockets = db.Column(db.Boolean, default=False)  # Whether there are plug sockets
    has_toilet = db.Column(db.Boolean, default=False)  # Whether there's a restroom
    coffee_price = db.Column(db.String(10), nullable=True)  # Price of a coffee (optional)

    def to_dict(self):
        """
        Serialize the cafe instance into a dictionary.
        Useful for returning JSON responses.
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<Cafe {self.name} in {self.location}>"
