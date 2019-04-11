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
    # pega o nome fornecido para exclusão
    nome = request.args.get("nome")

    # percorre a lista de pessoas
    for i in lista_global:
        # se o nome da pessoa atual for igual ao nome definido para exclusão    
        if i.nome == nome:
            # remove a pessoa da lista
            lista_global.remove(i)
            break
    return listar_pessoas()

@app.route("/form_alterar_pessoa")
def form_alterar():
    nome = request.args.get("nome")
    for p in lista_global:
        if p.nome == nome:
            return render_template("form_alterar_pessoa.html", pessoa = p)
    return "Pessoa não encontrada:" +nome

@app.route("/alterar_pessoa")
def alterar_pessoa():
    procurar = request.args.get("nome_original")
    nome = request.args.get("nome")
    idade = request.args.get("idade")

app.run(host="0.0.0.0", debug=True)
