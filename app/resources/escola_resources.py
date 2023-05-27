from flask import jsonify, request
from flask_restful import Resource, reqparse
import json

from app.models.alunos_dados import Alunos

class Index(Resource):
    def get(self): # vai mostrar a mensagem abaixo
        return jsonify("Informações dos Alunos")
    
#Definir os argumentos
argumentos = reqparse.RequestParser()
argumentos.add_argument('cpf', type=int)
argumentos.add_argument('nome', type=str)
argumentos.add_argument('data_nascimento', type=str)
argumentos.add_argument('sexo', type=str)
argumentos.add_argument('idade', type=int)
argumentos.add_argument('nota_1', type=float)
argumentos.add_argument('nota_2', type=float)
argumentos.add_argument('media', type=float)

class AlunosCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            user = Alunos(**datas)
            user.save_alunos()

            return {"message": 'Aluno inserido com sucesso!'}, 201

        except Exception as error:
            return {'error': str(error)}, 500
        
class AlunosSearch(Resource):
    def get(self):
        try:
            alunos = Alunos.query.all()
            alunos_dados = [aluno.json() for aluno in alunos]
            return {'alunos_dados': alunos_dados}
        except Exception as e:
            return {'status': 500, 'msg': str(e)}, 500
        


