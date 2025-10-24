from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection (SQLite in this case)
# "sqlite:///database.db" means a local file named 'database.db' will be used
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# Initialize the SQLAlchemy object (the database handler)
db = SQLAlchemy(app)
api = Api(app)


# Define a model (a table structure) for users
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    # Representation of the object (useful for debugging)
    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"


user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, required=True, help="Name cannot be blank")
user_args.add_argument("email", type=str, required=True, help="Email cannot be blank")

# Fields to serialize when returning responses
userFields = {"id": fields.Integer, "name": fields.String, "email": fields.String}


# Resource for handling GET and POST requests for users
class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201


api.add_resource(Users, "/api/users/")


# Define a route (URL endpoint) for the home page
@app.route("/")
def home():
    return "<h1>Flask REST API</h1>"


if __name__ == "__main__":
    app.run(debug=True)
