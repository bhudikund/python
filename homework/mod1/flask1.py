import datetime
import os.path
import random
import re
from traceback import print_tb

from flask import Flask

app = Flask(__name__)

cars = ["Chevrolet", "Renault", "Ford", "Lada"]
cats = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
BOOK_FILE= os.path.join(BASE_DIR,'war_and_peace.txt')

words = []


def file_to_matrix():
    try:
        with open(BOOK_FILE) as book:
            text = book.read()
            from_file = re.findall(r'\w+', text)
            return from_file
    except FileNotFoundError:
        return 0

words = file_to_matrix()

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def show_cars():
    return ', '.join(cars)

@app.route('/cars/add/<string:car>')
def add_car(car):
    cars.append(car)
    return ', '.join(cars)

@app.route('/cats')
def show_cat():
    random_cat = random.choice(cats)
    return f"{random_cat}"

@app.route('/cats/add/<string:cat>')
def add_cat(cat):
    cats.append(cat)
    return 'Порода добавлена'

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f"Точное время: {current_time}"

@app.route('/get_time/future')
def get_time_future():
    time = datetime.datetime.now() + datetime.timedelta(hours= 1)
    return f"Через час будет {time}"

@app.route('/get_random_word')
def get_random_word():
    random_word= random.choice(words)
    return random_word

@app.route('/counter')
def counter():
    counter.visits +=1
    return f"{counter.visits}"

counter.visits = 0


if __name__ == '__main__':
    app.run(debug=True)