from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/historia")
def historia():
    return render_template("historia.html")


# POST aceito para o botão do formulário não dar erro 405; nada é salvo.
@app.route("/m1to", methods=["GET", "POST"])
def m1to():
    return render_template("m1to.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
