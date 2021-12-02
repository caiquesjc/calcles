from flask import Flask, request
from waitress import serve
from math import sin
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calcula", methods=['POST'])
def calcula():
    try:
        req = request.get_json()
        res = {"arg" : req["arg"], "op": "seno", "result": str(sin(float(req["arg"])))}

        return res
    except:
        return "An exception occurred"

if __name__ =='__main__':
    print(f"acesse a porta: {9904}")
    serve(app, host="0.0.0.0", port=9904)