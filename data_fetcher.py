import requests
import json


BASE_URL = "https://api.api-ninjas.com/v1/animals?"
API_KEY = "f34fZuedb6TQDadSf68Wsw==Qg7HEFhopF0PVHNz"


def load_data_from_api(animal_name):
    url = f"{BASE_URL}name={animal_name}"
    response = requests.get(url, headers={"X-Api-Key": API_KEY})
    data = response.json()
    if len(data) == 0:
        no_output_message = [f"<h4>The animal {animal_name} doesn't exist.</h4>"]
        return no_output_message
    return data


def load_data_from_json(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def fetch_data(animal_name):
    data = load_data_from_api(animal_name)
    return data
