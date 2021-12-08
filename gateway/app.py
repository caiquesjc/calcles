from flask import Flask, request
from waitress import serve
import requests
from flask_cors import CORS
import get_db



app = Flask(__name__)
CORS(app)

service_registry = []


db = get_db.selectAll()
for k in db:
    service_registry.append({'operation':k[0], 'address':k[1], 'port':k[2], 'route':k[3]})


@app.route('/api/<operation>', methods=['POST', 'GET'])
def api_gateway(operation):
    print("operation")
    for service_config in service_registry:
        if service_config['operation'] == ('/'+operation):
            print(service_config)
            if request.method == "GET":
                url = 'http://' + service_config['address'] +':' + service_config['port'] + service_config['route'] 
                result = requests.get(url)
                return result.json()
            elif request.method == "POST":
                url = 'http://' + service_config['address'] +':' + service_config['port'] + service_config['route']
                result = requests.post(url, json=request.json)
                return result.json()
    else:
        return "unauthorized method"

if __name__ == "__main__":
    print(f"acesse a porta: {5502}")
    serve(app, host="0.0.0.0", port=5502)
