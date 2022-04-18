from pathlib import Path
import requests

from dotenv import dotenv_values


# Read .env file
config_path = Path('/Users/mslivins/Projects/redcap-image-processing/src/validation.env')
config = dotenv_values(config_path)
# Create requested fields
fields = {
    'token': config['API_TOKEN'],
    'content': 'record',
    'format': 'csv',
    'type': 'flat'}
# Send request
r = requests.post(config['API_URL'], data=fields)
print('HTTP Status: ' + str(r.status_code))

 
