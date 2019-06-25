import os
from peewee import *

arq = "pessoa.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    dd = CharField()
    mm = CharField()
    aaaa = CharField()
    rg = CharField()
    cpf = CharField()
    rua = CharField()
    numero = CharField()
    bairro = CharField()
    estado = CharField()
    cidade = CharField()
    cep = CharField()
    email = CharField()
    imagem = CharField()
    login = CharField()
    senha = CharField()
    senha = CharField()
    senhaconfirma = CharField()

    def __str__(self):
        return self.nome + " nasceu no dia " + self.dd + "/" + self.mm + "/" + self.aaaa 
if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Pessoa])

poliana = Pessoa.create(nome = "Poliana Zalasik", dd = "26", mm = "08", aaaa = "2001", rg = "8888888", cpf = "123456789876", rua = "06", numero = "06", bairro = "06", estado = "SC", cidade = "06", cep = "9999999", email = "polianaazalasik@outlook.com", imagem = "qualqueruma.png", login = "poliana", senha = "123", senhaconfirma = "123")
print(poliana)
