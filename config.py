import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Create the connexion application instance
connex_app = connexion.App(__name__)

# Get the underlying Flask app instance
app = connex_app.app
# Build the Sqlite ULR for SqlAlchemy
psql_url = "postgresql:///sagradofutebol"

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = psql_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

#CORS

