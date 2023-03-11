# TODO add exception handler
# TODO fill text area with Kira Yoshikage's text

import dash_bootstrap_components as dbc
from dash import dcc, html

from utils.Config import config
from utils.IdHolder import IdHolder as ID
from utils.LayoutBuilder import LayoutBuilder as LB

layout = LB.layout(
    page_class='index',
    title=html.H1('MBTI Prediction'),
    callback_dispatcher_id=ID.index_type_callback_dispatcher,
    children=[
        html.Div(
            children=[
                dbc.Switch(
                    label='Raw Text',
                    value=False,
                    id=ID.input_switch,
                ),
                dbc.Button(
                    'Show Tokens',
                    id=ID.input_show_tokens_button,
                ),
                dbc.Toast(
                    id=ID.input_tokens_toast,
                    header='List of tokens',
                    icon='primary',
                    dismissable=True,
                    is_open=False,
                ),
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText('@'),
                        dbc.Input(
                            id=ID.input_profile,
                        ),
                    ],
                    id=ID.input_profile_wrapper,
                    style={'display': 'none'},
                ),
                dbc.Textarea(
                    id=ID.input_area,
                    style={'height': '100px'},
                    size='lg',
                ),
                dbc.Button(
                    'Predict',
                    id=ID.input_button,
                ),
            ],
            id=ID.input_container,
        ),
        LB.shared_layout(is_generic=False),
    ],
)
