from models.api import addLog, selectAll

def logAdd(date_op, type_op, spec_op, args_op):
    addLog(date_op, type_op, spec_op, args_op)
    print(f" log: {date_op} - {type_op} - {spec_op} - {args_op}")
    return f" log: {date_op} - {type_op} - {spec_op} - {args_op}"


def select():
    logs = selectAll()
    logsList = []
    for log in logs:
        dic = {"op_id" : log.op_id, "date_op": log.date_op, "type_op": log.type_op, "spec_op":log.spec_op,  "args_op":log.args_op}
        #logsList.append(f'{log.op_id} {log.date_op} {log.type_op} {log.spec_op} {log.args_op}')
        logsList.append(dic)
        #print(f'{log.op_id} {log.date_op} {log.type_op} {log.spec_op} {log.args_op}')
    return logsList