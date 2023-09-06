"""Initialize Flask app."""
from flask import Flask


def init_server():
    """Construct core Flask application."""
    server = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')
    
    with server.app_context():
        # Import parts of our core Flask app
        from . import routes
        server.register_blueprint(routes.bp)

        from .dashboard.dashboard import create_dashboard
        server = create_dashboard(server).server


        return server