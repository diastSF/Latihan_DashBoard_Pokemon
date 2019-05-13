import os

#________IMPORT LIBRARY________#
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

#________IMPORT LAYOUT________#
from src.components.datapokemon import dfPokemon, dfPokemonTable
from src.components.tab1.view import renderIsiTab1
from src.components.tab2.view import renderIsiTab2
from src.components.tab3.view import renderIsiTab3
from src.components.tab4.view import renderIsiTab4
from src.components.tab5.view import renderIsiTab5
from src.components.tab6.view import renderIsiTab6
from src.components.tab7.view import renderIsiTab7

#________IMPORT CALLBACK FUNCTION________#
from src.components.tab1.callbacks import callbacksortingtable, callbackfiltertable
from src.components.tab2.callbacks import callbackupdatecatgraph
from src.components.tab3.callbacks import callbackupdatescattergraph
from src.components.tab4.callbacks import callbackupdatepiegraph
from src.components.tab5.callbacks import callbackupdatehistogram
from src.components.tab6.callbacks import callbackpredict
from src.components.tab7.callbacks import callbacksortingtablehistory, callbackfiltertablehistory

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

server = app.server

app.title = 'Dashboard Pokemon'

app.layout = html.Div([
    html.H1('Dashboard Pokemon'),
    html.H3('''
        Created By : Diast S. F.
    '''
    ),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Data Pokemon', value='tab-1', children=renderIsiTab1()),
        dcc.Tab(label='Categorical Plots', value='tab-2', children=renderIsiTab2()),
        dcc.Tab(label='Scatter Plot', value='tab-3', children=renderIsiTab3()),
        dcc.Tab(label='Pie Chart', value='tab-4', children=renderIsiTab4()),
        dcc.Tab(label='Histogram', value='tab-5', children=renderIsiTab5()),
        dcc.Tab(label='Test Predict', value='tab-6', children=renderIsiTab6()),
        dcc.Tab(label='History Predictions', value='tab-7', children=renderIsiTab7())
    ],style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    }) 
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})

#________________CALLBACK TAB 1__________________

@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])

def update_sort_paging_table(pagination_settings, sorting_settings):
    return callbacksortingtable(pagination_settings, sorting_settings)

@app.callback(
    Output(component_id='tablediv', component_property='children'),
    [Input('buttonsearch', 'n_clicks'),
    Input('filterrowstable', 'value')],
    [State('filternametable', 'value'),
    State('filtergenerationtable', 'value'),
    State('filtercategorytable', 'value'),
    State('filtertotaltable', 'value')]
)
def update_table(n_clicks,maxrows, name,generation,category,total):
    return callbackfiltertable(n_clicks,maxrows, name,generation,category,total)

#________________CALLBACK TAB 2__________________

@app.callback(
    Output(component_id='categorygraph', component_property='figure'),
    [Input(component_id='jenisplotcategory', component_property='value'),
    Input(component_id='xplotcategory', component_property='value'),
    Input(component_id='yplotcategory', component_property='value'),
    Input(component_id='statsplotcategory', component_property='value')]
)
def update_category_graph(jenisplot,x,y,stats):
    return callbackupdatecatgraph(jenisplot,x,y,stats)

@app.callback(
    Output(component_id='statsplotcategory', component_property='disabled'),
    [Input(component_id='jenisplotcategory', component_property='value')]
)
def update_disabled_stats(jenisplot):
    if(jenisplot == 'Bar') :
        return False
    return True

#________________CALLBACK TAB 3__________________

@app.callback(
    Output(component_id='scattergraph', component_property='figure'),
    [Input(component_id='hueplotscatter', component_property='value'),
    Input(component_id='xplotscatter', component_property='value'),
    Input(component_id='yplotscatter', component_property='value')]
)
def update_scatter_plot(hue,x,y):
    return callbackupdatescattergraph(hue,x,y)

#________________CALLBACK TAB 4__________________

@app.callback(
    Output(component_id='piegraph', component_property='figure'),
    [Input(component_id='groupplotpie', component_property='value')]
)
def update_pie_plot(group):
    return callbackupdatepiegraph(group)

#________________CALLBACK TAB 5__________________

@app.callback(
    Output(component_id='histgraph', component_property='figure'),
    [Input(component_id='xplothist', component_property='value'),
    Input(component_id='hueplothist', component_property='value'),
    Input(component_id='stdplothist', component_property='value')]
)
def update_hist_plot(x, hue, std):
    return callbackupdatehistogram(x, hue, std)

#_________________CALLBACK TAB 6__________________

@app.callback(
    Output(component_id='outputpredict', component_property='children'),
    [Input('predictsearch', 'n_clicks')],
    [State('predictname', 'value'),
    State('predicttype1', 'value'),
    State('predicttype2', 'value'),
    State('predictgeneration', 'value'),
    State('predicttotal', 'value'),
    State('predicthp', 'value'),
    State('predictattack', 'value'),
    State('predictdefense', 'value'),
    State('predictspatk', 'value'),
    State('predictspdef', 'value'),
    State('predictspeed', 'value')]
)
def update_predict(n_clicks,name,type1,type2,generation,total,hp,attack,defense,spatk,spdef,speed):
    return callbackpredict(n_clicks,name,type1,type2,generation,total,hp,attack,defense,spatk,spdef,speed)

#___________________CALLBACK TAB 7__________________

@app.callback(
    Output('table-history-prediction', "data"),
    [Input('table-history-prediction', "pagination_settings"),
     Input('table-history-prediction', "sorting_settings")])

def update_sort_history_table(pagination_settings, sorting_settings):
    return callbacksortingtablehistory(pagination_settings, sorting_settings)

@app.callback(
    Output(component_id='tablehistorydiv', component_property='children'),
    [Input('filtercreatedbyhistory', 'value'),
    Input('filterrowhistory', 'value')]
)
def update_table_history(createdby,maxrows):
    return callbackfiltertablehistory(createdby,maxrows)

if __name__ == '__main__':
    app.run_server(debug=True)