from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Olá, Mundo!</h1><p>Esta é uma aplicação Flask rodando em um container Docker.</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)