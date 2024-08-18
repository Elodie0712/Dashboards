#Importing Dependencies
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

import dash
from dash import dcc, html
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'notebook'


# Define the path to the CSV file (use absolute path)
Data2 = Path("RESOURCES\Data Team Performance Task_Raw Dataset (1).xlsx - 2018-19 STAAR GRADE 3 ELA (2).csv")

# Read the CSV file into a pandas DataFrame
Data_df2 = pd.read_csv(Data2)

header_mapping = {
    'CDB03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate',
    'CDA03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate',
    'CDI03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate',
    'CD303ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate',
    'CDR03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, At Risk, STAAR Reading/ELA Rate',
    'CNC03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Continuous Enrollee, STAAR Reading/ELA Rate',
    'CD003ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Current-&-Monitored-Y1toY4-EL, STAAR Reading/ELA Rate',
    'CDL03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate',
    'CDE03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Econ Disadv, STAAR Reading/ELA Rate',
    'CDF03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate',
    'CNS03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Former Special Ed, STAAR Reading/ELA Rate',
    'CDH03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate',
    'CDM03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate',
    'CNM03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Mobile, STAAR Reading/ELA Rate',
    'CD403ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate',
    'CDS03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate',
    'CD203ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate',
    'CDW03ARE1S18R': 'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate',
    'CDB03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate',
    'CDA03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate',
    'CDI03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate',
    'CD303ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate',
    'CDR03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, At Risk, STAAR Reading/ELA Rate',
    'CNC03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Continuous Enrollee, STAAR Reading/ELA Rate',
    'CD003ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Current-&-Monitored-Y1toY4-EL, STAAR Reading/ELA Rate',
    'CDL03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate',
    'CDE03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Econ Disadv, STAAR Reading/ELA Rate',
    'CDF03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate',
    'CNS03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Former Special Ed, STAAR Reading/ELA Rate',
    'CDH03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate',
    'CDM03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate',
    'CNM03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Mobile, STAAR Reading/ELA Rate',
    'CD403ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate',
    'CDS03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate',
    'CD203ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate',
    'CDW03ARE1318R': 'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate',
    'CDB03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate',
    'CDA03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate',
    'CDI03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate',
    'CD303ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate',
    'CDR03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, At Risk, STAAR Reading/ELA Rate',
    'CNC03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Continuous Enrollee, STAAR Reading/ELA Rate',
    'CD003ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Current-&-Monitored-Y1toY4-EL, STAAR Reading/ELA Rate',
    'CDL03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate',
    'CDE03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Econ Disadv, STAAR Reading/ELA Rate',
    'CDF03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate',
    'CNS03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Former Special Ed, STAAR Reading/ELA Rate',
    'CDH03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate',
    'CDM03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate',
    'CNM03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Mobile, STAAR Reading/ELA Rate',
    'CD403ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate',
    'CDS03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate',
    'CD203ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate',
    'CDW03ARE1218R': 'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate',
    'CDB03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate',
    'CDA03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate',
    'CDI03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate',
    'CD303ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate',
    'CDR03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, At Risk, STAAR Reading/ELA Rate',
    'CNC03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Continuous Enrollee, STAAR Reading/ELA Rate',
    'CD003ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Current-&-Monitored-Y1toY4-EL, STAAR Reading/ELA Rate',
    'CDL03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate',
    'CDE03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Econ Disadv, STAAR Reading/ELA Rate',
    'CDF03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate',
    'CNS03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Former Special Ed, STAAR Reading/ELA Rate',
    'CDH03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate',
    'CDM03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate',
    'CNM03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Mobile, STAAR Reading/ELA Rate',
    'CD403ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate',
    'CDS03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate',
    'CD203ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate',
    'CDW03ARE1S19R': 'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate',
    'CDB03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate',
    'CDA03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate',
    'CDI03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate',
    'CD303ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate',
    'CDR03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, At Risk, STAAR Reading/ELA Rate',
    'CNC03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Continuous Enrollee, STAAR Reading/ELA Rate',
    'CD003ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Current-&-Monitored-Y1toY4-EL, STAAR Reading/ELA Rate',
    'CDL03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate',
    'CDE03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Econ Disadv, STAAR Reading/ELA Rate',
    'CDF03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate',
    'CNS03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Former Special Ed, STAAR Reading/ELA Rate',
    'CDH03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate',
    'CDM03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate',
    'CNM03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Mobile, STAAR Reading/ELA Rate',
    'CD403ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate',
    'CDS03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate',
    'CD203ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate',
    'CDW03ARE1319R': 'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate',
    'CDB03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate',
    'CDA03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate',
    'CDI03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate',
    'CD303ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate',
    'CDR03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, At Risk, STAAR Reading/ELA Rate',
    'CNC03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Continuous Enrollee, STAAR Reading/ELA Rate',
    'CD003ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Current-&-Monitored-Y1toY4-EL, STAAR Reading/ELA Rate',
    'CDL03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate',
    'CDE03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Econ Disadv, STAAR Reading/ELA Rate',
    'CDF03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate',
    'CNS03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Former Special Ed, STAAR Reading/ELA Rate',
    'CDH03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate',
    'CDM03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate',
    'CNM03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Mobile, STAAR Reading/ELA Rate',
    'CD403ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate',
    'CDS03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate',
    'CD203ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate',
    'CDW03ARE1219R': 'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate'}
