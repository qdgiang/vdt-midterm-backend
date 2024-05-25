import psycopg2
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/get_students")
def read_all_students():
    try:
        connection = psycopg2.connect(user="vdt_user",
                                    password="vdt_password",
                                    host="localhost",
                                    port="5432",
                                    database="vdt_db")
        cursor = connection.cursor()
        cursor.execute("SELECT name, gender, university FROM vdt_student")
        students = cursor.fetchall()
    
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    
    return students

@app.get("/api/get_student/{id}")
def read_one_student(id: int):
    try:
        connection = psycopg2.connect(user="vdt_user",
                                    password="vdt_password",
                                    host="localhost",
                                    port="5432",
                                    database="vdt_db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM vdt_student WHERE id = {id}")
        student = cursor.fetchone()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return student


