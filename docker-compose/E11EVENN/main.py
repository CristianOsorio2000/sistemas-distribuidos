from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError
from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db/db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.get("/data")
def read_data():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM tabla"))
        # Usamos result.keys() para obtener los nombres de las columnas y zip para combinarlos con los valores
            columns = result.keys()  # Nombres de las columnas
            data = [dict(zip(columns, row)) for row in result]
        return {"data":data}
    #añadimos una captura de excepciones para manejar posibles errores de conexión
    except ProgrammingError as e:
        return {"error": str(e)}
