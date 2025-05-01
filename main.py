from flask import Flask, request
from livereload import Server
from operaciones import suma
from operaciones import division_piso
app=Flask(__name__)

@app.route("/")
def home():


    return '''
PAGINA DE INICIO DE LA APLICACION DE LOS NUEVOS PROGRAMADORES
<a href="/suma?numero1=20&numero2=30"> ir a la pagina de suma </a>
<a href="/division_piso?numero1=20&numero2=30">Ir a la pagina de division piso </a>
'''

@app.route("/suma")
def ruta_suma():
    numero1=request.args.get("numero1",type=float)
    numero2=request.args.get("numero2",type=float)
    if numero1 is None or  numero2 is None:
            return "Faltan datos"
    return f"El resultado de la suma es: {suma(numero1, numero2)}" 

@app.route("/division_piso")
def ruta_division_piso():
    numero1=request.args.get("numero1",type=float)
    numero2=request.args.get("numero2",type=float)
    if numero1 is None or  numero2 is None:
            return "Faltan datos"
    return f"El resultado de la division piso es: {division_piso(numero1, numero2)}" 

if __name__ == "__main__":
    app.run(debug=True)

    server = Server(app.wsgi_app)

    server.serve()

