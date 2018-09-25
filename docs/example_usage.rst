.. _example_usage:

Example Usage
=============

The code snippets below are practical examples of useful tasks accomplished via PlantPredict's API. All of the code
used in the examples below is available via `the source code on Github
<https://github.com/stephenkaplan/plantpredict-python/tree/master/example_usage>`_. Feel free to use and/or modify the
code in your local environment.

Every example assumes that you have first imported the plantpredict module and received an authentication token in your
Python session, as shown in Step 3 of :ref:`authentication_oauth2`.

Download nodal data.
---------------------

First, set up a dictionary containing the nodal data export options. Set the values to True according to which nodes
in the :py:class:`~plantpredict.PowerPlant` hierarchy you are interested in exporting nodal data. For each block in
'blockExportOptions', specify the block number.

.. code-block:: python

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

Instantiate a new prediction using the :py:class:`~plantpredict.Prediction` class, specifying its ID and project ID
(visible in the URL of that prediction in a web browser '.../projects/{project_id}/prediction/{id}/').

.. code-block:: python

    project_id = 7178   # CHANGE TO YOUR PROJECT ID
    prediction_id = 45110   # CHANGE TO YOUR PREDICTION ID
    prediction = plantpredict.Prediction(id=prediction_id, project_id=project_id)

Run the prediction.

.. code-block:: python

    prediction.run(export_options=export_options)

Retrieve the nodal data of Array 1 (in Block 1) and DC  Field 1 (in Block 1 --> Array 1 --> Inverter A). Note that
the lowest node (power plant hierarchy-wise) in the input dictionary specifies the nodal data returned.

.. code-block:: python

    nodal_data_array = prediction.get_nodal_data(params={
        'block_number': 1,
        'array_number': 1,
    })

    nodal_data_dc_field = prediction.get_nodal_data(params = {
        'block_number': 1,
        'array_number': 1,
        'inverter_name': 'A',
        'dc_field_number': 1
    })

The nodal data returned will be returned as JSON serializable data, as detailed in the documentation for
:py:func:`~plantpredict.Prediction.get_nodal_data`.


Clone a prediction.
-------------------

Instantiate the prediction you wish to clone using the :py:class:`~plantpredict.Prediction` class, specifying its ID and project ID
(visible in the URL of that prediction in a web browser '.../projects/{project_id}/prediction/{id}/').

.. code-block:: python

    project_id = 7178   # CHANGE TO YOUR PROJECT ID
    prediction_id = 45110   # CHANGE TO YOUR PREDICTION ID
    prediction_to_clone = plantpredict.Prediction(id=prediction_id, project_id=project_id)


Clone the prediction, passing in a name for the new prediction. This will create a new prediction within the same
project that is an exact copy (other than the name) of the original prediction.

.. code-block:: python

    new_prediction_id = prediction_to_clone.clone(new_prediction_name='Cloned Prediction')

If you wish to change something about the new prediction, instantiate a new :py:class:`~plantpredict.Prediction` with
the returned prediction ID, change an attribute, and call the :py:func:`~plantpredict.Prediction.update` method.

.. code-block:: python

    new_prediction = plantpredict.Prediction(id=new_prediction_id, project_id=project_id)
    new_prediction.get()
    from plantpredict.enumerations.transposition_model_enum import *    # import at the top of the file
    new_prediction.transposition_model = HAY
    new_prediction.update()


Change the module in a power plant.
-----------------------------------

Instantiate the prediction of interest using the :py:class:`~plantpredict.Prediction` class, specifying its ID and
project ID (visible in the URL of that prediction in a web browser '.../projects/{project_id}/prediction/{id}/').

.. code-block:: python

    project_id = 7178   # CHANGE TO YOUR PROJECT ID
    prediction_id = 45110   # CHANGE TO YOUR PREDICTION ID
    prediction = plantpredict.Prediction(id=prediction_id, project_id=project_id)

Retrieve the prediction in order to extract its power plant ID. Then instantiate a :py:class:`~plantpredict.PowerPlant`
with that ID and retrieve all of its attributes.

.. code-block:: python

    prediction.get()
    power_plant = plantpredict.PowerPlant(prediction_id=prediction_id, project_id=project_id)
    power_plant.get()

Specify the ID of the module you want to replace the power plant's current module with (visible in the URL
of that module in a web browser '.../module/{id}/').

.. code-block:: python

    new_module_id = 1645

In order to change the module in Block 1 --> Array 1 --> Inverter A --> DC Field 1,
nullify the previous module's data structure, replace the module id, and update the power plant with the
the :py:func:`~plantpredict.Prediction.update` method.

.. code-block:: python

    power_plant.blocks[0]['arrays'][0]['inverters'][0]['dc_fields'][0]['module'] = None
    power_plant.blocks[0]['arrays'][0]['inverters'][0]['dc_fields'][0]['moduleId'] = new_module_id
    power_plant.update()


Change a prediction's weather file.
------------------------------------

Instantiate the prediction of interest using the :py:class:`~plantpredict.Prediction` class, specifying its ID and
project ID (visible in the URL of that prediction in a web browser '.../projects/{project_id}/prediction/{id}/').
Do the same for the project of interest using the :py:class:`~plantpredict.Project` class.

