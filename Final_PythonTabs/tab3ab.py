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
                            id="SD3",
                            options=[{'label': 'All DISTRICTS', 'value': 'All'}] +
                                    [{'label': district, 'value': district} for district in merge_df['DISTNAME'].unique()],
                            style={'color': 'black'},
                            value='All'  # Default value
                        ), width=6),

                        dbc.Col(dcc.RadioItems(
                            id='SchoolType3',
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
                            dcc.Graph(id='ELAG', style={'width': '400px', 'height': '400px'}),
                            html.P(id='ELA', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Meets", style={'textAlign': 'center', 'color': 'green', 'fontWeight': 'bold'}),
                            dcc.Graph(id='ELMG', style={'width': '400px', 'height': '400px'}),
                            html.P(id='ELM', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Masters", style={'textAlign': 'center', 'color': 'purple', 'fontWeight': 'bold'}),
                            dcc.Graph(id='ELMAG', style={'width': '400px', 'height': '400px'}),
                            html.P(id='ELMA', style={'textAlign': 'center'})
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

color_map = {
    'App_El_18': 'orange',
    'App_El_19':'blue',
    'Me_El_18':'orange',
    'Me_El_19':'blue',
    'Ma_El_18': 'orange',
    'Ma_El_19':'blue',
    'App_Sped_18':'orange',
    'Me_Sped_18': 'orange',
    'Me_Sped_19':'blue',
    'Ma_Sped_18':'orange',
    'Ma_Sped_19':'blue'
}

# Define calculation and graph generation functions
def calculate_averages(df, cols):
    return df[cols].mean().to_dict()

def generate_bar_graph(averages, title):
    categories = list(averages.keys())
    values = list(averages.values())
    
    # Calculate the average for categories ending with '18'
    trendline_values = [averages[cat] for cat in categories if '18' in cat]
    if trendline_values:
        avg_trendline_value = sum(trendline_values) / len(trendline_values)
    else:
        avg_trendline_value = 0

    fig = px.bar(
        x=categories,
        y=values
    )

    colors = [color_map.get(cat, 'grey') for cat in categories]
    fig.update_traces(marker_color=colors)
# Determine which trendline to add based on the title
    trendline_categories = {
        'Approaches': 'Approaches_All',
        'Meets': 'Meets_All',
        'Masters': 'Masters_All'
    }
    trendline_category = next((value for key, value in trendline_categories.items() if key in title), None)
    
    if trendline_category and trendline_category in averages:
        # Calculate the y-value for the trendline
        avg_trendline_value = averages[trendline_category]
        
        # Create x-values for the trendline (use the same categories as the bar chart)
        x_trendline = categories
        y_trendline = [avg_trendline_value] * len(categories)
        

    # Add trendline
    fig.add_trace(go.Scatter(
        x=categories,
        y=[avg_trendline_value] * len(categories),
        mode='lines',
        name='2018 Avg Performance',
        line=dict(color='black', dash='dash')
    ))
    fig.update_layout(
        xaxis_title='',  # Hide x-axis title
        yaxis_title='',  # Hide y-axis title
        xaxis_tickangle=-45
    )
    
    return fig
def register_callbacks3(app):
    @app.callback(
        [Output("ELAG", "figure"),
         Output("ELMG", "figure"),
         Output("ELMAG", "figure"),
         Output("SPED_App", "figure"),
         Output("SPED_Me", "figure"),
         Output("SPED_Ma", "figure")],
        [Input("SD3", "value"),
         Input("SchoolType3", "value")]
    )
    def update_cards(selected_district, selected_school_type):
        # Filtering the DataFrame based on the selected values
        if selected_district == 'All':
            filtered_df = merge_df
        else:
            filtered_df = merge_df[merge_df['DISTNAME'] == selected_district]

        if selected_school_type != 'All':
            filtered_df = filtered_df[filtered_df['GRDTYPE'] == selected_school_type]

        print("Filtered DataFrame shape:", filtered_df.shape)  # Debugging print

        if filtered_df.empty:
            print("No data available for the selected filters.")
            return (
                generate_bar_graph([], 'Approaches'),
                generate_bar_graph([], 'Meets'),
                generate_bar_graph([], 'Masters'),
                generate_bar_graph([], 'Approaches'),
                generate_bar_graph([], 'Meets'),
                generate_bar_graph([], 'Masters')
            )

        # Calculating averages for each category
        fmag_averages = calculate_averages(filtered_df, el_app)
        fmmg_averages = calculate_averages(filtered_df, el_meets)
        fmmag_averages = calculate_averages(filtered_df, el_ma)
        rag_averages = calculate_averages(filtered_df, sped_app)
        ramg_averages = calculate_averages(filtered_df, sped_me)
        raag_averages = calculate_averages(filtered_df, sped_ma)

        # Generating figures for each output
        return (
            generate_bar_graph(fmag_averages, 'Approaches'),
            generate_bar_graph(fmmg_averages, 'Meets'),
            generate_bar_graph(fmmag_averages, 'Masters'),
            generate_bar_graph(rag_averages, 'Approaches'),
            generate_bar_graph(ramg_averages, 'Meets'),
            generate_bar_graph(raag_averages, 'Masters')
        )
