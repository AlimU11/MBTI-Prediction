from __future__ import annotations

from typing import Sequence

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.development.base_component import Component

from .Config import config
from .IdHolder import IdHolder as ID


class LayoutBuilder:
    @staticmethod
    def layout(
        page_class: str,
        title: str | Component | None,
        children: str | Sequence[Component],
        callback_dispatcher_id: str = ID.UNDEFINED,
    ) -> Component:
        """Layout template for all pages"""
        return html.Div(
            children=[
                LayoutBuilder.sidebar(page_class),
                html.Div(
                    children=[
                        dbc.Button(
                            id=callback_dispatcher_id,
                            style={'display': 'none'},
                        ),
                        title,
                        html.Div(
                            children=children,
                            className=f'main-grid main-grid--{page_class}',
                        ),
                    ],
                    className=f'main-container main-container--{page_class}',
                ),
            ],
            className='page-container',
        )

    @staticmethod
    def sidebar(page_name: str) -> Component:
        """Sidebar template for all page pages"""
        return html.Div(
            children=[
                *[
                    html.A(
                        children=html.I(
                            className=f'{"fa-solid"} fa-{page.icon}',
                        ),
                        href=f'{page.link}',
                        id=getattr(
                            ID,
                            page.name.lower().replace(' ', '_'),
                        ),
                    )
                    for page in config.pages
                ],
                *[
                    dbc.Tooltip(
                        page.name,
                        target=getattr(
                            ID,
                            page.name.lower().replace(' ', '_'),
                        ),
                    )
                    for page in config.pages
                ],
            ],
            className=f'sidebar sidebar--{page_name}',
        )

    @staticmethod
    def kpi_card(
        title: str | Component,
        title_size: int | str,
        description: str | Component,
        title_id: str,
        description_id: str,
    ) -> Component:
        """KPI card template"""
        return dbc.Card(
            dbc.CardBody(
                [
                    dbc.Spinner(
                        [
                            getattr(html, f'H{title_size}')(
                                title,
                                className='card-title',
                                id=title_id,
                            ),
                            html.P(
                                description,
                                className='card-text',
                                id=description_id,
                            ),
                        ],
                    ),
                ],
            ),
        )

    @staticmethod
    def graph_card(
        graph_id: str,
        title: str | Component = '',
        title_size: int | str = 1,
        title_id: str = ID.UNDEFINED,
        config: dict = {'displayModeBar': False},
        controls=None,
    ) -> Component:
        """Graph card template"""
        return dbc.Card(
            dbc.CardBody(
                [
                    getattr(html, f'H{title_size}')(
                        title,
                        className='card-title',
                        id=title_id,
                        style={
                            'display': 'none',
                        }
                        if title_id == ID.UNDEFINED
                        else {},
                    ),
                    controls,
                    dbc.Spinner(
                        [
                            dcc.Graph(id=graph_id, config=config),
                        ],
                    ),
                ],
            ),
        )

    @staticmethod
    def card(title: str, url: str, background_url: str) -> Component:
        """Card template"""
        return dbc.Card(
            dbc.CardBody(
                [
                    html.A(
                        html.Div(
                            [
                                html.Div(
                                    style={
                                        'background-image': f'url({background_url})',
                                    },
                                    className='card-image',
                                ),
                            ],
                            className='card-image-container',
                        ),
                        href=f'''{url}''',
                        target='_blank',
                        className='card-title',
                    ),
                    html.Div(
                        [
                            html.H6(
                                html.A(
                                    f'''{title}''',
                                    href=f'''{url}''',
                                    target='_blank',
                                    className='card-title',
                                ),
                            ),
                        ],
                        className='mt-auto card-text-container',
                    ),
                ],
                className='flex-column d-flex content-card',
            ),
        )

    @staticmethod
    def shared_layout(is_generic: bool) -> Component:
        """Layout shared between index and types pages. Returns MBTI type description."""
        return dbc.Spinner(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    id=ID.profile_img,  # TODO: change to profile pic
                                )
                                if not is_generic
                                else html.Div(id=ID.profile_img),
                                html.H3('@Example', id=ID.profile_username)
                                if not is_generic
                                else html.Div(id=ID.profile_username),  # TODO: change to username
                                html.H2('Personality Type:'),
                                html.Div(id=ID.personality_type_container),
                                dcc.Dropdown(id=ID.input_dropdown, style={'display': 'none'})
                                if not is_generic
                                else html.Div(),
                                html.Div()
                                if not is_generic
                                else html.Div(id=ID.input_button, style={'display': 'none'}),
                                html.Div()
                                if not is_generic
                                else dbc.Switch(id=ID.input_switch, style={'display': 'none'}),
                                html.Div()
                                if not is_generic
                                else html.Div(id=ID.input_profile_wrapper, style={'display': 'none'}),
                                html.Div()
                                if not is_generic
                                else html.Div(dbc.Textarea(id=ID.input_area), style={'display': 'none'}),
                            ],
                            id=ID.profile_container,
                        ),
                        dbc.Alert(
                            'All following information was generated by ChatGPT. No credability guaranteed.',
                            color='warning',
                        ),
                        dbc.Card(
                            children=[
                                html.H4(
                                    'Type description:',
                                    style={
                                        'margin-bottom': '1rem',
                                    },
                                ),
                                html.P(
                                    style={
                                        'white-space': 'pre-wrap',
                                        'font-size': '1.2rem',
                                        'text-align': 'justify',
                                    },
                                    id=ID.type_description,
                                ),
                            ],
                        ),
                        LayoutBuilder.graph_card(
                            graph_id=ID.personality_graph,
                        ),
                        dbc.Card(id=ID.strengths_container),
                        dbc.Card(id=ID.weaknesses_container),
                        html.Div(
                            children=[
                                html.Div(id=ID.careers_container),
                                html.Div(id=ID.interests_container),
                            ],
                        ),
                        dbc.Card(id=ID.ideal_partners_container),
                        html.Div(
                            id=ID.famous_people_container,
                        ),
                    ],
                    id=ID.prediction_container,
                    style={'display': 'none'},
                ),
            ],
        )
