from dash import Input, Output, callback, html, no_update

from utils import Colors, data
from utils.IdHolder import IdHolder as ID


@callback(
    [
        Output(ID.input_profile_wrapper, 'style'),
        Output(ID.input_area, 'style'),
        Output(ID.input_button, 'style'),
        Output(ID.input_switch, 'label'),
    ],
    Input(ID.input_switch, 'value'),
)
def update_input_switch(value):
    return (
        [{}, {'display': 'none'}, {}, 'Twitter Username']
        if value
        else [{'display': 'none'}, {}, {'grid-row': '3'}, 'Raw Text']
    )


def token(text):
    return html.Code(
        text,
        style={
            'white-space': 'pre-wrap',
            'word-break': 'normal',
            'color': Colors.white,
            'background-color': Colors.black,
            'padding': '.125rem .25rem',
            'border-radius': '.25rem',
            'font-family': 'monospace',
            'font-size': '1rem',
            'margin': '0.125rem .125rem',
            'display': 'inline-block',
        },
    )


@callback(
    [
        Output(ID.input_tokens_toast, 'is_open'),
        Output(ID.input_tokens_toast, 'children'),
    ],
    Input(ID.input_show_tokens_button, 'n_clicks'),
    prevent_initial_call=True,
)
def open_toast(n):
    if n == 0:
        return no_update
    return [
        True,
        html.Div(
            children=[token(t) for t in data.model.tokens],
        ),
        # {'display': 'inline-block'}
    ]
