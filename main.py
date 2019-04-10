from flask import \
    (Flask,
     request,
     g,
     session)
import json
from src.core.selection import Selection

from src.htmlforms.testform import TestForm

app = Flask(__name__)

# Мы не поняли, что это, но ладно
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/erwerwerw/', methods=['GET', 'POST'])
def hello_world():
    return Selection().get_text_v1(request.get_json(force=True))


@app.route('/', methods=['GET', 'POST'])
def hello_world_2():
    if session.get('login', None) is None:
        login = request.args.get('login')
        if login is None:
            return TestForm().login()

        session['login'] = login

    a = request.args.get('answer1')
    b = request.args.get('answer2')
    c = request.args.get('answer3')

    if a is None or b is None or c is None:
        return TestForm().test()

    return 'Молодец, прошел тест'


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0')
