# from dash import callback, Input, Output
# from utils import IdHolder as ID
# from utils import app_data as data

# @callback(
#     Output(ID.prediction_container, 'style'),
#     Input(ID.input_dropdown, 'value'),
#     prevent_initial_call=True,
# )
# def update_prediction_container(value):
#     data.type = value
#     return {'display': 'grid'}
