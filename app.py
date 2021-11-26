from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route("/calcula", methods=['POST'])
def calcula():
    try:
        req = request.get_json()
        args = req["args"]
        res = {"args" : [], "op": "", "res": str(eval(req["args"]))}

        for k in args:
            if not k.isdigit():
                res["op"] = k
                res["args"] = req["args"].split(k)
        return res
    except:
        return "An exception occurred"

if __name__ =='__main__':
    print(f"acesse a porta: {9903}")
    serve(app, host="0.0.0.0", port=9903)