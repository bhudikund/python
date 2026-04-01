import os.path

from flask import Flask

app = Flask(__name__)

@app.route('/preview/<int:number>/<path:file_path>')
def preview_file(number, file_path):
    abs_path= os.path.abspath(file_path)

    try:
        with open(abs_path) as input_file:
            output_text = input_file.read(number)

        return f"{abs_path} {number} <br> {output_text}"
    except FileNotFoundError:
        return "Файл не найден"


if __name__ == "__main__":
    app.run(debug= True, port= 5555)