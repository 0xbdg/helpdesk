from flask import *
from flask_login import LoginManager,login_required, UserMixin,login_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["SECRET_KEY"] = "9df31cad3eb2f66386575da6dd6641ae"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

login_manager=LoginManager()
login_manager.init_app(app)
csrf = CSRFProtect(app)

from app import routes, models