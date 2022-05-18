from flask import Flask, render_template

app = Flask(__name__)


# criar a 1º página do site
# route --> hashtagtreinamentos.com/
# função --> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/teste")
def teste():
    return render_template("teste.html")


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar

# só funciona se for chamado diretamente do programa
# se a chamada foi importada por outros programas não funciona
if __name__ == "__main__": 
    app.run(debug=True)
