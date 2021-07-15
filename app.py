from urllib.request import Request
import json

import jsonschema
from flask import Flask, jsonify, request, abort, Response, send_file, make_response
from jsonschema import validate, ValidationError
import pandas as pd
from itertools import chain
import tempfile

from generator import Generator

app = Flask(__name__)


@app.route("/")
# Generic Python function that returns "Hello world!"
def index():
    return "Hello world!"


def get_schema(filename):
    """This function loads the given schema available"""
    with open(f'{filename}.json', 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema('generator_schema')
    message = "json is valid"
    try:
        validate(instance=json_data, schema=execute_api_schema)
    except ValidationError as err:
        message = "Error: " + err.message
        return False, message
    return True, message


# return  list(map(tuple, fake_data_list))


@app.route("/generate/test/data", methods=["POST"])
def generate_data():
    if not request.json:
        abort(400)
    content = request.json
    # fake_data = []
    # validate it
    is_valid, msg = validate_json(content)
    if is_valid:
        gen = Generator(content)
        # fake_data += gen.handler()
        resp = make_response(gen.handler().to_csv())
        resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp
    else:
        return jsonify(msg), 400

    # return jsonify(fake_data)


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(debug=True)
