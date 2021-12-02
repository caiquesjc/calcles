from flask import Flask, request
from urllib import parse, request as req


app = Flask(__name__)

elementar = {'operation':'/elementar', 'address':'192.168.100.6', 'port':9903, 'route':'/elementar'}
seno = {'operation':'/seno', 'address':'192.168.100.6', 'port':9904, 'route':'/seno'}
logs = {'operation':'/logs', 'address':'192.168.100.6', 'port':9905, 'route':'/logs/listar'}

service_registry = [elementar, seno, logs]

@app.route('/api/<operation>')
def api_gateway(operation):
    for service_config in service_registry:
        if service_config['operation'] == ('/'+operation):
            parameters = { 'str_input': request.args.get('str_input')}
            url = 'http://' + service_config['address'] +':' + str(service_config['port']) + service_config['route'] 
            url_request = req.urlopen(url+'?'+parse.urlencode(parameters))
            result = url_request.read()
            return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
