<h1 align="center">NBA</h1>

<p align="center">
  <p align="center">Projeto NBA - Projeto de Banco de Dados - Projeto de Ciência de Dados</p>
  <a href="#-sobre-o-projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>
</p>

## 🔥 Sobre o projeto
TO-DO

## 💻 Como executar
* Crie o **virtual environment** dentro do diretório do repositório<br>
`$ python3 -m venv nba_env`<br>

* Instalando as dependências (repetir esses 2 passos a cada vez que um novo pacote for instalado)<br>
`$ pip install -r requirements.txt`

* Ativando o **virtual environment**<br>
`$ source nba_env/bin/activate` (MacOS e Linux) ou <br>
`$ nba_env\Scripts\activate` (Windows)<br>

* Inicie o servidor do PostgreSQL<br>
  
* Crie um banco de dados chamado **nba** no seu PostgreSQL Client favorito (eu uso o Postbird)<br>
  
* Crie o script de migração do banco de dados:<br>
`$ flask db migrate`

* Atualize o banco de dados:<br>
`$ flask db upgrade`

* Rodando o back-end<br>
`$ flask run`