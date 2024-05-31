from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BusStop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class BusRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_order = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
