import json


class ReadData:

    def __init__(self, DATA_PATH):
        self.DATA_PATH = DATA_PATH

    def read_data(self):
        with open(self.DATA_PATH, 'r') as f:
            json_data = f.read()
            obj = json.loads(json_data)
            return obj

#
# search_data = ReadData(DATA_PATH="/Users/Akash.Dasgupta/PycharmProjects/SeleniumPython/test_data/search_page.json")
# print(search_data.read_data()['search-data'][0])
