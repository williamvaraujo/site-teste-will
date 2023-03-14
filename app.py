from flask import Flask

app = Flask(__name__)

menu = """

<a href="/">Página inicial</a> | <a href="sobre">Sobre</a> | <a href="/contato">Contato</a>
</br>
"""

@app.route("/")
def hell_world():
  return menu + "Olá, vamos dominar o mundo! (Pink e Cérebro)"


@app.route("/sobre")
def sobre():
  return menu + "Aqui vamos postar o conteúdo de como dominar o mundo"


@app.route("/contato")
def contato():
  return menu + "Aqui colocaremos o contato dos dominadores de mundos mais experientes do mundo"
