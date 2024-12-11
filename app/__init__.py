from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["SECRET_KEY"] = ""
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
admin = Admin(app, name="HelpDesk Admin Panel", template_mode="bootstrap4")

from app import routes, models