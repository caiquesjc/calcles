from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from waitress import serve
import time
import requests
from flask_cors import CORS





env = Environment(
   loader=FileSystemLoader('./templates')
)

calculadora_template = env.get_template('Calculator.html')
logs_template = env.get_template('Logs.html')

app = Flask(__name__,static_folder="static")
CORS(app)

#tela principal
@app.route('/')
def calcular():
    return calculadora_template.render()
#tela logs
@app.route('/logs')
def logs():
    return logs_template.render()

# @app.route("/operacao", methods=['POST'])
# def operacao():

#     arg = request.get_json()

#     res_x2 = requests.post("http://192.168.100.6:9900/elementar",json={"args":f'{arg["x"]}**2'}).json()["resultado"]
    
#     res_x10 = requests.post("http://192.168.100.6:9900/elementar",json={"args":f'{arg["x"]}+10'}).json()["resultado"]

#     res_sen = requests.post("http://192.168.100.6:9900/seno",json={"arg": res_x2}).json()["resultado"]

#     resultado = requests.post("http://192.168.100.6:9900/elementar",json={"args":f'{res_sen}*{res_x10}'}).json()["resultado"]

#     logAdd(time.strftime('%Y-%m-%d %H:%M:%S'), 3, f'sen({arg["x"]}^2) * ({arg["x"]}+10)', arg['x'])
#     return dict(resultado=resultado)

# @app.route("/listar")
# def listar():
#     logs_lista = select()
#     return dict(logs=logs_lista)

if __name__ =='__main__':
    #app.run('0.0.0.0', port=9900)
    print(f"acese a porta: {9900}")
    serve(app, host="0.0.0.0", port=9900)