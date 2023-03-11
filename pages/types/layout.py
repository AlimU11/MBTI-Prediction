import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import app_data as data
from utils.IdHolder import IdHolder as ID
from utils.LayoutBuilder import LayoutBuilder as LB

layout = LB.layout(
    page_class='index',
    title=html.H1('MBTI Types Info'),
    callback_dispatcher_id=ID.index_type_callback_dispatcher,
    children=[
        html.Div(
            children=[
                dbc.Label(html.H5('Choose a type:')),
                dcc.Dropdown(
                    id=ID.input_dropdown,
                    options=list(map(str.upper, data.types)),
                    clearable=False,
                ),
            ],
        ),
        LB.shared_layout(is_generic=True),
    ],
)
