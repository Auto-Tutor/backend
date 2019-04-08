import json


class Selection():
    def get_text_v1(self, data: json) -> json:
        return json.dumps({"text": """Тут должен быть какой-то возвращаемый текст"""})
