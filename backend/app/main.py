from flask import Flask
from flask_cors import CORS
from app.api.flights import flights_blueprint
from app.utils.database import init_db

app = Flask(__name__)
CORS(app)
app.register_blueprint(flights_blueprint)

@app.before_first_request
def setup():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
