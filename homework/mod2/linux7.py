from flask import Flask

app = Flask(__name__)

storage= {}

@app.route('/add/<string:date>/<int:number>')
def add_expense(date, number):
    year = int(date[:4])
    month = int(date[4:6])

    storage.setdefault(year, {})
    storage[year][month] = storage[year].get(month, 0) + number
    return "Добавлено"

@app.route('/calculate/<int:year>')
def show_year(year):
    total = sum(storage.get(year, {}).values())
    return f"За год {total}"

@app.route('/calculate/<int:year>/<int:month>')
def show_year_month(year, month):
    total = storage.get(year, {}).get(month, {})

    return f"За выбранный период {total}"

if __name__ == "__main__":
    app.run(debug=True, port= 5555)