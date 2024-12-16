from app import *
from .models import *
from .forms import *

from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=["POST","GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            return redirect("/helpdesk")
    return render_template("auth/login.html", form=form)

@app.route("/admin/dashboard/")
@login_required
def dashboard():
    return render_template("admin/pages/index.html")

@app.route("/helpdesk/", methods=["POST", "GET"])
@login_required
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        title = request.form.get("title")
        desc = request.form.get("desc")

        tickets = Tickets(client=name,email=email, title=title, description=desc, status="proses", datetime=datetime.now())

        db.session.add(tickets)
        db.session.commit()

        return redirect("/helpdesk")
    
    elif request.method == "GET":
        tickets = Tickets.query.all()
        return render_template("client/pages/index.html", tickets=tickets)