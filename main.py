from flask import Flask
from flask import request
from src.core.selection import Selection

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return Selection().get_text_v1(request.get_json(force=True))


if __name__ == '__main__':
    app.run()
