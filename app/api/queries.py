from flask import current_app, request
from app import db
from app.api import bp
from app.models import PlayersInfo
import json

@bp.route('/tallest', methods=['GET'])
def get_tallest_players():
    results = db.engine.execute("""
        SELECT player, height
        FROM players_info
        ORDER BY height DESC
        LIMIT 1
    """)
    for result in results:
        response = {
            "name": result[0],
            "height": result[1] 
        }
    return json.dumps(response)

@bp.route('/playersMostPoints', methods=['GET'])
def get_players_most_points():
    args = request.args
    num = args['num']
    results = db.engine.execute(f"""
        SELECT player, SUM(points) AS totalPoints
        FROM players_matches
        GROUP BY player
        ORDER BY totalPoints DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "name": result[0],
            "totalPoints": result[1] 
        })
    return json.dumps(response)