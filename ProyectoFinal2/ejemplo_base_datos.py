import sqlite3

conn = sqlite3.connect("example.sqlite3")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (identificacion INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

#cursor.execute('''CREATE TABLE IF NOT EXISTS cursos
#               (identificacion INTEGER PRIMARY KEY, nombre TEXT, comision INTEGER)''')

cursor.execute("INSERT INTO users (nombre, edad) VALUES ('Rogelio', 32)")
cursor.execute("INSERT INTO users (nombre, edad) VALUES ('Marcela', 34)")
#cursor.execute("INSERT INTO cursos (nombre, comision) VALUES ('Python', 47790)")

conn.commit()

cursor.execute("SELECT * FROM users")  # "query"

filas = cursor.fetchall()
for fila in filas:
    print(fila)

conn.close()