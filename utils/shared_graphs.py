import plotly.graph_objects as go

from . import Colors
from . import app_data as data


def plot_personality_graph():
    fig = go.Figure()

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=25, b=25),
        paper_bgcolor=Colors.transparent,
        polar=dict(
            bgcolor=Colors.transparent,
            radialaxis=dict(
                side='counterclockwise',
                showline=False,
                linewidth=1,
                gridcolor=Colors.grey,
                gridwidth=1,
                showticklabels=False,
                range=[-5, 100],
                dtick=25,
            ),
            sector=[-180, 180],
            angularaxis=dict(
                direction='clockwise',
                rotation=90,
                showline=True,
                linecolor=Colors.grey,
            ),
            gridshape='linear',
        ),
        font=dict(
            family='Inter',
            color=Colors.black,
            size=16,
        ),
    )

    fig.add_trace(
        go.Scatterpolar(
            r=[
                (data.proba[0] if data.type.name[0] == 'i' else 1 - data.proba[0]) * 100,
                (data.proba[1] if data.type.name[1] == 'n' else 1 - data.proba[1]) * 100,
                (data.proba[2] if data.type.name[2] == 't' else 1 - data.proba[2]) * 100,
                (data.proba[3] if data.type.name[3] == 'j' else 1 - data.proba[3]) * 100,
                (data.proba[0] if data.type.name[0] == 'e' else 1 - data.proba[0]) * 100,
                (data.proba[1] if data.type.name[1] == 's' else 1 - data.proba[1]) * 100,
                (data.proba[2] if data.type.name[2] == 'f' else 1 - data.proba[2]) * 100,
                (data.proba[3] if data.type.name[3] == 'p' else 1 - data.proba[3]) * 100,
                (data.proba[0] if data.type.name[0] == 'i' else 1 - data.proba[0]) * 100,
            ],
            theta=[
                '<b>Introversion</b>',
                '<b>Thinking</b>',
                '<b>Intuition</b>',
                '<b>Judging</b>',
                '<b>Extroversion</b>',
                '<b>Feeling</b>',
                '<b>Sensing</b>',
                '<b>Perceiving</b>',
                '<b>Introversion</b>',
            ],
            fill='toself',
            fillcolor=Colors.personality(data.pred_type.upper()).opacity(0.2),
            mode='markers+lines',
            marker=dict(
                size=0,
                color=Colors.personality(data.pred_type.upper()),
            ),
            # text=[100, 40, 50, 50, 75, 25, 60, 40, 100],
            name='Identificators',
            hovertemplate='%{theta} %{r:.2f}%',
        ),
    )

    return fig
