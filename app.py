from flask import Flask, render_template, request
from s_script import run_script
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/s_script", methods=['GET', 'POST'])
def result():
    name = request.form.get('name')
    name = run_script(name)
    return render_template('result.html', name=name)


app.run(debug=True)
