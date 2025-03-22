from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # __name__ is a special variable in Python that is the name of the module.

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"

db = SQLAlchemy(app)
app.app_context().push()

from market import routes
