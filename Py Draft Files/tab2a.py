# Importing Dependencies
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

import dash
from dash import dcc, html
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

# Define the path to the CSV files
Data2 = Path("RESOURCES/Data Team Performance Task_Raw Dataset (1).xlsx - 2018-19 STAAR GRADE 3 ELA (2).csv")
Data3 = Path("Overview Data/Data Team Performance Task_Raw Dataset.xlsx - 2018-19 CAMPUS (2).csv")

# Read the CSV files into pandas DataFrames
Data_df2 = pd.read_csv(Data2)
Data_df3 = pd.read_csv(Data3)

# Header mapping

header_mapping2 = {
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
Data_df2 = Data_df2.rename(columns=header_mapping2)
Data_df2.replace([-1, '.'], pd.NA, inplace=True)

for col in Data_df2.columns:
    if col != 'CAMPUS':
        Data_df2[col] = Data_df2[col].astype('Int64')

# Merge DataFrames
merge_df = pd.merge(Data_df3, Data_df2, on='CAMPUS')

# Column name mapping

col_mapping3 = {
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate': 'Meets_AA',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate': 'Meets_All',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate': 'Meets_AI',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate': 'Meets_Asian',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate': 'Meets_Hispanic',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate': 'Meets_PI',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate': 'Meets_TwoRaces',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate': 'Meets_White',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate': 'Masters_AA',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate': 'Masters_All',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate': 'Masters_AI',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate': 'Masters_Asian',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate': 'Masters_Hispanic',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate': 'Masters_PI',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate': 'Masters_TwoRaces',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate': 'Masters_White',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate': 'Female_Approaches',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate': 'Male_Approaches',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate': 'Female_Meets',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate': 'Male_Meets',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate': 'Female_Masters',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate': 'Male_Masters',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate': 'Approaches_AA',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate': 'Approaches_All',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate': 'Approaches_AI',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate': 'Approaches_Hispanic',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate': 'Approaches_PI',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate': 'Approaches_Sped',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate': 'Approaches_TwoRaces',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate': 'Approaches_White',
}
# Column name mapping
col_mapping3 = {
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate': 'Meets_AA',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate': 'Meets_All',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate': 'Meets_AI',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate': 'Meets_Asian',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate': 'Meets_Hispanic',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate': 'Meets_PI',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate': 'Meets_TwoRaces',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate': 'Meets_White',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate': 'Masters_AA',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate': 'Masters_All',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate': 'Masters_AI',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Asian, STAAR Reading/ELA Rate': 'Masters_Asian',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate': 'Masters_Hispanic',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate': 'Masters_PI',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate': 'Masters_TwoRaces',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate': 'Masters_White',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate': 'Female_Approaches',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate': 'Male_Approaches',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate': 'Female_Meets',
    'Campus 2019 Domain 1A: Meets Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate': 'Male_Meets',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Female, STAAR Reading/ELA Rate': 'Female_Masters',
    'Campus 2019 Domain 1A: Masters Grade Level STD, Grade 3, Male, STAAR Reading/ELA Rate': 'Male_Masters',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, African American, STAAR Reading/ELA Rate': 'Approaches_AA',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, All Students, STAAR Reading/ELA Rate': 'Approaches_All',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, American Indian, STAAR Reading/ELA Rate': 'Approaches_AI',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Hispanic, STAAR Reading/ELA Rate': 'Approaches_Hispanic',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Pacific Islander, STAAR Reading/ELA Rate': 'Approaches_PI',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Special Ed, STAAR Reading/ELA Rate': 'Approaches_Sped',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, Two or More Races, STAAR Reading/ELA Rate': 'Approaches_TwoRaces',
    'Campus 2019 Domain 1A: Approaches Grade Level STD, Grade 3, White, STAAR Reading/ELA Rate': 'Approaches_White',
}

# Rename columns in the DataFrame
merge_df.rename(columns=col_mapping3, inplace=True)


# Define column lists
fmag_cols = ['Female_Approaches', 'Male_Approaches']
fmmg_cols = ['Female_Meets', 'Male_Meets']
fmmag_cols = ['Female_Masters', 'Male_Masters']
rag_cols = ['Approaches_AA', 'Approaches_All', 'Approaches_AI', 'Approaches_Hispanic', 'Approaches_PI', 'Approaches_Sped', 'Approaches_TwoRaces', 'Approaches_White']
ramg_cols = ['Meets_AA', 'Meets_All', 'Meets_AI', 'Meets_Asian', 'Meets_Hispanic', 'Meets_PI', 'Meets_TwoRaces', 'Meets_White']
raag_cols = ['Masters_AA', 'Masters_All', 'Masters_AI', 'Masters_Asian', 'Masters_Hispanic', 'Masters_PI', 'Masters_TwoRaces', 'Masters_White']

# Color mapping
color_map = color_map = {
    'Female_Approaches': 'pink',
    'Male_Approaches':'blue',
    'Female_Meets':'pink',
    'Male_Meets':'blue',
    'Female_Masters':'pink',
    'Male_Masters': 'blue', 
    'Approaches_AA':'black',
    'Approaches_All':'grey',
    'Approaches_AI':'orange',
    'Approaches_Hispanic':'brown',
    'Approaches_PI':'yellow',
    'Approaches_Sped':'green',
    'Approaches_TwoRaces':'purple',
    'Approaches_White':'white',
    'Meets_AA':'black',
    'Meets_All':'grey',
    'Meets_AI':'orange',
    'Meets_Asian':'pink',
    'Meets_Hispanic':'brown',
    'Meets_PI':'yellow',
    'Meets_TwoRaces':'purple',
    'Meets_White':'white',
    'Masters_AA':'black',
    'Masters_All':'grey',
    'Masters_AI':'orange',
    'Masters_Asian':'pink',
    'Masters_Hispanic':'orange',
    'Masters_PI':'yellow',
    'Masters_TwoRaces':'purple',
    'Masters_White':'white'
    }
# Define layout function
def layout2():
    return dbc.Container([
        html.H1("School District Dashboard"),

        dbc.Container([
            dbc.Row([
                dbc.Col(dcc.Dropdown(
                    id="SD2",
                    options=[{'label': 'All DISTRICTS', 'value': 'All'}] +
                            [{'label': district, 'value': district} for district in merge_df['DISTNAME'].unique()],
                    style={'color': 'black'},
                    value='All'  # Default value
                ), width=6),

                dbc.Col(dcc.RadioItems(
                    id='SchoolType2',
                    options=[
                        {'label': 'Elementary', 'value': 'E'},
                        {'label': 'Charter', 'value': 'B'},
                        {'label': 'All', 'value': 'All'}
                    ],
                    value='All'  # Default value
                ), width=6),
            ], className='mb-4'),

            html.Br(),
            # Add the centered h2 title here
            html.Div([
                html.H2("Female Vs Male", style={'textAlign': 'center', 'fontStyle': 'italic', 'color': 'black'})
            ], style={
                'border': '2px solid black',        # Border of the rectangle
                'borderRadius': '15px',             # Curvy corners
                'padding': '10px',                  # Space inside the rectangle
                'backgroundColor': '#f2f2f2',       # Background color of the rectangle
                'boxShadow': '0px 4px 8px rgba(0,0,0,0.1)',  # Shadow effect
                'margin': '20px auto'               # Centered margin
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
                    html.Div(style={'height': '0.5em'}),
                    dcc.Graph(id='FMMAG', style={'width': '400px', 'height': '400px'}),
                    html.P(id='FMMA', style={'textAlign': 'center'})
                ], width=4, className='mb-4'),
            ]),
            html.Br(),
            html.Div([
                html.H2("Across Racial Categories", style={'textAlign': 'center', 'fontStyle': 'italic', 'color': 'black'})
            ], style={
                'border': '2px solid black',        # Border of the rectangle
                'borderRadius': '15px',             # Curvy corners
                'padding': '10px',                  # Space inside the rectangle
                'backgroundColor': '#f2f2f2',       # Background color of the rectangle
                'boxShadow': '0px 4px 8px rgba(0,0,0,0.1)',  # Shadow effect
                'margin': '20px auto'               # Centered margin
            }),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.H3("Approaches", style={'textAlign': 'center', 'color': 'orange', 'fontWeight': 'bold'}),
                    dcc.Graph(id='RAG', style={'width': '400px', 'height': '400px'}),
                    html.P(id='RA', style={'textAlign': 'center'})
                ], width=4, className='mb-4'),

                dbc.Col([
                    html.H3("Meets", style={'textAlign': 'center', 'color': 'green', 'fontWeight': 'bold'}),
                    dcc.Graph(id='RAMG', style={'width': '400px', 'height': '400px'}),
                    html.P(id='RAM', style={'textAlign': 'center'})
                ], width=4, className='mb-4'),

                dbc.Col([
                    html.H3("Masters", style={'textAlign': 'center', 'color': 'purple', 'fontWeight': 'bold'}),
                    html.Div(style={'height': '0.5em'}),
                    dcc.Graph(id='RMAG', style={'width': '400px', 'height': '400px'}),
                    html.P(id='RMA', style={'textAlign': 'center'})
                ], width=4, className='mb-4'),
            ])
        ])
    ])


