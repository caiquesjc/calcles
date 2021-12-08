from sqlalchemy import text, create_engine

engine = create_engine(f"mariadb+mariadbconnector://root:root@192.168.100.49:3306/calcles")

def selectAll():
    services = engine.execute(text("select * from gateway"))
    return services

