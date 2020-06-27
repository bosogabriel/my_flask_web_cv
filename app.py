from flask import Flask, render_template
from jinja2 import Template, Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = Template('Hello {{ name }}!')
app = Flask(__name__)

@app.route("/")
def home():
    nums=range(6)
    index=['Inicio','Experiencia','Proyectos','Metricas']
    return render_template("index.html", nums=nums, index=index)

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