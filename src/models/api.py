from re import A
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime


engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:123456@127.0.0.1:3306/calcles")


Base = declarative_base()

class Logs(Base):
    __tablename__ = 'logs'
    op_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date_op = sqlalchemy.Column(sqlalchemy.Date())
    type_op = sqlalchemy.Column(sqlalchemy.String(length=100))
    spec_op = sqlalchemy.Column(sqlalchemy.String(length=100))
    args_op = sqlalchemy.Column(sqlalchemy.String(length=100))

Base.metadata.create_all(engine)


Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


def addLog(date_op, type_op, spec_op, args_op):
   newLogs = Logs(date_op=date_op, type_op=type_op, spec_op=spec_op, args_op=args_op)
   session.add(newLogs)
   session.commit()


def selectAll():
   logs = session.query(Logs).all()
   return logs




    


