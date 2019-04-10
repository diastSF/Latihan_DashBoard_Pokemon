import dash_core_components as dcc
import dash_html_components as html

from src.components.datapokemon import dfPokemon

def renderIsiTab5():
    return [
            html.Div([
                html.Div([
                    html.P('X : '),
                    dcc.Dropdown(
                        id='xplothist',
                        options=[{'label': i, 'value': i} for i in dfPokemon.columns[4:11]],
                        value='Total'
                    )
                ], className='col-3'),
                html.Div([
                    html.P('Hue : '),
                    dcc.Dropdown(
                        id='hueplothist',
                        options=[{'label': i, 'value': i} for i in ['All','Generation','Legendary']],
                        value='All'
                    )
                ], className='col-3'),
                html.Div([
                    html.P('Std : '),
                    dcc.Dropdown(
                        id='stdplothist',
                        options=[{'label': '{} Standart Deviation'.format(i), 'value': i} for i in ['1','2','3']],
                        value='2'
                    )
                ], className='col-3')
            ], className='row'),
            html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
            dcc.Graph(
                id='histgraph'
            )
        ]