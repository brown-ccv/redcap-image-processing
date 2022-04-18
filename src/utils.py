from pathlib import Path
from collections import OrderedDict
import io
import csv

from PIL import Image
from dotenv import dotenv_values
import requests
import numpy as np

def read_env(file: str) -> OrderedDict:
    config_path = Path(file)
    return dotenv_values(config_path)

def post_request(url: str, fields: dict) -> requests.models.Response:
    try:
        return requests.post(url, data=fields)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def records_to_dict(csv_str: str) -> dict:
    records_dict = {
        record['record_id']: record
        for record in list(csv.DictReader(io.StringIO(csv_str)))
    }
    return records_dict

def bytes_to_img(data: np.array) -> Image:
    size = data.shape[::-1]
    databytes = np.packbits(data, axis=1)
    return Image.frombytes(mode='1', size=size, data=databytes)