# Rename columns using the header mapping dictionary
Data_df2 = Data_df2.rename(columns=header_mapping)
#turning -1 and . into NA
Data_df2.replace(['-1', '.'], pd.NA, inplace=True)

# Column name mapping
col_mapping2 = {'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate': 'App_El_18',
                'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Econ Disadv, STAAR Reading/ELA Rate': 'Ma_El_18',
                'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate':'Me_El_18',
                'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate':'App_El_19',
                'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate':'Me_El_19',
                'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, EL, STAAR Reading/ELA Rate':'Ma_El_19', 
                'Campus 2018 Domain 1A: Approaches Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate':'App_Sped_18',
                'Campus 2018 Domain 1A: Meets Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate':'Me_Sped_18',
                'Campus 2018 Domain 1A: Masters Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate':'Ma_Sped_18',
                'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate':'App_Sped_19',
                'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate':'Me_Sped_19',
                'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate':'Ma_Sped_19'}
                
                
            # Rename columns using the header mapping dictionary
Data_df2 = Data_df2.rename(columns=col_mapping2)    
                
for col in Data_df2.columns:
    if col != 'CAMPUS':
        Data_df2[col] = Data_df2[col].astype('Int64')

# Define the path to the CSV file (use absolute path)
Data3 = Path("Overview Data/Data Team Performance Task_Raw Dataset.xlsx - 2018-19 CAMPUS (2).csv")

# Read the CSV file into a pandas DataFrame
Data_df3 = pd.read_csv(Data3)
merge_df=pd.merge(Data_df3, Data_df2, on='CAMPUS')


# Assuming Data_df3 and Data_df2 are predefined
# mergedf
merge_df = pd.merge(Data_df3, Data_df2, on='CAMPUS')
merge_df.replace([-1, '.'], pd.NA, inplace=True)

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Updated column lists with new column names
el_app = ['App_El_18','App_El_19']
el_meets = ['Me_El_18', 'Me_El_19']
el_ma = ['Ma_El_18', 'Ma_El_19']
sped_app = ['App_Sped_18']
sped_me = ['Me_Sped_18','Me_Sped_19']
sped_ma = ['Ma_Sped_18','Ma_Sped_19']

