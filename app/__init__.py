from flask import Flask
from flask_sqlalchemy import SQLAlchemy #SQLAlchemy é uma biblioteca de mapeamento objeto-relacional (ORM) para Python
from flask_restful import Api #gerenciar rotas, recursos e outros aspectos para APIs RESTful
import sqlite3

app = Flask(__name__) # cria a instância do flask

# configuração com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto_alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # desativando o rastreamento de modificações do SQLAlchemy no app Flask

db = SQLAlchemy(app) # cria a instância do banco de dados
api = Api(app) # cria a instância da Api

from app.models.alunos_dados import Alunos
with app.app_context(): #garantir que as tabelas estejam prontas para uso antes de executar a aplicação Flask
    db.create_all() # vai criar todas as tabelas

from app.resources.escola_resources import Index, AlunosCreate, AlunosSearch
api.add_resource(Index, '/') #criar a rota para o index
api.add_resource(AlunosCreate, '/criar') # criar a rota para o API para criar os dados
api.add_resource(AlunosSearch, '/buscar')