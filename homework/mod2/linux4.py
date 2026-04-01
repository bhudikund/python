from datetime import datetime
from flask import Flask

app = Flask(__name__)

weekdays = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')

@app.route('/hello-world/<string:name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    return f'Привет, {name}! Хорошей {weekdays[weekday]}!'

if __name__ == '__main__':
    app.run(debug=True, port= 5555)