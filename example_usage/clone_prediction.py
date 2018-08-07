"""This file contains the code for "Clone a prediction." in the "Example Usage" section of the documentation located
at https://plantpredict-python.readthedocs.io."""

import plantpredict
from plantpredict.enumerations.transposition_model_enum import *

# authenticate with client credentials and assign TOKEN variable in plantpredict/settings.py
plantpredict.OAuth2.token(client_id=plantpredict.settings.CLIENT_ID, client_secret=plantpredict.settings.CLIENT_SECRET)

# instantiate the prediction you wish to clone, specifying its ID and project ID (visible in the URL of that prediction
# in a web browser '.../projects/{project_id}/prediction/{id}/').
project_id = 7178   # CHANGE TO YOUR PROJECT ID; this is the project inside of which you are cloning a prediction
prediction_id = 45110   # CHANGE TO YOUR PREDICTION ID; this is the prediction you
prediction_to_clone = plantpredict.Prediction(id=prediction_id, project_id=project_id)

# clone prediction (within the same project)
new_prediction_id = prediction_to_clone.clone(new_prediction_name='Cloned Prediction')

# update transposition model of new prediction
new_prediction = plantpredict.Prediction(id=new_prediction_id, project_id=project_id)
new_prediction.get()
new_prediction.transposition_model = HAY
new_prediction.update()

# delete prediction for housekeeping
new_prediction.delete()




