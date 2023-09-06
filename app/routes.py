"""Routes for parent Flask app."""
from flask import render_template, Blueprint
from flask import current_app as app

bp = Blueprint('home', __name__, url_prefix='/')


# @app.route('/')
@bp.route('/')
def home():
    """Landing page."""
    return render_template(
        'home.html'
    )

# @app.route('/edit')
@bp.route('/edit')
def edit():
    return render_template(
        'edit.html'
    )