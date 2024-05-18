import json
import pandas as pd


class JsonToCsv:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_and_save_csv:
        pass

# Open the JSON file
with open('movies.json') as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Save DataFrame as CSV
df.to_csv('movies.csv', index_label='title')
