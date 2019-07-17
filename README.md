# django_db_seed
Converts .csv to Django .json seed files for use with manage.py loaddata method

## Dependencies

* Python3.7
* [Pipenv](https://pipenv.readthedocs.io/en/latest/)

## Getting Started

### Clone the repo

```
$ git clone https://github.com/kipp-bayarea/django_db_seed.git
```

### Install dependencies

```
$ pip install pipenv
$ pipenv install
```

### Run the script

This script will take four arguments.

1. --csv: The filename of the csv you want to parse
2. --model: The name of the Django model you want to load this data into
3. --json: A filename to save the json seed file as
4. --merge: Used with the --json arg. Will merge all json files into a single file for import.

**Example**:

Create json seed file from csv
```
$ pipenv run python main.py --csv "test.csv" --model "app.test" --json "test.json"
```

Merge all json files for use with django's `loaddata` method

```
$ pipenv run python main.py --merge --json "seed.json"
```

