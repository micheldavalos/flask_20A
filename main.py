from flask import Flask, jsonify
from conexion import get_alumnos

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola Mundo'

@app.route('/<string:nombre>')
def home2(nombre):
    return "Hola " + nombre

@app.route('/alumno/')
def alumno():
    lista = get_alumnos()

    return jsonify(lista)

app.run()