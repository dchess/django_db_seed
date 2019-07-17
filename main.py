import glob
import json
from seed import Seed
from args import ARGS


def merge_json():
    data = []
    json_files = glob.glob("*.json")
    for file in json_files:
        with open(file, "r") as f:
            j = json.load(f)
            data += j
    with open(ARGS.json, "w") as f:
        json.dump(data, f, indent=4)


def main():
    if ARGS.merge:
        merge_json()
    elif ARGS.csv:
        Seed().to_json()
    else:
        raise ValueError("Missing argument. To see list of arguments use --help.")


if __name__ == "__main__":
    main()
