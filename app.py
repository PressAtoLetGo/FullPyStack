# Importa dependências.
from flask import Flask, render_template, request

# Cria um aplicativo Flask.
app = Flask(__name__)

# Define a rota para a página inicial (raiz).
# Define a função da página inicial.
# Renderiza a página "home.html" e retorna para o navegador.


@app.route("/")
def home():

    # Parâmetros passados do Python para o HTML.
    params = {
        # Obrigatório - Valor da tag <title>.
        "title": "O melhor site do mundo",
        "css": "home.css",  # Opcional - Nome da folha de estilos da página.
        "js": "home.js"  # Opcional - Nome do Javascript da página.
    }
    return render_template("home.html", params=params)


# Define a rota para a página de contatos.
# Define a função da página de contatos.
# Renderiza a página "contacts.html" e retorna para o navegador.

@app.route("/contatos")
def contacts():

    params = {
        "title": "Faça Contato",  # Obrigatório - Valor da tag <title>.
        # Opcional - Nome da folha de estilos da página.
        "css": "contacts.css",
        "js": "contacts.js"  # Opcional - Nome do Javascript da página.
    }
    return render_template("contacts.html", params=params)


# Define a rota para a página de sobre.
# Define a função da página de sobre.
# Renderiza a página "about.html" e retorna para o navegador.

@app.route("/sobre")
def about():

    params = {
        "title": "Sobre...",  # Obrigatório - Valor da tag <title>.
        "css": "about.css",  # Opcional - Nome da folha de estilos da página.
    }
    return render_template("about.html", params=params)


# Define a rota para a página com as políticas de privacidade.
# Define a função da página das políticas de privacidade.
# Renderiza a página "policies.html" e retorna para o navegador.

@app.route("/privacidade")
def policies():

    params = {
        "title": "Privacidade",  # Obrigatório - Valor da tag <title>.
    }
    return render_template("policies.html", params=params)


# Define uma rota inexistente (Erro 404).
# Define a função da página de erro 404.
# Renderiza a página "404.html" e retorna para o navegador.

@app.errorhandler(404)
def not_found(e):

    params = {
        "title": "Oooops!",  # Obrigatório - Valor da tag <title>.
        "css": "404.css",  # Opcional - Nome da folha de estilos da página.
    }
    return render_template("404.html", params=params), 404


# Executa o servidor HTTP do Flask no modo "desenvolvedor".
if __name__ == "__main__":
    app.run(debug=True)
