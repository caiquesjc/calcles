from flask import Flask, request
import requests
from waitress import serve
from flask_cors import CORS
import time

app = Flask(__name__,static_folder="static")
CORS(app)

@app.route("/operacao", methods=['POST'])
def operacao():

    arg = request.get_json()

    res_x2 = requests.post("http://192.168.100.6:5502/api/elementar",json={"args":f'{arg["x"]}**2'}).json()["result"]
    
    res_x10 = requests.post("http://192.168.100.6:5502/api/elementar",json={"args":f'{arg["x"]}+10'}).json()["result"]

    res_sen = requests.post("http://192.168.100.6:5502/api/seno",json={"arg": res_x2}).json()["result"]

    resultado = requests.post("http://192.168.100.6:5502/api/elementar",json={"args":f'{res_sen}*{res_x10}'}).json()["result"]

    #logAdd(time.strftime('%Y-%m-%d %H:%M:%S'), 3, f'sen({arg["x"]}^2) * ({arg["x"]}+10)', arg['x'])
    requests.post("http://192.168.100.6:5502/api/logs-cadastrar", json={
            "date_op": time.strftime('%Y-%m-%d %H:%M:%S'),
            "type_op": 3,
            "spec_op": f'sen({arg["x"]}^2) * ({arg["x"]}+10)',
            "args_op": arg["x"]
        })
    return dict(result=resultado)

if __name__ =='__main__':
    print(f"acese a porta: {9906}")
    serve(app, host="0.0.0.0", port=9906)