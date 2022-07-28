from flask import Flask, render_template, jsonify
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

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/cd9e64089b1d214c3a20'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts, blog_num=int(num))

if __name__ == '__main__':
    app.run(debug=True)
