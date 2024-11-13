from flask import Flask, render_template
from model.ITCompany import ITCompany

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    template = 'index.html'
    it_company: ITCompany = ITCompany()
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User. name: " + name + "id:" + str(id)


def run_web():
    app.run(debug=True)