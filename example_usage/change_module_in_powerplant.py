"""This file contains the code for "Change the module in a power plant.." in the "Example Usage" section of the
documentation located at https://plantpredict-python.readthedocs.io."""

import plantpredict

# authenticate using API credentials
api = plantpredict.Api(
    username="insert username here",
    password="insert password here",
    client_id="insert client_id here",
    client_secret="insert client_secret here"
)

# instantiate a prediction, specifying its ID and project ID (visible in the URL of that prediction in a web browser
# '.../projects/{project_id}/prediction/{id}/').
project_id = 13161   # CHANGE TO YOUR PROJECT ID
prediction_id = 147813   # CHANGE TO YOUR PREDICTION ID
prediction = api.prediction(id=prediction_id, project_id=project_id)

# get the prediction in order to extract its powerplant ID
prediction.get()

# instantiate  powerplant and retrieve all of its attributes
powerplant = api.powerplant(prediction_id=prediction_id, project_id=project_id)
powerplant.get()

# get the ID of the module you want to replace the powerplant's current module with (visible in the URL
# of that module in a web browser '.../module/{id}/'), and retrieve the module
new_module_id = 3047
new_module = api.module(id=new_module_id)
new_module.get()

# in order to change the module in Block 1 --> Array 1 --> Inverter A --> DC Field 1,
# replace the previous module's data structure, replace the module id, and update the power plant
powerplant.blocks[0]['arrays'][0]['inverters'][0]['dc_fields'][0]['module'] = new_module.__dict__
powerplant.blocks[0]['arrays'][0]['inverters'][0]['dc_fields'][0]['module_id'] = new_module_id
powerplant.update()
