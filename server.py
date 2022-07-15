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
    connection = requests.get(f'https://api.agify.io?name={name.lower()}')
    data = connection.json()
    age = int(data['age'])
    connection.close()
    connection = requests.get(f'https://api.genderize.io/?name={name}')
    data = connection.json()
    gender = data['gender']
    return render_template('guess.html', name=name.capitalize(), age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)

