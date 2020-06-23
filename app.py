from flask import Flask, render_template, request
from s_script import run_script

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/s_script", methods=['GET', 'POST'])
def result():
    fname = request.form.get('name')
    name = run_script(fname)
    return render_template('result.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
