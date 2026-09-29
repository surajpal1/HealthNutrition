from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bmi")
def bmi():
    return render_template("bmi.html")


@app.route("/calories")
def calories():
    return render_template("calories.html")


@app.route("/diet")
def diet():
    return render_template("diet.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Login successful hone ke baad Home page
        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Account create hone ke baad Home page
        return redirect(url_for("home"))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )