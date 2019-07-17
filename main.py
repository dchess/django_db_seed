import argparse
import json
import pandas as pd


class Seed:
    def __init__(self, csv=None, model=None, json=None):
        args = self._get_args()
        csv = csv or args.csv
        df = pd.read_csv(csv)
        self.records = df.to_dict("records")
        self.model = model or args.model
        self.json = json or args.json

    def _get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--csv", help="file name of csv to parse")
        parser.add_argument("--model", help="django model name")
        parser.add_argument("--json", help="file name of json to output")
        return parser.parse_args()

    def _item_schema(self, index, record):
        item = {"model": self.model, "pk": index, "fields": record}
        return item

    def _parse_csv(self):
        self.data = []
        for index, record in enumerate(self.records):
            item = self._item_schema(index + 1, record)
            self.data.append(item)

    def to_json(self):
        self._parse_csv()
        with open(self.json, "w") as f:
            json.dump(self.data, f, indent=4)


if __name__ == "__main__":
    Seed().to_json()
