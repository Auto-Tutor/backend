from flask import Flask
from flask import request
import json
from src.core.selection import Selection

from src.htmlforms.testform import TestForm

app = Flask(__name__)


@app.route('/erwerwerw/', methods=['GET', 'POST'])
def hello_world():
    return Selection().get_text_v1(request.get_json(force=True))


@app.route('/', methods=['GET', 'POST'])
def hello_world_2():
    a = request.args.get('answer1')
    b = request.args.get('answer2')
    c = request.args.get('answer3')

    if a is None or b is None or c is None:
        return TestForm().get_text_v1()

    return 'Молодец, прошел тест'


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0')
