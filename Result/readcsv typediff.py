#import all the required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np
import pandas as pd


#read all the data
df = pd.read_csv('finalBatsRuns.csv')
df1 = pd.read_csv('finalBatsSR.csv')
df2 = pd.read_csv('finalBowlwkt.csv')
df3 = pd.read_csv('finalBowlEco.csv')
df4 = pd.read_csv('finalARSr.csv')
df5 = pd.read_csv('finalARwkt.csv')



# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H5('Overview'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ])
    )
])



app.layout = html.Div([

    html.H1('ALL STARS IPL TEAM ANALYSIS'),
    html.P('Here we are plotting all the possible cases taken for selecting players of ALL STARS team'),
    
    #batting-runs
    dcc.Graph(
        id='scatter-chartdf',
        figure = {
            'data': [
                    
                     {'x':df.Player, 'y':df.RohitSharma , 'type':'line', 'name': 'RohitSharma'},
                     {'x':df.Player, 'y':df.ShaneWatson , 'type':'line', 'name': 'ShaneWatson'},
                     {'x':df.Player, 'y':df.ViratKohli , 'type':'line', 'name': 'ViratKohli'},
                     {'x':df.Player, 'y':df.ABdeVilliers , 'type':'line', 'name': 'ABdeVilliers'},
                     {'x':df.Player, 'y':df.SureshRaina , 'type':'line', 'name': 'SureshRaina'},
                     {'x':df.Player, 'y':df.MSDhoni , 'type':'line', 'name': 'MSDhoni'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise Runs Scored by Batsmen',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'Runs scored in Seasons'}
            )
         }
        )
    ,

    #batting-srtike rate
    dcc.Graph(
        id='scatter-chartdf1',
        figure = {
            'data': [
                     
                     {'x':df1.Player, 'y':df1.RohitSharma , 'type':'line', 'name': 'RohitSharma'},
                     {'x':df1.Player, 'y':df1.ShaneWatson , 'type':'line', 'name': 'ShaneWatson'},
                     {'x':df1.Player, 'y':df1.ViratKohli , 'type':'line', 'name': 'ViratKohli'},
                     {'x':df1.Player, 'y':df1.ABdeVilliers , 'type':'line', 'name': 'ABdeVilliers'},
                     {'x':df1.Player, 'y':df1.SureshRaina , 'type':'line', 'name': 'SureshRaina'},
                     {'x':df1.Player, 'y':df1.MSDhoni , 'type':'line', 'name': 'MSDhoni'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise Strike Rate Scored by Batsmen',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'Strike Rate of all Seasons'}
            )
         }
        )
    ,

    
    #bowling-wickets
    dcc.Graph(
        id='scatter-chartdf2',
        figure = {
            'data': [
                     
                     {'x':df2.Player, 'y':df2.SunilNarine , 'type':'line', 'name': 'SunilNarine'},
                     {'x':df2.Player, 'y':df2.BhuvneshwarKumar , 'type':'line', 'name': 'BhuvneshwarKumar'},
                     {'x':df2.Player, 'y':df2.JaspritBumrah , 'type':'line', 'name': 'JaspritBumrah'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise wickets taken by bowlers',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'No. of wickets taken'}
            )
         }
        )
    ,

    #bowling-Economy
    dcc.Graph(
        id='scatter-chartdf3',
        figure = {
            'data': [
                    
                     {'x':df3.Player, 'y':df3.SunilNarine , 'type':'line', 'name': 'SunilNarine'},
                     {'x':df3.Player, 'y':df3.BhuvneshwarKumar , 'type':'line', 'name': 'BhuvneshwarKumar'},
                     {'x':df3.Player, 'y':df3.JaspritBumrah , 'type':'line', 'name': 'JaspritBumrah'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise Economy of bowlers',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'Economy'}
            )
         }
        )

    ,

    #allRounder-Srtike rate
    dcc.Graph(
        id='scatter-chartdf4',
        figure = {
            'data': [
                     {'x':df4.Player, 'y':df4.AndreRussell, 'type':'bar', 'name': 'AndreRussell'},
                     {'x':df4.Player, 'y':df4.HardikPandya, 'type':'bar', 'name': 'HardikPandya'},
                     {'x':df4.Player, 'y':df4.AndreRussell, 'type':'line', 'name': 'AndreRussell'},
                     {'x':df4.Player, 'y':df4.HardikPandya, 'type':'line', 'name': 'HardikPandya'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise Strike Rate of all-rounder Players',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'Strike Rate of all Seasons'}
            )
         }
        )

    ,


    #allRounder-wickets
    dcc.Graph(
        id='scatter-chartdf5',
        figure = {
            'data': [
                     {'x':df5.Player, 'y':df5.AndreRussell, 'type':'bar', 'name': 'AndreRussell'},
                     {'x':df5.Player, 'y':df5.HardikPandya, 'type':'bar', 'name': 'HardikPandya'},
                     {'x':df5.Player, 'y':df5.AndreRussell, 'type':'line', 'name': 'AndreRussell'},
                     {'x':df5.Player, 'y':df5.HardikPandya, 'type':'line', 'name': 'HardikPandya'},
                 ],

        'layout': go.Layout(
            title = 'Season-wise wickets taken by all-rounder Players',
            xaxis = {'title':'IPL year'},
            yaxis = {'title':'No. of wickets taken'}
            )
         }
        )

    
    ])


if __name__ == '__main__':
    app.run_server(debug=True)


