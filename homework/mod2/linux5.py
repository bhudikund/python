from flask import Flask

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def find_max(numbers):
    split_numbers = numbers.split('/')

    valid = []

    for value in split_numbers:
        if not value:
            continue

        try:
            number = int(value)
            valid.append(number)
        except ValueError:
            return "Недопустимые значения вместе"

    max_number = max(valid)
    return f"Максимальное число: {max_number}"

if __name__ == '__main__':
    app.run(debug=True, port=5555)