from app import app, db
from flask import render_template, url_for, request, redirect
from app.forms import TarefaForm
from app.models import Tarefa

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/tarefa/', methods=['GET', 'POST'])
def cadastrar_tarefa():
    form = TarefaForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('tarefa.html', context=context, form=form)

@app.route('/tarefa/lista/')
def lista_tarefas():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    dados = Tarefa.query.order_by('titulo')
    
    if pesquisa != '':
        dados = dados.filter(Tarefa.titulo.ilike(f'%{pesquisa}%'))
    
    context = {'dados' : dados.all()}
    return render_template('tarefa_lista.html', context=context)

