from flask import Flask, request
from waitress import serve
from models.model import addLog, selectAll

app = Flask(__name__)


@app.route("/inserir", methods=['POST'])
def logAdd():
    req = request.get_json()
    addLog(req['date_op'], req['type_op'], req['spec_op'], req['args_op'])

    return "success"

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
    print(f"acesse a porta: {9902}")
    serve(app, host="0.0.0.0", port=9902)