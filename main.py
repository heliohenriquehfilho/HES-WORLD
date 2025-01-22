from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/jogos')
def jogos():
    return "Página de Jogos"

@app.route('/series')
def series():
    return "Página de Séries"

@app.route('/one-shot')
def one_shot():
    return "Página de One-Shot"

@app.route('/poster/inserta_futuri')
def inserta_futuri():
    return render_template("incerta_futuri.html")

@app.route('/poster/<nome>')
def poster(nome):
    return f"Você clicou no pôster: {nome}"

if __name__ == "__main__":
    app.run(debug=True)