# Define calculation and graph generation functions
def calculate_averages(df, cols):
    return df[cols].mean().to_dict()

def generate_bar_graph(averages, title):
    categories = list(averages.keys())
    values = list(averages.values())

    # Create a bar graph
    fig = px.bar(
        x=categories,
        y=values,
        labels={'x': 'Category', 'y': 'Average Rate'},
        title=title
    )

    # Extract colors in the same order as categories
    colors = [color_map.get(cat, 'grey') for cat in categories]

    # Update trace to use the defined colors
    fig.update_traces(marker_color=colors)

    # Determine which trendline to add based on the title
    trendline_categories = {
        'Approaches': 'Approaches_All',
        'Meets': 'Meets_All',
        'Masters': 'Masters_All'
    }

    # Find the trendline category based on the title
    trendline_category = next((value for key, value in trendline_categories.items() if key in title), None)

    if trendline_category and trendline_category in averages:
        # Add trendline as a scatter plot
        fig.add_trace(go.Scatter(
            x=[categories[0], categories[-1]],
            y=[averages[trendline_category], averages[trendline_category]],
            mode='lines',
            name='All Students',
            line=dict(color='red', width=2, dash='dash')
        ))

    return fig

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Set the layout of the app
app.layout = layout2

# Define callbacks
def register_callbacks2(app):
    @app.callback(
        [   Output('FMAG', 'figure'),
            Output('FMMG', 'figure'),
            Output('FMMAG', 'figure'),
            Output('RAG', 'figure'),
            Output('RAMG', 'figure'),
            Output('RMAG', 'figure'),
            Output('FMA', 'children'),
            Output('FMM', 'children'),
            Output('FMMA', 'children'),
            Output('RA', 'children'),
            Output('RAM', 'children'),
            Output('RMA', 'children')
        ],
        [   Input('SD2', 'value'),
            Input('SchoolType2', 'value')]
    )
    def update_graphs(selected_district, school_type):
        if not selected_district or not school_type:
            raise PreventUpdate

        # Filter data based on selected district and school type
        filtered_df = merge_df.copy()
        if selected_district != 'All':
            filtered_df = filtered_df[filtered_df['DISTNAME'] == selected_district]
        if school_type != 'All':
            filtered_df = filtered_df[filtered_df['SCHTYPE'] == school_type]

        # Calculate averages
        fmag_averages = calculate_averages(filtered_df, fmag_cols)
        fmmg_averages = calculate_averages(filtered_df, fmmg_cols)
        fmmag_averages = calculate_averages(filtered_df, fmmag_cols)
        rag_averages = calculate_averages(filtered_df, rag_cols)
        ramg_averages = calculate_averages(filtered_df, ramg_cols)
        rag_averages = calculate_averages(filtered_df, rag_cols)
        rmag_averages = calculate_averages(filtered_df, raag_cols)

        # Generate bar graphs
        fmag_figure = generate_bar_graph(fmag_averages, 'Female Vs Male Approaches')
        fmmg_figure = generate_bar_graph(fmmg_averages, 'Female Vs Male Meets')
        fmmag_figure = generate_bar_graph(fmmag_averages, 'Female Vs Male Masters')
        rag_figure = generate_bar_graph(rag_averages, 'Approaches Across Racial Categories')
        ramg_figure = generate_bar_graph(ramg_averages, 'Meets Across Racial Categories')
        rmag_figure = generate_bar_graph(rmag_averages, 'Masters Across Racial Categories')

        return (fmag_figure, fmmg_figure, fmmag_figure, rag_figure, ramg_figure, rmag_figure,
                fmag_averages['Female_Approaches'], fmmg_averages['Female_Meets'], fmmag_averages['Female_Masters'],
                rag_averages['Approaches_AA'], ramg_averages['Meets_AA'], rmag_averages['Masters_AA'])

# Register callbacks
register_callbacks2(app)

