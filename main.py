from flask import Flask,render_template, request
from livereload import Server
from operaciones import suma
from operaciones import division_piso
app=Flask(__name__)

@app.route("/")
def home():


    return render_template("index.html")

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

