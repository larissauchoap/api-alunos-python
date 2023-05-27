from app import db
from flask import jsonify

class Alunos(db.Model):
    __tablename__ = 'alunos_nova_versao'

    cpf = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    data_nascimento = db.Column(db.String(11))
    sexo = db.Column(db.String(9))
    idade=db.Column(db.Integer)
    nota_1 = db.Column(db.Float)
    nota_2 = db.Column(db.Float)
    media = db.Column(db.Float)

    def __init__(self, cpf, nome, data_nascimento,sexo,idade, nota_1, nota_2, media):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento =  data_nascimento
        self.sexo= sexo
        self.idade=idade
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media = media

    def json(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento,
            'sexo': self.sexo,
            'idade': self.idade,
            'nota_1': self.nota_1,
            'nota_2': self.nota_2,
            'media': self.media
        }

    def save_alunos(self):
        try:
            db.session.add(self) 
            db.session.commit() 
        except Exception as e: 
            print(e)
