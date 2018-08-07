"""This file contains the code for "Download nodal data." in the "Example Usage" section of the documentation located
at https://plantpredict-python.readthedocs.io."""

import plantpredict

# authenticate with client credentials and assign TOKEN variable in plantpredict/settings.py
plantpredict.OAuth2.token(client_id=plantpredict.settings.CLIENT_ID, client_secret=plantpredict.settings.CLIENT_SECRET)

# assign the nodal for which level(s) of the power plant hierarchy you desire.
export_options = {
    'export_system': False,
    'block_export_options': [{
        "name": 1,
        "export_block": False,
        "export_arrays": True,
        "export_inverters": False,
        "export_dc_fields": True
    }]
}


# instantiate a prediction, specifying its ID and project ID (visible in the URL of that prediction in a web browser
# '.../projects/{project_id}/prediction/{id}/').
project_id = 7178   # CHANGE TO YOUR PROJECT ID
prediction_id = 45110   # CHANGE TO YOUR PREDICTION ID
prediction = plantpredict.Prediction(id=prediction_id, project_id=project_id)

# run prediction and call utility to wait for it to complete
prediction.run(export_options=export_options)

# retrieve the nodal data of Array 1 (in Block 1)
nodal_data_array = prediction.get_nodal_data(params={
    'block_number': 1,
    'array_number': 1
})

# retrieve the nodal data of DC  Field 1 (in Block 1 --> Array 1 --> Inverter A)
nodal_data_dc_field = prediction.get_nodal_data(params={
    'block_number': 1,
    'array_number': 1,
    'inverter_name': 'A',
    'dc_field_number': 1
})
