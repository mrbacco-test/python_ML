from flask import Flask, render_template
from data import Items

app = Flask(__name__)

Items = Items()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/items")
def items():
    return render_template("items.html", items = Items)




if __name__ == "__main__":
    app.run(debug=True)