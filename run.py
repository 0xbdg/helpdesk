from app import *

from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Role, db.session))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)