from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from waitress import serve
from services.elementar import calcula
from services.seno import seno
from services.logs import logAdd, select
import time



env = Environment(
   loader=FileSystemLoader('./templates')
)

calculadora_template = env.get_template('Calculator.html')
logs_template = env.get_template('Logs.html')

app = Flask(__name__,static_folder="static")


@app.route('/')
def calcular():
    return calculadora_template.render()

@app.route('/logs')
def logs():
    return logs_template.render()

@app.route('/elementar', methods=['POST'])
def elementar():
    
    args = request.get_json()
    logAdd(time.strftime('%Y-%m-%d %H:%M:%S'), "elementar", args['args'], args['args'])
    
    return calcula(args['args'])

@app.route('/seno', methods=['POST'])
def seno():
    arg = request.get_json()
    return seno(arg['arg'])

@app.route("/operacao", methods=['POST'])
def operacao():
    x = request.get_json()
    result = seno(calcula(f'{x["x"]}**2')) * calcula(f'{x["x"]}+10')
    logAdd(time.strftime('%Y-%m-%d %H:%M:%S'), "transcendental", f'sen({x["x"]}^2) * ({x["x"]}+10)', x['args'])
    return result

@app.route("/listar")
def listar():
    log = select()
    return log

if __name__ =='__main__':
    #app.run('0.0.0.0', port=9900)
    serve(app, host="0.0.0.0", port=9900)