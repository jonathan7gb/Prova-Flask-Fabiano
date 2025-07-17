from app import db
from flask_sqlalchemy import SQLAlchemy

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data_limite = db.Column(db.String(100), nullable=False)