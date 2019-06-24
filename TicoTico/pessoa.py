from peewee import *
import os

arquivo = "escola.db"
db = SqliteDatabase(arquivo)

class BaseModelo(Model):
    class Meta():
        database = db

class Aluno(BaseModelo):
    matricula = CharField()
    idade = CharField()
    nome = CharField()

    def __str__(self):
        return "matricula: " + self.matricula + " nome:  " + self.nome + " idade: " + self.idade


class Disciplina(BaseModelo):
    alunos = ManyToManyField(Aluno)
    carga_horaria = CharField()
    nome = CharField()




if os.path.exists(arquivo):
    os.remove(arquivo)

db.connect()
db.create_tables([Aluno, Disciplina, Disciplina.alunos.get_through_model()])

maria = Aluno.create(matricula = "2017458534", idade = "18", nome = "Maria Luisa")
david = Aluno.create(matricula = "2017856321", idade = "17", nome = "David Davi")

programacao = Disciplina.create(carga_horaria = "120", nome = "Progração")
historia = Disciplina.create(carga_horaria = "60", nome = "História")
filosofia = Disciplina.create(carga_horaria = "30", nome = "Filosofia")

maria.disciplinas.add([programacao, historia])
david.disciplinas.add([programacao, filosofia])

todo_mundo = Disciplina.select()

for i in todo_mundo:
    print("Quem cursa a disciplina" + i.nome)
    for aluno in i.alunos:
        print(aluno.nome)
