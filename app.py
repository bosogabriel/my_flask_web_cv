from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

with open("./static/experience.json") as f:
    XP=json.load(f)

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = Template('Hello {{ name }}!')

@app.route("/")
def home():
    nums=range(6)
    index=['Inicio','Experiencia','Proyectos','Metricas']
    return render_template("index.html", experience=XP)

@app.route("/experience")
def experience():
    
    return template.render(name='John Doe')

@app.route("/education")
def education():
    return "Hello, Salvador"

@app.route("/projects")
def projects():
    return "Hello, Salvador"

@app.route("/metrics")
def metrics():
    return "Hello, Salvador"

if __name__ == "__main__":
    app.run(debug=True)