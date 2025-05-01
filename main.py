from flask import Flask 
from livereload import Server
from operaciones import suma
app=Flask(__name__)

@app.route("/")
def home():


    return '''
PAGINA DE INICIO DE LA APLICACION DE LOS NUEVOS PROGRAMADORES
<a href="/suma"> ir a la pagina de suma </a>
'''
@app.route("/suma")
def ruta_suma():
    return '''
Pagina para ejecutar suma
'''

if __name__ == "__main__":
    app.run(debug=True)

    server = Server(app.wsgi_app)

    server.serve()

