from flask import Flask, request
from waitress import serve
from model.model import addLog, selectAll
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/inserir", methods=['POST'])
def logAdd():
    try:
        req = request.get_json()
        addLog(req['date_op'], req['type_op'], req['spec_op'], req['args_op'])
        return dict(success=True)
    except:
        return dict(success=False)

    

@app.route("/listar")
def list_logs():
    logs = selectAll()
    logsList = []
    for log, typeop in logs:
        dic = {"op_id" : log.op_id, "date_op": log.date_op,
            "type_op": log.type_op, "spec_op":log.spec_op,
            "args_op":log.args_op, "name_op": typeop.name_op,
            "name_op":typeop.name_op, "op_type_id": typeop.op_id
            }
        logsList.append(dic)
    return dict(logs=logsList)


if __name__ =='__main__':
    print(f"acesse a porta: {9905}")
    serve(app, host="0.0.0.0", port=9905)