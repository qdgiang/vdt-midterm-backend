import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "localhost:8080",
    "localhost"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/get_students")
def read_all_students():
    try:
        connection = psycopg2.connect(user="vdt_user",
                                    password="vdt_password",
                                    host="db",
                                    port="5432",
                                    database="vdt_db")
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, gender, university FROM vdt_student ORDER BY id ASC")
        students = cursor.fetchall()
        return students
        # jsonify the result
        # students = json.dumps(students, default=str)
    
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    



@app.get("/api/get_student/{id}")
def read_one_student(id: int):
    try:
        connection = psycopg2.connect(user="vdt_user",
                                    password="vdt_password",
                                    host="db",
                                    port="5432",
                                    database="vdt_db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT name, gender, email, phone, university FROM vdt_student WHERE id = {id}")
        student = cursor.fetchone()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return student

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

