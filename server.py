from flask import Flask, render_template
import random as r
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    year = dt.date.today().year
    name = 'Joey Ohannesian'
    random_number = r.randint(1, 10)
    return render_template('index.html', num=random_number, current_year=year, name=name)

@app.route('/guess/<name>')
def guess(name):
    return render_template()

if __name__ == '__main__':
    app.run(debug=True)

