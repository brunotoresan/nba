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

# JOGADORES COM MAIS REBOTES

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

# TIMES COM MAIS BLOQUEIOS

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

# JOGADORES COM MAIS BLOQUEIOS

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

# TIMES QUE MAIS VENCEM EM CASA

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

# ARREMESSOS DE JOGADORES MAIS ALTOS QUE A MÊDIA

@bp.route('/playersShootingTallerThanAvg', methods=['GET'])
def  players_shooting_taller_than_avg():
    args = request.args
    shootingStat = args['shootingStat']
    results = db.engine.execute(f"""
        SELECT players_shooting.player, height, (height > (SELECT AVG(height) FROM players_info)) as isTallerThanAvg
        FROM players_shooting
        INNER JOIN players_info
        ON players_shooting.player = players_info.player
        WHERE {shootingStat} > (SELECT AVG({shootingStat}) FROM players_shooting)
        ORDER BY {shootingStat} DESC
""")
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "height": result[1],
            "isTallerThanAvg": result[2]
        })
    return json.dumps(response)

# ARREMESSOS DE JOGADORES MAIS PESADOS QUE A MÊDIA

@bp.route('/playersShootingHeavierThanAvg', methods=['GET'])
def  players_shooting_heavier_than_avg():
    args = request.args
    shootingStat = args['shootingStat']
    results = db.engine.execute(f"""
        SELECT players_shooting.player, weight, (weight > (SELECT AVG(weight) FROM players_info)) as isHeavierThanAvg
        FROM players_shooting
        INNER JOIN players_info
        ON players_shooting.player = players_info.player
        WHERE {shootingStat} > (SELECT AVG({shootingStat}) FROM players_shooting)
        ORDER BY {shootingStat} DESC
""")
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "height": result[1],
            "isHeavierThanAvg": result[2]
        })
    return json.dumps(response)

# TIMES COM MELHOR APROVEITAMENTO EM UM TIPO DE ARREMESSO

@bp.route('/teamsBestShooting', methods=['GET'])
def get_teams_best_shooting():
    args = request.args
    shootingZone = args['shootingZone']
    results = db.engine.execute(f"""
        SELECT team, CAST(to_char(SUM({shootingZone}_fgm) * 100.0/NULLIF(SUM({shootingZone}_fga), 0), 'FM999999999.00') AS FLOAT) AS shootingTypePercent, CAST(to_char(SUM({shootingZone}_fga), 'FM999999999.00') AS FLOAT) AS shootingTypeAttempted, CAST(to_char(SUM({shootingZone}_fgm), 'FM999999999.00') AS FLOAT) AS shootingTypeScored
        FROM players_shooting
        GROUP BY team
        ORDER BY shootingTypePercent DESC, shootingTypeScored DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "shootingTypePercent": result[1],
            "shootingTypeAttempted": result[2],
            "shootingTypeScored": result[3]
        })
    return json.dumps(response)

# JOGADORES COM MELHOR APROVEITAMENTO EM UM TIPO DE ARREMESSO

@bp.route('/playersBestShooting', methods=['GET'])
def get_players_best_shooting():
    args = request.args
    shootingZone = args['shootingZone']
    minShots = args['minShots']
    num = args['num']
    results = db.engine.execute(f"""
        SELECT player, CAST(to_char(SUM({shootingZone}_fgm) * 100.0/NULLIF(SUM({shootingZone}_fga), 0), 'FM999999999.00') AS FLOAT) AS shootingTypePercent, CAST(to_char(SUM({shootingZone}_fga), 'FM999999999.00') AS FLOAT) AS shootingTypeAttempted, CAST(to_char(SUM({shootingZone}_fgm), 'FM999999999.00') AS FLOAT) AS shootingTypeScored
        FROM players_shooting
        GROUP BY player
        HAVING CAST(to_char(SUM({shootingZone}_fga), 'FM999999999.00') AS FLOAT) > 0 AND CAST(to_char(SUM({shootingZone}_fga), 'FM999999999.00') AS FLOAT) >= {minShots}
        ORDER BY shootingTypePercent DESC, shootingTypeScored DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "shootingTypePercent": result[1],
            "shootingTypeAttempted": result[2],
            "shootingTypeScored": result[3]
        })
    return json.dumps(response)

# JOGADORES COM MAIS ACERTOS EM ARREMESSOS

@bp.route('/playersMVP', methods=['GET'])
def get_players_mvp():
    results = db.engine.execute(f"""
        SELECT team, player, (rar_fgm + itp_fgm + mrg_fgm + lc3_fgm + rc3_fgm + cn3_fgm + ab3_fgm) as totalShotsMade
        FROM players_shooting
        GROUP BY team, player
        ORDER BY totalShotsMade DESC
        LIMIT 10
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "player": result[1],
            "totalShotsMade": result[2]
        })
    return json.dumps(response)

# VITÓRIAS DE TIMES COM JOGADORES COM MAIS ACERTOS EM ARREMESSOS

@bp.route('/teamsWithMVP', methods=['GET'])
def get_teams_mvp():
    results = db.engine.execute(f"""
        SELECT team, SUM(case when won then 1 else null end) as numberOfWins
        FROM team_matches
        WHERE team IN (SELECT team FROM players_shooting ORDER BY (rar_fgm + itp_fgm + mrg_fgm + lc3_fgm + rc3_fgm + cn3_fgm + ab3_fgm) DESC LIMIT 10)
        GROUP BY team
        ORDER BY numberOfWins DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            "numberOfWins": result[1]
        })
    return json.dumps(response)

# VITÓRIAS DE TIMES COM MELHOR APROVEITAMENTO EM UMA JOGADA

@bp.route('/teamsWinMoves', methods=['GET'])
def get_teams_win_moves():
    args = request.args
    move = args['move']
    results = db.engine.execute(f"""
        SELECT team, CAST(ROUND(AVG({move}), 2) AS FLOAT) AS total_{move}, SUM(case when won then 1 else null end) as numberOfWins
        FROM team_matches
        GROUP BY team
        ORDER BY total_{move} DESC
    """)
    response = []
    for result in results:
        response.append({
            "team": result[0],
            f'total_{move}': result[1],
            "numberOfWins": result[2]
        })
    return json.dumps(response)

# JOGADORES COM MAIOR PORCENTAGEM DE 3 PONTOS

@bp.route('/playersBest3PointsPercentage', methods=['GET'])
def get_players_best_3_points_percentage():
    args = request.args
    minPoints = args['minPoints']
    num = args['num']
    results = db.engine.execute(f"""
        SELECT player, team, CAST(to_char(SUM(tpm) * 3 * 100.0/NULLIF(SUM(points), 0), 'FM999999999.00') AS FLOAT) AS threePointsPerc, SUM(points) AS totalPoints, SUM(tpm)*3 AS total3Points
        FROM players_matches
        GROUP BY player, team
        HAVING SUM(points) >= 3 AND SUM(points) >= {minPoints}
        ORDER BY threePointsPerc DESC
        LIMIT {num}
    """)
    response = []
    for result in results:
        response.append({
            "player": result[0],
            "team": result[1],
            "threePointsPerc": result[2],
            "totalPoints": result[3],
            "total3Points": result[4]
        })
    return json.dumps(response)