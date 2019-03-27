from flask import Flask, render_template, request
from pessoa import Pessoa

app = Flask(__name__)
lista = [Pessoa("Maria", "18")]

@app.route("/")
def listar_pessoas():
    nome = request.args.get("nome")
    idade = request.args.get("idade")
    lista.append(Pessoa(nome, idade))
    return render_template("listar_pessoas.html", pessoas = lista)

@app.route("/form_inserir_pessoas")
def inserir_pessoas():
    return render_template("form_inserir_pessoas.html")

app.run(host="0.0.0.0")
