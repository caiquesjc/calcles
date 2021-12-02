from flask import Flask, request
from waitress import serve
from flask_cors import CORS
import requests
import time
from math import sin

app = Flask(__name__)
CORS(app)


@app.route("/calcula", methods=['POST'])
def calcula():
    try:
        req = request.get_json()
        args = req["args"]
        res = {"args": [], "op": "", "result": str(eval(req["args"]))}
        for k in args:
            if not k.isdigit():
                res["op"] = k
                res["args"] = req["args"].split(k)
        if "**" in args:
            res["op"] = "**"

        requests.post("http://192.168.100.6:9905/inserir", json={
            "date_op": time.strftime('%Y-%m-%d %H:%M:%S'),
            "type_op": 1,
            "spec_op": str(res["op"]),
            "args_op": str(res["args"])
        })
        return res
    except:
        return "An exception occurred"


@app.route("/seno", methods=['POST'])
def seno():
    try:
        req = request.get_json()
        res = {"arg": req["arg"], "op": "seno",
               "result": str(sin(float(req["arg"])))}

        requests.post("http://192.168.100.6:9905/inserir", json={
            "date_op": time.strftime('%Y-%m-%d %H:%M:%S'),
            "type_op": 1,
            "spec_op": res["op"],
            "args_op": res["arg"]
        })

        return res
    except:
        return "An exception occurred"


if __name__ == '__main__':
    print(f"acesse a porta: {9903}")
    serve(app, host="0.0.0.0", port=9903)
