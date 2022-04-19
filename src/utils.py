from pathlib import Path
from collections import OrderedDict
import io
import csv

from PIL import Image
from dotenv import dotenv_values
import requests
import numpy as np

def read_env(file: str) -> OrderedDict:
    """Read environment file.

    Args:
        file (str): File path

    Returns:
        OrderedDict: Dictionary of environment file contents.
    """
    config_path = Path(file)
    return dotenv_values(config_path)

def post_request(url: str, fields: dict) -> requests.models.Response:
    """Submits a POST request.

    Args:
        url (str): URL to POST to
        fields (dict): Data fields contained in the request

    Raises:
        SystemExit: Request exception error

    Returns:
        requests.models.Response: POST response
    """
    try:
        return requests.post(url, data=fields)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def records_to_dict(csv_str: str) -> dict:
    """Converts REDCap's exported CSV to a dictionary.

    Args:
        csv_str (str): File path to CSV

    Returns:
        dict: Dictionary of records
    """
    records_dict = {
        record['record_id']: record
        for record in list(csv.DictReader(io.StringIO(csv_str)))}
    return records_dict

def bytes_to_img(data: np.array) -> Image:
    """Converts bytes to an image.

    Args:
        data (np.array): Array of bytes

    Returns:
        Image: An image
    """
    size = data.shape[::-1]
    databytes = np.packbits(data, axis=1)
    return Image.frombytes(mode='1', size=size, data=databytes)