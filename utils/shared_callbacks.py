import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html

from . import Colors
from . import IdHolder as ID
from . import LayoutBuilder as LB
from . import app_data as data
from . import shared_graphs


@callback(
    Output(ID.index_type_callback_dispatcher, 'n_clicks'),
    [
        Input(ID.input_dropdown, 'value'),
        Input(ID.input_button, 'n_clicks'),
    ],
    [
        State(ID.input_area, 'value'),
    ],
    prevent_initial_call=True,
)
def dispatcher(dropdown_value, _, area_value):
    if dropdown_value:
        data.type = dropdown_value.lower()
        data.proba = [1, 1, 1, 1]
    else:
        import numpy as np

        # TODO: remove
        # data.type = 'entp'
        # data.proba = np.random.uniform(0.5, 1, 4)
        data.type, data.proba = data.model.predict(area_value)
    return _


@callback(
    [
        Output(ID.profile_img, 'style'),
        Output(ID.profile_username, 'style'),
    ],
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    State(ID.input_switch, 'value'),
    prevent_initial_call=True,
)
def update_profile_container(_, switch_value):
    return [{'display': 'block'}, {'display': 'block'}] if switch_value else [{'display': 'none'}, {'display': 'none'}]


@callback(
    Output(ID.personality_graph, 'figure'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment back
)
def update_personality_graph(_):
    return shared_graphs.plot_personality_graph()


@callback(
    Output(ID.prediction_container, 'style'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment back
)
def update_prediction_container(_):
    return {'display': 'grid'}


@callback(
    Output(ID.famous_people_container, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: uncomment
)
def update_famous_people_container(_):
    return [
        html.H4('Famous People:'),
        html.Div(
            children=[
                LB.card(
                    person.name,
                    person.url,
                    person.image_url,
                )
                for person in data.type.famous_persons
            ],
        ),
    ]


@callback(
    Output(ID.type_description, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment
)
def update_type_description(_):
    return data.type.description


@callback(
    Output(ID.strengths_container, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment
)
def update_strengths_container(_):
    return [
        html.H4('Strengths:', style={'color': Colors.green}),
        html.Div(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        children=[
                            html.B(strength.name),
                            html.P(strength.description),
                        ],
                    ),
                )
                for strength in data.type.strengths
            ],
        ),
    ]


@callback(
    Output(ID.weaknesses_container, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment
)
def update_weaknesses_container(_):
    return [
        html.H4('Weaknesses:', style={'color': Colors.red}),
        html.Div(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        children=[
                            html.B(weakness.name),
                            html.P(weakness.description),
                        ],
                    ),
                )
                for weakness in data.type.weaknesses
            ],
        ),
    ]


@callback(
    Output(ID.careers_container, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment
)
def update_careers_container(_):
    return [
        html.H4('Careers:'),
        dbc.Card(
            dbc.CardBody(
                children=[html.Div(career) for career in data.type.careers],
            ),
        ),
    ]


@callback(
    Output(ID.ideal_partners_container, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment
)
def update_ideal_partners_container(_):
    return [
        html.H4('Ideal Partners:'),
        html.Div(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        children=[
                            html.B(
                                partner.name,
                                style={
                                    'color': Colors.personality(partner.name.upper()),
                                    'display': 'inline-block',
                                    'margin-bottom': '1rem',
                                },
                            ),
                            html.P(partner.description),
                        ],
                    ),
                )
                for partner in data.type.ideal_partners
            ],
        ),
    ]


@callback(
    Output(ID.interests_container, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment
)
def update_interests_container(_):
    return [
        html.H4('Hobbies & Interests:'),
        dbc.Card(
            dbc.CardBody(
                children=[html.Div(interest) for interest in data.type.interests],
            ),
        ),
    ]


@callback(
    Output(ID.personality_type_container, 'children'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,  # TODO: comment
)
def update_personality_type_container(_):
    color = Colors.personality(data.pred_type.upper())
    return html.Table(
        children=[
            html.Tr(
                children=[
                    html.Td(
                        html.H1(
                            f'{data.pred_type[0].upper()}',
                            style={
                                'color': f'{color}',
                                'font-weight': 'bold',
                            },
                        ),
                    ),
                    html.Td(
                        html.H1(
                            f'{data.pred_type[1].upper()}',
                            style={
                                'color': f'{color}',
                                'font-weight': 'bold',
                            },
                        ),
                    ),
                    html.Td(
                        html.H1(
                            f'{data.pred_type[2].upper()}',
                            style={
                                'color': f'{color}',
                                'font-weight': 'bold',
                            },
                        ),
                    ),
                    html.Td(
                        html.H1(
                            f'{data.pred_type[3].upper()}',
                            style={
                                'color': f'{color}',
                                'font-weight': 'bold',
                            },
                        ),
                    ),
                ],
            ),
            html.Tr(
                children=[
                    html.Td(html.H6(f'{data.proba[0]*100:.2f}%')),
                    html.Td(html.H6(f'{data.proba[1]*100:.2f}%')),
                    html.Td(html.H6(f'{data.proba[2]*100:.2f}%')),
                    html.Td(html.H6(f'{data.proba[3]*100:.2f}%')),
                ],
            ),
        ],
        style={
            'width': '20rem',
            'text-align': 'center',
            'margin': '0 auto',
        },
    )


@callback(
    Output(ID.input_show_tokens_button, 'style'),
    Input(ID.index_type_callback_dispatcher, 'n_clicks'),
    prevent_initial_call=True,
)
def update_show_tokens_button(_):
    return {'display': 'block'}
