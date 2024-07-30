from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flightuser:flightpass@db:5432/flightstatus'
db = SQLAlchemy(app)

def init_db():
    db.create_all()
