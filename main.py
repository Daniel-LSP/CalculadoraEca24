from flask import Flask 
from livereload import Server
app=Flask(__name__)

@app.route("/")
def home():

    return "PAGINA DE INICIO"

if __name__ == "__main__":

    server = Server(app.wsgi_app)

    server.serve()
