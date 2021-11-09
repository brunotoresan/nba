from flask import current_app
from app import db
from app.api import bp
from app.models import PlayersInfo

@bp.route('/tallest', methods=['GET'])
def get_tallest_players():
    return (PlayersInfo.query.order_by(PlayersInfo.height).all()[-1].player)