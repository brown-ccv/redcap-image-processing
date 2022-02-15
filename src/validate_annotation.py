import utilities as utils

# Read in config file
config_file = '/Users/mslivins/Projects/redcap-image-processing/src/validation.env'
config = utils.read_env(config_file)
print(config)

# Request all records
fields = 
# For each circled annotation, check if single annotation is within circled area