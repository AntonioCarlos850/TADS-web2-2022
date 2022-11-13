# IMPORTS
import random
import string
from flask import Flask, render_template, request
from datetime import datetime

# IMPORTAR a classe Cliente do arquivo entidades.py
from entidades import Cliente

# criado o servidor web (flask)
app = Flask(__name__)
# Flask é a classe
# app é a instancia (objeto)

# http://localhost:5000/


@app.route("/", methods=["POST", "GET"])  # caminho da pagina principal
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.form.get("password") != request.form.get("password-conf"):
        return render_template('index.html', error="senhas incorretas")
    letters = string.ascii_lowercase
    uuid = (''.join(random.choice(letters) for i in range(30)))
    cliente = Cliente(uuid, request.form.get("name"), request.form.get("cpf"),
                      request.form.get("cep"), request.form.get("tel"),
                      request.form.get("password"), request.form.get("nasc"),
                      request.form.get("email")
                      )

    success = "Usuário criado: "+str(cliente.nome)
    return render_template('index.html', success=success)


if __name__ == "__main__":
    app.run(debug=True)
