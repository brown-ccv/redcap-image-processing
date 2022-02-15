from pathlib import Path

import yaml
import requests
from dotenv import dotenv_values


# Read config.yaml file
# config_path = Path('/Users/mslivins/Projects/redcap-image-processing/src/config.yaml')  # TODO: fix hardcode
# with open(config_path, "r") as stream:
#     try:
#         config = yaml.safe_load(stream)
#     except yaml.YAMLError as exc:
#         print(exc)

# Read .env file
config_path = Path('/Users/mslivins/Projects/redcap-image-processing/src/validation.env')  # TODO: fix hardcode
config = dotenv_values(config_path)

# Create requested fields
fields = {
    'token': config['API_TOKEN'],
    'content': 'record',
    'format': 'csv',
    'type': 'flat'
}

# Send request
r = requests.post(config['API_URL'], data=fields)
print('HTTP Status: ' + str(r.status_code))

 
