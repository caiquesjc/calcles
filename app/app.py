from flask import Flask
from jinja2 import Environment, FileSystemLoader
from waitress import serve
from flask_cors import CORS

env = Environment(
   loader=FileSystemLoader('./templates')
)

calculadora_template = env.get_template('Calculator.html')
logs_template = env.get_template('Logs.html')

app = Flask(__name__,static_folder="static")
CORS(app)


@app.route('/')
def calcular():
    return calculadora_template.render()

@app.route('/logs')
def logs():
    return logs_template.render()


if __name__ =='__main__':
    print(f"acese a porta: {9900}")
    serve(app, host="0.0.0.0", port=9900)