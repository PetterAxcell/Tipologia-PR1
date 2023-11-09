import pandas as pd
import json


class Save:
    def __init__(self, data):
        self.data = json.dumps(data)

    def save_csv(self):
        csv_data = pd.read_json(self.data)
        csv_data.to_csv("data/csv/dataset.csv", index=False)

    def save_json(self):
        with open("data/json/dataset.csv", "w") as outfile:
            json.dump(self.data, outfile)
