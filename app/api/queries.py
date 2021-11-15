from flask import current_app, request
from app import db
from app.api import bp
from app.models import PlayersInfo
import json

# JOGADORES + ALTOS

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

# JOGADORES QUE + PONTUAM

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
            "player": result[0],
            "totalPoints": result[1] 
        })
    return json.dumps(response)

# TIMES QUE + PONTUAM

@bp.route('/teamsMostPoints', methods=['GET'])
def get_teams_most_points():
    results = db.engine.execute(f"""
        SELECT team, SUM(points) AS totalPoints
        FROM team_matches
        GROUP BY team
        ORDER BY totalPoints DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "totalPoints": result[1] 
        })
    return json.dumps(response)

# JOGADORES QUE + FAZEM ASSISTÊNCIAS

@bp.route('/playersMostAssists', methods=['GET'])
def get_players_most_assists():
    args = request.args
    num = args['num']
    results = db.engine.execute(f"""
        SELECT player, SUM(ast) AS totalAssists
        FROM players_matches
        GROUP BY player
        ORDER BY totalAssists DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "totalAssists": result[1] 
        })
    return json.dumps(response)

# TIMES QUE + FAZEM ASSISTÊNCIAS

@bp.route('/teamsMostAssists', methods=['GET'])
def get_teams_most_assists():
    results = db.engine.execute(f"""
        SELECT team, SUM(ast) AS totalAssists
        FROM team_matches
        GROUP BY team
        ORDER BY totalAssists DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "totalAssists": result[1] 
        })
    return json.dumps(response)

# JOGADORES COM MELHOR APROVEITAMENTO EM LANCES LIVRES

@bp.route('/playersBestFreeThrow', methods=['GET'])
def get_players_best_free_throw():
    args = request.args
    num = args['num']
    minFTA = args['minFTA']
    results = db.engine.execute(f"""
        SELECT player, CAST(ROUND(SUM(ftm) * 100.0/NULLIF(SUM(fta), 0), 2) AS FLOAT) AS freeThrowPercent, SUM(fta) AS nFreeThrows, SUM(ftm) AS nFreeThrowsScored
        FROM players_matches
        GROUP BY player
        HAVING SUM(fta) >= {minFTA}
        ORDER BY freeThrowPercent DESC, nFreeThrowsScored DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "freeThrowPercent": result[1],
            "nFreeThrows": result[2],
            "nFreeThrowsScored": result[3]
        })
    return json.dumps(response)

# TIMES QUE + FAZEM ARREMESSOS DE 3 PONTOS

@bp.route('/teamsMost3Points', methods=['GET'])
def get_teams_most_3_points():
    results = db.engine.execute(f"""
        SELECT team, SUM(tpa) AS total3Points
        FROM team_matches
        GROUP BY team
        ORDER BY total3Points DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "total3Points": result[1] 
        })
    return json.dumps(response)

# TIMES COM MELHOR APROVEITAMENTO EM ARREMESSOS DE 3 PONTOS

@bp.route('/teamsBest3Points', methods=['GET'])
def get_teams_best_3_points():
    results = db.engine.execute(f"""
        SELECT team, CAST(ROUND(SUM(tpm) * 100.0/NULLIF(SUM(tpa), 0), 2) AS FLOAT) AS ThreePointPercent, SUM(tpa) AS n3PointsAttempted, SUM(tpm) AS n3PointsScored
        FROM team_matches
        GROUP BY team
        ORDER BY ThreePointPercent DESC, n3PointsScored DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "3PointPercent": result[1],
            "n3PointsAttempted": result[2],
            "n3PointsScored": result[3]
        })
    return json.dumps(response)

# JOGADORES COM MELHOR APROVEITAMENTO EM ARREMESSOS DE 3 PONTOS

@bp.route('/playersBest3Points', methods=['GET'])
def get_players_best_3_points():
    args = request.args
    num = args['num']
    minTPA = args['minTPA']
    results = db.engine.execute(f"""
        SELECT player, CAST(ROUND(SUM(tpm) * 100.0/NULLIF(SUM(tpa), 0), 2) as FLOAT) AS ThreePointPercent, SUM(tpa) AS n3PointsAttempted, SUM(tpm) AS n3PointsScored
        FROM players_matches
        GROUP BY player
        HAVING SUM(tpa) >= {minTPA}
        ORDER BY ThreePointPercent DESC, n3PointsScored DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "3PointPercent": result[1],
            "n3PointsAttempted": result[2],
            "n3PointsScored": result[3]
        })
    return json.dumps(response)

@bp.route('/teamsMostRebounds', methods=['GET'])
def get_teams_most_rebounds():
    args = request.args
    num = args['num']
    results = db.engine.execute(f"""
        SELECT team, SUM(reb) AS totalRebounds
        FROM team_matches
        GROUP BY team
        ORDER BY totalRebounds DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "totalRebounds": result[1] 
        })
    return json.dumps(response)

@bp.route('/teamsMostBlocks', methods=['GET'])
def get_teams_most_blocks():
    args = request.args
    num = args['num']
    results = db.engine.execute(f"""
        SELECT team, SUM(blk) AS totalBlocks
        FROM team_matches
        GROUP BY team
        ORDER BY totalBlocks DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "totalBlocks": result[1] 
        })
    return json.dumps(response)

@bp.route('/playersMostBlocks', methods=['GET'])
def get_players_most_blocks():
    args = request.args
    num = args['num']
    results = db.engine.execute(f"""
        SELECT player, SUM(blk) AS totalBlocks
        FROM players_matches
        GROUP BY player
        ORDER BY totalBlocks DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "totalBlocks": result[1] 
        })
    return json.dumps(response)

@bp.route('/teamsWinHome', methods=['GET'])
def get_teams_wins_home():
    results = db.engine.execute(f"""
        SELECT team, COUNT(case when won then 1 else null end) AS totalHomeWins, COUNT(case when NOT won then 1 else null end) AS totalHomeLosses
        FROM team_matches
        WHERE match_id LIKE CONCAT(team, \' vs.%%\')
        GROUP BY team
        ORDER BY totalHomeWins DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "totalHomeWins": result[1],
            "totalHomeLosses": result[2]
        })
    return json.dumps(response)

