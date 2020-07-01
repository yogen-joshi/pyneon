# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from pydoc import classname


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)





app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Hello Dash', className = 'nine columns'),
        
          html.Img(
                    src=app.get_asset_url('kapsarc.PNG'),
                    className='three columns',
                    style={
                        'height': '8%',
                        'width': '10%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                       'margin-right': 30
                    },
                ),
    
        html.Div(children='''
            Dash: A web application framework for Python.
        ''', className='nine columns')
    ], className="row"),
    html.Div([
        html.Div([
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'xaxis': dict(
                            title= 'x Axis',
                            titlefont= dict(
                            family= 'Courier New, monospace',
                            size= 20,
                            color= '#7f7f7f'     
                            )),
                        'yaxis': dict(
                            title= 'y Axis',
                            titlefont= dict(
                            family= 'Helvetica, monospace',
                            size= 18,
                            color= '#7f7f7f'     
                            ))
                    }
                }
            )        
        ], className = "six columns" ),
        html.Div([
            dcc.Graph(
                id='example-graph-2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'xaxis': dict(
                            title= 'x Axis',
                            titlefont= dict(
                            family= 'Courier New, monospace',
                            size= 20,
                            color= '#7f7f7f'     
                            )),
                        'yaxis': dict(
                            title= 'y Axis',
                            titlefont= dict(
                            family= 'Helvetica, monospace',
                            size= 18,
                            color= '#7f7f7f'     
                            ))
                    }
                }
            )
        ], className = "six columns" )
    ], className = "row")
], className= "ten columns offset-by-one")
if __name__ == '__main__':
    app.run_server(debug=True)