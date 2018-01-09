from flask import Flask, render_template, request
from wtforms import Form, StringField, validators



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/views')
def views():
    return render_template('views.html')

@app.route('/Graph')
def Graph():
    return render_template('Graph.html')

@app.route('/Details')
def details():
    return render_template('Details.html')

@app.route('/setaside')
def setaside():
    return render_template('SetAside.html')

@app.route('/enough')
def enough():
    return render_template('enough.html')

@app.route('/riskprofile')
def riskprofile():
    return render_template('riskprofile.html')

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/action1')
def transfer1():
    return render_template('action1.html')


if __name__ == '__main__':
    app.run()
