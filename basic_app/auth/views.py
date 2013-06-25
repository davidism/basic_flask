from basic_app.auth import bp
from basic_app.auth.models import User


@bp.route("/<username>")
def hello(username):
    u = User.query.filter_by(username=username).first_or_404()
    return "Hello, {}!".format(u.username)
