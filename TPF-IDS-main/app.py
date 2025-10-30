from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/promociones")
def onecolumn():
    return render_template("promociones.html")


@app.route("/suiteromantica")
def threecolumn():
    return render_template("suiteromantica.html")


@app.route("/suitefamiliar")
def twocolumn1():
    return render_template("suitefamiliar.html")


@app.route("/suiteamigos")
def twocolumn2():
    return render_template("suiteamigos.html")


if __name__ == "main":
    app.run("localhost", port=8000, debug=True)