# Front end layout
# Continuing layout definition
def layout3():
    return dbc.Container([
        html.H1("School District Dashboard"),
        dcc.Tabs([
            dcc.Tab(label='3rd Grade RLA Special Populations', children=[
                dbc.Container([
                    dbc.Row([
                        dbc.Col(dcc.Dropdown(
                            id="SD",
                            options=[{'label': 'All DISTRICTS', 'value': 'All'}] +
                                    [{'label': district, 'value': district} for district in merge_df['DISTNAME'].unique()],
                            style={'color': 'black'},
                            value='All'  # Default value
                        ), width=6),

                        dbc.Col(dcc.RadioItems(
                            id='SchoolType',
                            options=[
                                {'label': 'Elementary', 'value': 'E'},
                                {'label': 'Charter', 'value': 'B'},
                                {'label': 'All', 'value': 'All'}
                            ],
                            value='All'  # Default value
                        ), width=6),
                    ], className='mb-4'),
                    html.Br(),
                    html.Div([
                        html.H2("Emergent Bilinguals", style={'textAlign': 'center', 'fontStyle': 'italic', 'color': 'black'})
                    ], style={
                        'border': '2px solid black',
                        'borderRadius': '15px',
                        'padding': '10px',
                        'backgroundColor': '#f2f2f2',
                        'boxShadow': '0px 4px 8px rgba(0,0,0,0.1)',
                        'margin': '20px auto'
                    }),
                    html.Br(),

                    dbc.Row([
                        dbc.Col([
                            html.H3("Approaches", style={'textAlign': 'center', 'color': 'orange', 'fontWeight': 'bold'}),
                            dcc.Graph(id='FMAG', style={'width': '400px', 'height': '400px'}),
                            html.P(id='FMA', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Meets", style={'textAlign': 'center', 'color': 'green', 'fontWeight': 'bold'}),
                            dcc.Graph(id='FMMG', style={'width': '400px', 'height': '400px'}),
                            html.P(id='FMM', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Masters", style={'textAlign': 'center', 'color': 'purple', 'fontWeight': 'bold'}),
                            dcc.Graph(id='FMMAG', style={'width': '400px', 'height': '400px'}),
                            html.P(id='FMMA', style={'textAlign': 'center'})
                        ], width=4, className='mb-4', style={'paddingTop': '0', 'marginTop': '-9px'}),
                    ]),
                    html.Br(),
                    html.Div([
                        html.H2("SPED", style={'textAlign': 'center', 'fontStyle': 'italic', 'color': 'black'})
                    ], style={
                        'border': '2px solid black',
                        'borderRadius': '15px',
                        'padding': '10px',
                        'backgroundColor': '#f2f2f2',
                        'boxShadow': '0px 4px 8px rgba(0,0,0,0.1)',
                        'margin': '20px auto'
                    }),
                    html.Br(),

                    dbc.Row([
                        dbc.Col([
                            html.H3("Approaches", style={'textAlign': 'center', 'color': 'orange', 'fontWeight': 'bold'}),
                            dcc.Graph(id='SPED_App', style={'width': '400px', 'height': '400px'}),
                            html.P(id='SPED_App_Text', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Meets", style={'textAlign': 'center', 'color': 'green', 'fontWeight': 'bold'}),
                            dcc.Graph(id='SPED_Me', style={'width': '400px', 'height': '400px'}),
                            html.P(id='SPED_Me_Text', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Masters", style={'textAlign': 'center', 'color': 'purple', 'fontWeight': 'bold'}),
                            dcc.Graph(id='SPED_Ma', style={'width': '400px', 'height': '400px'}),
                            html.P(id='SPED_Ma_Text', style={'textAlign': 'center'})
                        ], width=4, className='mb-4', style={'paddingTop': '0', 'marginTop': '-9px'}),
                    ]),
                ])
            ]),
        ])
    ])

app.layout = layout3()

# Define callback to update graphs based on dropdown and radio selection
@app.callback(
    [Output('FMAG', 'figure'),
     Output('FMMG', 'figure'),
     Output('FMMAG', 'figure'),
     Output('FMA', 'children'),
     Output('FMM', 'children'),
     Output('FMMA', 'children'),
     Output('SPED_App', 'figure'),
     Output('SPED_Me', 'figure'),
     Output('SPED_Ma', 'figure'),
     Output('SPED_App_Text', 'children'),
     Output('SPED_Me_Text', 'children'),
     Output('SPED_Ma_Text', 'children')],
    [Input('SD', 'value'),
     Input('SchoolType', 'value')]
)
def update_graphs(selected_district, school_type):
    if selected_district is None or school_type is None:
        raise PreventUpdate

    df_filtered = merge_df.copy()

    if selected_district != 'All':
        df_filtered = df_filtered[df_filtered['DISTNAME'] == selected_district]

    if school_type != 'All':
        df_filtered = df_filtered[df_filtered['SCHOOLTYPE'] == school_type]

    # Create the figures
    el_app_figure = px.bar(df_filtered, x='CAMPUS', y=el_app, title='Approaches (Emergent Bilinguals)')
    el_meets_figure = px.bar(df_filtered, x='CAMPUS', y=el_meets, title='Meets (Emergent Bilinguals)')
    el_ma_figure = px.bar(df_filtered, x='CAMPUS', y=el_ma, title='Masters (Emergent Bilinguals)')
    
    sped_app_figure = px.bar(df_filtered, x='CAMPUS', y=sped_app, title='Approaches (SPED)')
    sped_me_figure = px.bar(df_filtered, x='CAMPUS', y=sped_me, title='Meets (SPED)')
    sped_ma_figure = px.bar(df_filtered, x='CAMPUS', y=sped_ma, title='Masters (SPED)')


if __name__ == '__main__':
    app.run_server(debug=True)
