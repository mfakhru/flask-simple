from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")

def my_app():
    age = 23
    return render_template("index.html", myage=age)

if __name__ == "__main__":
    app.run(debug=True)