import projects  # projects definitions are placed in different file

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())


@app.route('/basic/')
def basic_route():
    return render_template("basic.html", projects=projects.setup())


@app.route('/scientific/')
def scientific_route():
    return render_template("scientific.html", projects=projects.setup())


if __name__ == "__main__":
    app.run(port='3000', host='0.0.0.0')
