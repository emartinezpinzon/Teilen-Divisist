import json

class Setting:
    def __init__(self):
        self.secret_key = ""

        self.data = self.load_json()

    def load_json(self):
        return json.load(open('env.json'))

    def get_secret_key(self):
        self.secret_key = self.data['secret_key']

        return self.secret_key
