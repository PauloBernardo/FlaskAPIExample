from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)


app = Flask(__name__)
app.config.from_object('config')
CORS(app, origins="*")

db = SQLAlchemy(app)
ma = Marshmallow(app)


from .models import users, posts, commentaries
from .views import users, posts, helper
from .routes import users, posts
