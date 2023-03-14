from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
  return "Olá, vamos dominar o mundo! (Pink e Cérebro)"


@app.route("/sobre")
def sobre():
  return "Aqui vamos postar o conteúdo de como dominar o mundo"


@app.route("/contato")
def contato():
  return "Aqui colocaremos o contato dos dominadores de mundos mais experientes do mundo"
