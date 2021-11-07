from flask import current_app, Blueprint

bp = Blueprint('api', __name__)

from app.api import queries


##def create_app(config_class=Config):
##    app = Flask(__name__)

    # ...

