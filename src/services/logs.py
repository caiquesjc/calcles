from models.api import addLog, selectAll

def logAdd(date_op, type_op, spec_op, args_op):
    addLog(date_op, type_op, spec_op, args_op)
    print(f" log: {date_op} - {type_op} - {spec_op} - {args_op}")
    return f" log: {date_op} - {type_op} - {spec_op} - {args_op}"


def select():
    logs = selectAll()
    logsList = []
    for log, typeop in logs:
        dic = {"op_id" : log.op_id, "date_op": log.date_op,
            "type_op": log.type_op, "spec_op":log.spec_op,
            "args_op":log.args_op, "name_op": typeop.name_op,
            "name_op":typeop.name_op, "op_type_id": typeop.op_id
            }
        logsList.append(dic)
    return logsList