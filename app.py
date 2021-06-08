import time

from flask import Flask, render_template, request
from datetime import datetime

from todo import ToDo

app = Flask(__name__)

todo_list = [
    ToDo(1, "Implementar Formulário Lab Programação Hipermídia",
         "O professor pediu para implementar o formulário no projeto que dei andamento até aqui",
         datetime.strptime("19/05/2021 19:00", "%d/%m/%Y %H:%M")),
    ToDo(2, "Transformar o ToDoWeb em MVC",
         "O professor solicitou que eu aplicasse o MVC no projeto ToDoWeb",
         datetime.strptime("24/05/2021 19:00", "%d/%m/%Y %H:%M")),
]


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/list", methods=['GET'])
def listatodo():
    return render_template("todolist.html", todo_list=todo_list)


@app.route("/inserir", methods=['POST'])
def inserir():
    time.sleep(10)
    titulo = request.form.get('titulo', None)
    descricao = request.form.get('descricao', None)
    data_str = request.form.get('data', None)
    data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M')
    id = len(todo_list) + 1
    todo = ToDo(id, titulo, descricao, data)
    todo_list.append(todo)
    return render_template("todolist.html", todo_list=todo_list)


@app.route("/excluir/<int:id>", methods=['GET'])
def excluir(id: int):
    time.sleep(10)
    for todo in todo_list:
        if todo.id == id:
            todo_list.remove(todo)
            return render_template("home.html", todo_list=todo_list)
    return render_template("home.html", todo_list=todo_list), 404


@app.route("/busca")
def busca():
    todo_list_filtrado = []
    palavra_chave = request.args.get('palavra_chave')
    for todo in todo_list:
        if palavra_chave in todo.titulo or palavra_chave in todo.descricao:
            todo_list_filtrado.append(todo)
    return render_template("todolist.html", todo_list=todo_list_filtrado)


@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id: int):
    time.sleep(10)
    if request.method == 'GET':
        for todo in todo_list:
            if todo.id == id:
                return render_template("home.html", todo_list=todo_list, todo_atualizar=todo)
        return render_template("home.html", todo_list=todo_list), 404
    else:
        titulo = request.form.get('titulo', None)
        descricao = request.form.get('descricao', None)
        data_str = request.form.get('data', None)
        data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M')
        for todo in todo_list:
            if todo.id == id:
                todo.titulo = titulo
                todo.descricao = descricao
                todo.data = data
        return render_template("home.html", todo_list=todo_list)
