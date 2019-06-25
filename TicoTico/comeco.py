from flask import Flask, render_template, request, redirect, url_for, session
from peewee import *
from pessoa import Pessoa

lista_global = []

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
    nome = request.form["nome"]
    dd = request.form["dia"]
    mm = request.form["mes"]
    aaaa = request.form["ano"]
    rg = request.form["rg"]
    cpf = request.form["cpf"]
    rua = request.form["rua"]
    numero = request.form["numero"]
    bairro = request.form["bairro"]
    estado = request.form["estado"]
    cidade = request.form["cidade"]
    cep = request.form["cep"]
    email = request.form["email"]
    imagem = request.form["imagem"]
    login = request.form["login"]
    senha = request.form["senha"]
    senhaconfirma = request.form["senhaconfirma"]
    lista_global.append(Pessoa(nome, dd, mm, aaaa, rg, cpf, rua, numero, bairro, estado, cidade, cep, email, imagem, login, senha, senhaconfirma))
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
    if login == "poliana" and senha == "123":
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

app.config['SECRET_KEY'] = 'RYDYDYT'
app.run(host="0.0.0.0", debug=True)

