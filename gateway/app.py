from flask import Flask, request
from waitress import serve
import requests
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

elementar = {'operation':'/elementar', 'address':'192.168.100.6', 'port':9903, 'route':'/calcula'}
seno = {'operation':'/seno', 'address':'192.168.100.6', 'port':9903, 'route':'/seno'}
logsListar = {'operation':'/logs-listar', 'address':'192.168.100.6', 'port':9905, 'route':'/listar'}
logsCad = {'operation':'/logs-cadastrar', 'address':'192.168.100.6', 'port':9905, 'route':'/inserir'}
operacao = {'operation':'/operacao', 'address':'192.168.100.6', 'port':9906, 'route':'/operacao'}


service_registry = [elementar, seno, logsListar, logsCad, operacao]

@app.route('/api/<operation>', methods=['POST', 'GET'])
def api_gateway(operation):

    for service_config in service_registry:
        if service_config['operation'] == ('/'+operation):
            if request.method == "GET":
                url = 'http://' + service_config['address'] +':' + str(service_config['port']) + service_config['route'] 
                result = requests.get(url)
                return result.json()
            elif request.method == "POST":
                url = 'http://' + service_config['address'] +':' + str(service_config['port']) + service_config['route']
                result = requests.post(url, json=request.json)
                return result.json()
    else:
        return "unauthorized method"

if __name__ == "__main__":
    print(f"acesse a porta: {5502}")
    serve(app, host="0.0.0.0", port=5502)
