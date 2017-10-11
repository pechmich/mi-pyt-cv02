from flask import Flask, render_template

app = Flask(__name__)

if app.config.get('DEBUG'):
    app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return 'MI-PYT je nejlepší předmět na FITu!'


@app.route('/hello')
def hello():
    return 'Hello world!'


@app.route('/user')
@app.route('/user/<username>')
def profile(username='Dezo'):
    return render_template('user.html', name=username)


@app.route('/number/<int:number>')
def number(number):
    return 'Square: {}'.format(number * number)
