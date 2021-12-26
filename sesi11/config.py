import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bjxipvoqfwfjrm:f24ed6cae14f1a63a3e73fa9b6cd64c6c98aa9284a2bd13d44e5864d94727c34@ec2-34-200-119-220.compute-1.amazonaws.com:5432/d3kkl2vkpdhdrj', + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bjxipvoqfwfjrm:f24ed6cae14f1a63a3e73fa9b6cd64c6c98aa9284a2bd13d44e5864d94727c34@ec2-34-200-119-220.compute-1.amazonaws.com:5432/d3kkl2vkpdhdrj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)