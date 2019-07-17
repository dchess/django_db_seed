import argparse
import json
import pandas as pd


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="file name of csv to parse")
    parser.add_argument("--model", help="django model name")
    parser.add_argument("--json", help="file name of json to output")
    return parser.parse_args()


def item_schema(record, index, model):
    item = {"model": model, "pk": index, "fields": record}
    return item


def csv_to_json(csv, model):
    df = pd.read_csv(csv)
    records = df.to_dict("records")
    json_list = []
    for index, record in enumerate(records):
        item = item_schema(record, index, model)
        json_list.append(item)
    return json_list


def write_seed_file(data, json_filename):
    with open(json_filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    try:
        args = get_args()
        json_list = csv_to_json(args.csv, args.model)
        write_seed_file(json_list, args.json)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
