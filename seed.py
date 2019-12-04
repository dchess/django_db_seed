import json
import pandas as pd
from args import ARGS


class Seed:
    def __init__(self, csv=None, model=None, json=None):
        csv = csv or ARGS.csv
        df = pd.read_csv(csv)
        df = df.where((pd.notnull(df)), None)
        self.records = df.to_dict("records")
        self.model = model or ARGS.model
        self.json = json or ARGS.json

    def _item_schema(self, record):
        item = {"model": self.model, "fields": record}
        return item

    def _parse_csv(self):
        self.data = []
        for record in self.records:
            item = self._item_schema(record)
            self.data.append(item)

    def to_json(self):
        self._parse_csv()
        with open(self.json, "w") as f:
            json.dump(self.data, f, indent=4)
