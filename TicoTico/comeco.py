from flask import Flask, render_template, request
from pessoa import Pessoa

lista_global = []

app = Flask(__name__)


@app.route("/")
def listar_pessoas():
    return render_template("listar_pessoas.html", pessoas = lista_global)

@app.route("/form_inserir_pessoas")
def mostrar_pessoas():
    return render_template("form_inserir_pessoas.html")

@app.route("/cadastrar")
def cadastrar_pessoas():
    nome = request.args.get("nome")
    idade = request.args.get("idade")
    lista_global.append(Pessoa(nome, idade))
    return listar_pessoas()

@app.route("/excluir_pessoas")
def excluir():
    for i in lista_global:
        x = request.args.get("nome")


app.run(host="0.0.0.0")
