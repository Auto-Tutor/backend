import json


class TestForm():
    def get_text_v1(self) -> json:
        return

    def login(self):
        with open('src/htmlforms/login.html', "r") as f:
            name_form = f.read()
        return name_form

    def test(self):
        with open("src/htmlforms/test.html", "r") as f:
            test_form = f.read()
        return test_form
