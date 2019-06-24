from flask import Flask, render_template, request, redirect, url_for, session
from peewee import *

lista_global = Pessoa.select()

db = SqliteDatabase("pessoa.db")

class BaseModelo(Model):
    class Meta():
        database = db

class Pessoa(BaseModelo):
    cpf = CharField()
    nome = CharField()
    idade = CharField()


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", pessoas = Pessoa.select())

@app.route("/form_inserir_pessoas")
def mostrar_pessoas():
    return render_template("form_inserir_pessoas.html")

@app.route("/cadastrar", methods = ["POST"])
def cadastrar_pessoas():
    cpf = request.form["cpf"]
    nome = request.form["nome"]
    idade = request.form["idade"]
    lista_global.append(Pessoa(cpf, nome, idade))
    return listar_pessoas()

@app.route("/excluir_pessoas")
def excluir():
    cpf = request.args.get("cpf")
    for i in lista_global:
        if i.cpf == cpf:
            lista_global.remove(i)
            break
    return listar_pessoas()

@app.route("/form_alterar_pessoa")
def form_alterar():
    cpf = request.args.get("cpf")
    for p in lista_global:
        if p.cpf == cpf:
            return render_template("form_alterar_pessoa.html", pessoa = p)
    return "Pessoa não encontrada:" +cpf

@app.route("/alterar_pessoa")
def alterar_pessoa():
    procurar = request.args.get("cpf_original")
    cpf = request.args.get("cpf")
    nome = request.args.get("nome")
    idade = request.args.get("idade")
    novo = Pessoa(cpf, nome, idade)
    for i in range(len(lista_global)):
        if lista_global[i].cpf == procurar:
            lista_global[i]= novo
            return redirect(url_for("listar_pessoas"))
    return "não achou" + procurar

@app.route("/login")
def login():
    login = request.args.get("login")
    senha = request.args.get("senha")
    if login == "admin" and senha == "123":
        session["usuario"] = login
        return redirect("/")
    else:
        return "erro no login e/ou senha"

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")


db.connect()

pessoa = Pessoa.create(cpf = "056987456", nome = "Poliana", idade = "17")


app.config['SECRET_KEY'] = 'RYDYDYT'
app.run(host="0.0.0.0", debug=True)

