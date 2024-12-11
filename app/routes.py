from app import *

@app.route("/")
def index():
    return render_template("pages/login.html")

@app.route("/helpdesk")
def login():
    return render_template("pages/index.html")