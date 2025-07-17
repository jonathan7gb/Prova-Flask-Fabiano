from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from app import db
from app.models import Tarefa

class TarefaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descricao = StringField('Descrição', validators=[DataRequired()])
    data_limite = StringField('Data Limite', validators=[DataRequired()])
    submit = SubmitField('Salvar')
    
    def save(self):
        tarefa = Tarefa(
            titulo = self.titulo.data,
            descricao = self.descricao.data,
            data_limite = self.data_limite.data
        )
        
        db.session.add(tarefa)
        db.session.commit()