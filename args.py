import argparse


global ARGS
parser = argparse.ArgumentParser()
parser.add_argument("--merge", action="store_true", help="merge all json files")
parser.add_argument("--csv", help="file name of csv to parse")
parser.add_argument("--model", help="django model name")
parser.add_argument("--json", help="file name of json to output")
ARGS = parser.parse_args()
