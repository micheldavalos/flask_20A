import mysql.connector

bd = mysql.connector.connect(
    user='michel',
    password='12345678',
    database='escuela'
)
cursor = bd.cursor()

def get_alumnos():
    consulta = "SELECT * FROM alumno"
    cursor.execute(consulta)

    lista = []
    for row in cursor.fetchall():
        a = {
            'id': row[0],
            'nombre': row[1],
            'apellido1': row[2],
            'apellido2': row[3],
            'carrera': row[4],
            'codigo': row[5]
        }
        lista.append(a)
    return lista