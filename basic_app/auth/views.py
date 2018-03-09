from basic_app import db
from basic_app.auth import bp
from basic_app.auth.models import User
from flask import redirect


@bp.route("/view/<email>")
def view(email):
    user = User.query.filter_by(email=email).first_or_404()
    return "Hello, %s, I guessed your password is '%s'!" % (user.email, user.password)

@bp.route("/insert/<email>")
def insert(email):
    user = User(email=email, password='secret', active=True)
    db.session.add(user)
    db.session.commit()
    return redirect("/%s" % email)
