import pandas as pd
import json


class Save:
    """
    A class to handle saving data into CSV and JSON formats.

    Attributes:
        data: JSON-formatted data to be saved.

    Methods:
        __init__(data): Constructor that initializes the class with JSON-formatted data.
        save_csv(): Converts the JSON data to a DataFrame and saves it as a CSV file.
        save_json(): Saves the JSON data directly as a JSON file.
    """
    def __init__(self, data):
        self.data = json.dumps(data)

    def save_csv(self):
        csv_data = pd.read_json(self.data)
        csv_data.to_csv("data/csv/dataset.csv", index=False)

    def save_json(self):
        with open("data/json/dataset.csv", "w") as outfile:
            json.dump(self.data, outfile)
