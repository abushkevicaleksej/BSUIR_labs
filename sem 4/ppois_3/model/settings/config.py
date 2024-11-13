import json

class ConfigClass:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config_dict = {}
        self.readFromFile()

    def readFromFile(self):
        with open(self.config_file, 'r', encoding='utf-8') as config_file:
            self.config_dict = json.load(config_file)

    def get(self, key, default=None):
        return self.config_dict.get(key, default)

