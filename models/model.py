import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://root:root@192.168.100.49:3306/calcles")

Base = declarative_base()


class Logs(Base):
    __tablename__ = 'logs'
    op_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date_op = sqlalchemy.Column(sqlalchemy.String(length=100))
    type_op = sqlalchemy.Column(sqlalchemy.Integer)
    spec_op = sqlalchemy.Column(sqlalchemy.String(length=100))
    args_op = sqlalchemy.Column(sqlalchemy.String(length=100))


class TypeOp(Base):
    __tablename__ = 'typeop'
    op_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name_op = sqlalchemy.Column(sqlalchemy.String(length=100))


Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


def addLog(date_op, type_op, spec_op, args_op):
    newLogs = Logs(date_op=date_op, type_op=type_op, spec_op=spec_op, args_op=args_op)
    session.add(newLogs)
    session.commit()


def selectAll():
    logs = session.query(Logs, TypeOp).join(TypeOp, Logs.type_op == TypeOp.op_id)
    return logs


def addOp(op_id, name_op):
    newOp = TypeOp(op_id=op_id, name_op=name_op)
    session.add(newOp)
    session.commit()


# addOp(1, "elementar")
# addOp(2, "seno")
# addOp(3, "transcendental")