.. code-block:: python

    project_id = 7178   # CHANGE TO YOUR PROJECT ID
    prediction_id = 45110   # CHANGE TO YOUR PREDICTION ID
    prediction = plantpredict.Prediction(id=prediction_id, project_id=project_id)
    project = plantpredict.Project(id=project_id)

Retrieve the project and prediction's attributes.

.. code-block:: python

    prediction.get()
    project.get()

In this particular case, let's say you are looking for the most recent Meteonorm weather file within a 5-mile
radius of the project site. Search for all weather files within a 5 mile radius of the project's lat/long
coordinates.

.. code-block:: python

    weathers = plantpredict.Weather.search(project.latitude, project.longitude, search_radius=5)

Filter the results by only Meteonorm weather files.

.. code-block:: python

    from plantpredict.enumerations.weather_data_provider_enum import *  # should import at the top of your file
    weathers_meteo = [weather for weather in weathers if int(weather['data_provider']) == METEONORM]

If there is a weather file that meets the criteria, used the most recently created weather file's ID. If no weather file
meets the criteria, download a new Meteonorm weather file and use that ID.

.. code-block:: python

    if weathers_meteo:
        created_dates = [w['created_date'] for w in weathers_meteo]
        created_dates.sort()
        idx = [w['created_date'] for w in weathers_meteo].index(created_dates[-1])
        weather_id = weathers_meteo[idx]['id']
    else:
        weather = plantpredict.Weather()
        response = weather.download(project.latitude, project.longitude, provider=METEONORM)
        weather_id = weather.id

Instantiate weather using the weather ID and retrieve all of its attributes.

.. code-block:: python

    weather = plantpredict.Weather(id=weather_id)
    weather.get()

Ensure that the prediction start/end attributes match those of the weather file.

.. code-block:: python

    prediction.start_date = weather.start_date
    prediction.end_date = weather.end_date
    prediction.start = weather.start_date
    prediction.end = weather.end_date

Change the weather ID of the prediction and update the prediction.

.. code-block:: python

    prediction.weather_id = weather_id
    prediction.update()

Upload raw weather data.
-------------------------

Whether you are starting with an Excel file, CSV file, SQL query, or other data format, the first step is to get your
data into a JSON-like format. That format is represented in Python as a list of dictionaries, where each dictionary
represents a timestamp of weather data. Depending on the initial data format, you can utilize any of Python's
open-source data tools such as the `native csv library
<https://docs.python.org/2/library/csv.html>`_ or
`pandas <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html>`_. This tutorial skips that step
and loads pre-processed data from :download:`this JSON file <_static/weather_details.json>`.

.. code-block:: python

    import json
    with open('weather_details.json', 'rb') as json_file:
        weather_details = json.load(json_file)

Using the known latitude and longitude of the weather data location, call
:py:meth:`~plantpredict.Geo.get_location_info` query crucial location info necessary to populate the weather file's
metadata.

.. code-block:: python

    latitude = 35.0
    longitude = -119.0
    location_info = plantpredict.Geo.get_location_info(latitude=latitude, longitude=longitude)

Initialize the :py:class:`~plantpredict.Weather` entity and populate with the minimum fields required by
:py:meth:`~plantpredict.Weather.create`. Note that the weather details time series data loaded in the first step
is assigned to `weather.weather_details` at this point.

.. code-block:: python

    from plantpredict.enumerations import weather_data_provider_enum
    weather = plantpredict.Weather()
    weather.name = "Python SDK Test Weather"
    weather.latitude = 35.0
    weather.longitude = -119.0
    weather.country = location_info['country']
    weather.country_code = location_info['country_code']
    weather.data_provider = weather_data_provider_enum.METEONORM
    weather.weather_details = weather_details

Assign additional metadata fields.

.. code-block:: python

    weather.elevation = round(plantpredict.Geo.get_elevation(latitude=latitude, longitude=longitude)['elevation'], 2)
    weather.locality = location_info['locality']
    weather.region = location_info['region']
    weather.state_province = location_info['state_province']
    weather.state_province_code = location_info['state_province_code']
    weather.time_zone = plantpredict.Geo.get_time_zone(latitude=latitude, longitude=longitude)['time_zone']
    weather.status = library_status_enum.DRAFT_PRIVATE
    weather.data_type = weather_data_type_enum.MEASURED
    weather.p_level = weather_plevel_enum.P95
    weather.time_interval = 60  # minutes
    weather.global_horizontal_irradiance_sum = round(
        sum([w['global_horizontal_irradiance'] for w in weather_details])/1000, 2
    )
    weather.diffuse_horizontal_irradiance_sum = round(
        sum([w['diffuse_horizontal_irradiance'] for w in weather_details])/1000, 2
    )
    weather.direct_normal_irradiance_sum = round(
        sum([w['direct_normal_irradiance'] for w in weather_details])/1000, 2
    )
    weather.average_air_temperature = np.round(np.mean([w['temperature'] for w in weather_details]), 2)
    weather.average_relative_humidity = np.round(np.mean([w['relative_humidity'] for w in weather_details]), 2)
    weather.average_wind_speed = np.round(np.mean([w['windspeed'] for w in weather_details]), 2)
    weather.max_air_temperature = np.round(max([w['temperature'] for w in weather_details]), 2)

Create the weather file in PlantPredict with :py:meth:`~plantpredict.Weather.create`.

.. code-block:: python

    weather.create()


Generate a module file.
------------------------
