from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
  return "Olá, vamos dominar o mundo! (Pink e Cérebro)"
