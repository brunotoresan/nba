<h1 align="center">NBA</h1>

<p align="center">
  <p align="center">Projeto NBA - Projeto de Banco de Dados - Projeto de Ciência de Dados</p>
  <a href="#-sobre-o-projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-instalar">Como instalar</a><a href="#-como-executar">Como executar</a>
  <a href="#-como-executar">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-recursos-interessantes">Recursos interessantes</a>
</p>

## 🏀 Sobre o projeto
TO-DO

## 🤓 Como instalar
* Crie o **virtual environment** dentro do diretório do repositório<br>
`$ python3 -m venv nba_env`<br>

* Ativando o **virtual environment**<br>
`$ source nba_env/bin/activate` (MacOS e Linux) **ou** <br>
`$ nba_env\Scripts\activate` (Windows)<br>

* Instalando as dependências (repetir esses 2 passos a cada vez que um novo pacote for instalado)<br>
`$ /usr/local/opt/postgres/bin/createuser -s postgres` (***apenas se*** utiliza MacOS + HomeBrew)<br>
`$ pip install -r requirements.txt`

* Inicie o servidor do PostgreSQL<br>
`$ pg_ctl -D /usr/local/var/postgres start` (MacOS + HomeBrew)<br>
  
* Crie um banco de dados chamado **nba** no seu PostgreSQL Client favorito (eu uso o Postbird)<br>

* Inicie o processo de migração do banco de dados:<br>
`$ flask db init`
  
* Crie o script de migração do banco de dados:<br>
`$ flask db migrate`

* Atualize o banco de dados:<br>
`$ flask db upgrade`

* Rode o script que insere os dados no banco:<br>
`$ python insert.py`

## 💻 Como executar
* Rodar o back-end<br>
`$ flask run`

## 🎯 Consultas disponibilizadas por endpoints
* Nome do jogador mais alto: `http://localhost:5000/api/tallest`
* Jogadores que mais pontuaram: `http://localhost:5000/api/playersMostPoints?num=100` (num=100 define o nº de jogadores a mostrar)
* Times que mais pontuaram: `http://localhost:5000/api/teamsMostPoints`
* Jogadores com mais assistências: `http://localhost:5000/api/playersMostAssists?num=100` (num=100 define o nº de jogadores a mostrar)
* Times com mais assistências: `http://localhost:5000/api/teamsMostAssists`
* Jogadores com melhor aproveitamento em lances livres: `http://localhost:5000/api/playersBestFreeThrow?num=100&minFTA=10` (num=100 define o nº de jogadores a mostrar e minFTA=10 define o número minimo de lances livres de um jogador)
* Times com mais arremessos de 3 pontos: `http://localhost:5000/api/teamsMost3Points`
* Times com melhor aproveitamento em arremessos de 3 pontos: `http://localhost:5000/api/teamsBest3Points`
* Jogadores com melhor aproveitamento em arremessos de 3 pontos: `http://localhost:5000/api/playersBest3Points?num=100&minTPA=10` (num=100 define o nº de jogadores a mostrar e minTPA=10 define o número minimo de arremessos de 3 pontos de um jogador)
* Times com maior número de rebotes: `http://localhost:5000/api/playersMostBlocks?num=10` (num=10 define o nº de times a mostrar)
* Times com maior número de bloqueios: `http://localhost:5000/api/playersMostBlocks?num=10` (num=10 define o nº de times a mostrar)
* Jogadores com maior número de bloqueios: `http://localhost:5000/api/playersMostBlocks?num=10` (num=10 define o nº de jogadores a mostrar)
* Número de vitórias em casa por time: `http://localhost:5000/api/teamsWinHome`
* Lista de jogadores com estatística maior que a média, com booleano indicando se são mais altos que a média
 `http://localhost:5000/api/playersShootingTallerThanAvg?shootingStat=rar_fgm` (shootingStat=rar_fgm define a estatística a ser usada para filtrar os jogadores)
 * Lista de jogadores com estatística maior que a média, com booleano indicando se são mais pesados que a média
 `http://localhost:5000/api/playersShootingHeavierThanAvg?shootingStat=rar_fgm` (shootingStat=rar_fgm define a estatística a ser usada para filtrar os jogadores)
 * Lista de times e os seus aproveitamentos para lances em uma zona específica da quadra: 
 `http://localhost:5000/api/teamsBestShooting?shootingZone=itp` (shootingZone=itp define a zona da quadra na qual os lances foram feitos)
 * Lista de jogadores e os seus aproveitamentos para lances em uma zona específica da quadra: 
 `http://localhost:5000/api/playersBestShooting?shootingZone=itp&minShots=1&num=50` (shootingZone=itp define a zona da quadra na qual os lances foram feitos, minShots=1 define o nº decimal mínimo de arremessos por partida que o jogador fez na temporada e num=50 define o nº de jogadores a mostrar)
 * Lista de jogadores MVP (10 jogadores com a maior soma de acertos de lances): `http://localhost:5000/api/teamsWithMVP`
 * Lista de times com jogadores MVP (10 jogadores com a maior soma de acertos de lances) junto com o número de vitórias do time: 
 `http://localhost:5000/api/teamsWithMVP`
  * Lista de times com seu aproveitamento em uma dada jogada e seu número de vitórias na temporada: `http://localhost:5000/api/teamsWinMoves?move=blk` (move=blk é a jogada)
  * Lista de jogadores pela porcentagem de pontos marcados com arremessos de 3 pontos: `http://localhost:5000/api/playersBest3PointsPercentage?minPoints=100&num=50` (minPoints=100 define o nº mínimo de pontos marcados pelo jogador e num=50 define o nº de times a mostrar)
  * Lista de jogadores ordenados pela média de pontos por partida: `http://localhost:5000/api/playersAveragePoints?num=50` (num=50 define o nº de times a mostrar)
  * Lista de times ordenados pela média de idade com a porcentagem de vitórias nos jogos: `http://localhost:5000/api/teamsAgeWins`
  * Lista de jogadores ordenados pelo aproveitamento em arremessos em uma zona específica da quadra junto com sua porcentagem de vitórias nos jogos: 
 `http://localhost:5000/api/playersShootingWins?shootingZone=ab3&minShots=1&num=50` (shootingZone=ab3 define a zona da quadra na qual os lances foram feitos, minShots=3 define o nº decimal mínimo de arremessos por partida que o jogador fez na temporada e num=50 define o nº de jogadores a mostrar)

## 🧑‍🏫 Recursos interessantes
* [Tutorial Flask + Banco de Dados](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)