from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/<name>")
def hello(name):
    return render_template("hello!.html", content=name)

if __name__ == "__main__":
    app.run()
