# TEA DASHBOARD IDEAS

![image](https://github.com/user-attachments/assets/256c2394-89b5-407d-a393-0a2780adf6be)

In this project, I created a dashboard to highlight 2017-2019 student performances using POWER BI and Dash.

## Power BI

_Disclaimer: I do not have the appropriate credentials to export the dashboards for users to manipulate._

### Dashboard Sections

- **[Overview Tab](#overview-tab)**
- **[By Gender Tab](#by-gender-tab)**
- **[By Races Tab](#by-races-tab)**
- **[By Special Population Tab](#by-special-population-tab)**

### Overview Tab

![image](https://github.com/user-attachments/assets/af7c2875-3a8f-4d59-837f-96b1e245c870)

The Overview Tab allows you to view RLA-related distinctions and the difference in overall performance from 2017 to 2018. Users can select a specific district by choosing from the dropdown menu on the upper right. By default, the data for all districts is displayed.

### By Gender Tab

![image](https://github.com/user-attachments/assets/4daf5194-cf2b-44dc-b0be-ec49eaa77c09)

The By Gender Tab enables users to compare performance by gender across two years. Users can select a specific district from the dropdown menu on the upper right. The default view shows data for all districts.

### By Races Tab

![image](https://github.com/user-attachments/assets/26c1672a-9490-4386-81ca-1fb078011c14)

The By Races Tab allows users to compare performance by race across two years. Users can select a specific district from the dropdown menu on the upper right. By default, data for all districts is shown.

### By Special Population Tab

![image](https://github.com/user-attachments/assets/1f5bc10a-4a59-4a3f-9461-c9e5436e1492)

The By Special Population Tab enables users to compare performance for additional student populations across two years. Users can select a specific district from the dropdown menu on the upper right. By default, data for all districts is displayed.

## DASH

In this section, I will present an alternative version of the same dashboard made with Plotly. The full web app can be found at:

I started with Jupyter notebook but soon realized that using Python would make it easier to make the app more robust.

Here is an overview:

## All Tabs
## Table of Contents
- **[Combined tabs](#tab-1)**
- **[Tab 1](#tab-1)**
- **[Tab 2](#tab-2)**
- **[Tab 3](#tab-3)**
### Combined tabs
![image](https://github.com/user-attachments/assets/65c279a9-f36b-44b6-aab0-d46553202951)

#### Entire Code
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

#Import layouts and callbacks from tab1a, tab2a, and tab3a
from tab1a2 import layout as tab1_layout, register_callbacks as tab1_callbacks
from tab2ab import layout2 as tab2_layout, register_callbacks2 as tab2_callbacks
from tab3ab import layout3 as tab3_layout, register_callbacks3 as tab3_callbacks

#Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

#Define the main layout with tabs
app.layout = dbc.Container([
    dcc.Tabs([
        dcc.Tab(label='Tab 1: Overview', children=[tab1_layout()]),
        dcc.Tab(label='Tab 2: Student Performance', children=[tab2_layout()]),
        dcc.Tab(label='Tab 3: Sped and EB', children=[tab3_layout()])
    ])
], fluid=True)

#Register callbacks for all tabs
tab1_callbacks(app)
tab2_callbacks(app)
tab3_callbacks(app)

#Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8059)

### Tab 1
![image](https://github.com/user-attachments/assets/7fa0b4dc-8dac-4480-bdba-df994021b146)
![image](https://github.com/user-attachments/assets/8b9236a3-752c-438f-bfbd-97bcf67364f1
![image](https://github.com/user-attachments/assets/5902199d-e170-4dc1-ae21-092a467f982c)

#Layout definition(front end)
def layout():
    return dbc.Container([
        html.H1("School District Dashboard"),

        dcc.Tabs([
            dcc.Tab(label='Academic Achievement & Ratings', children=[
                dbc.Container([
                    dbc.Row([
                        dbc.Col(dcc.Dropdown(
                            id="SD",
                            options=[{'label': 'All DISTRICTS', 'value': 'All'}] +
                                    [{'label': district, 'value': district} for district in Data_df3['DISTNAME'].unique()],
                            style={'color': 'black'},
                            value='All'  # Default value
                        ), width=6),

                        dbc.Col(dcc.RadioItems(
                            id='SchoolType',
                            options=[
                                {'label': 'Elementary', 'value': 'E'},
                                {'label': 'Middle', 'value': 'M'},
                                {'label': 'High', 'value': 'S'},
                                {'label': 'Charter', 'value': 'B'},
                                {'label': 'All', 'value': 'All'}
                            ],
                            value='All'  # Default value
                        ), width=6),
                    ], className='mb-4'),

                    dbc.Row([
                        dbc.Col([
                            html.H3("Academic Achievement in Mathematics", style={'textAlign': 'center'}),
                            dcc.Graph(id='Mathg', style={'width': '400px', 'height': '400px'}),
                            html.P(id='Math', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Academic Achievement in English Language Arts/Reading", style={'textAlign': 'center'}),
                            dcc.Graph(id='rlag', style={'width': '400px', 'height': '400px'}),
                            html.P(id='rla', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Academic Achievement in Science", style={'textAlign': 'center'}),
                            html.Br(),
                            html.Div(style={'height': '0.5em'}),
                            dcc.Graph(id='scienceg', style={'width': '400px', 'height': '400px'}),
                            html.P(id='science', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H3("Academic Achievement in Social Studies", style={'textAlign': 'center'}),
                            dcc.Graph(id='ssg', style={'width': '400px', 'height': '400px'}),
                            html.P(id='ss', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Top 25 Percent: Comparative Academic Growth", style={'textAlign': 'center'}),
                            dcc.Graph(id='cgg', style={'width': '400px', 'height': '400px'}),
                            html.P(id='cg', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),

                        dbc.Col([
                            html.H3("Top 25 Percent: Comparative Closing the Gaps", style={'textAlign': 'center'}),
                            dcc.Graph(id='cg2g', style={'width': '400px', 'height': '400px'}),
                            html.P(id='cg2', style={'textAlign': 'center'})
                        ], width=4, className='mb-4'),
                    ]),

                    html.H2("SCHOOL RATINGS", style={'textAlign': 'center', 'marginTop': '40px'}),
                    dcc.Graph(id='Graph1', style={'height': '600px'}),
                ], fluid=True)
            ]),

            dcc.Tab(label='Different Dashboard', children=[
                html.Div([
                    html.H2("Student Performance", style={'textAlign': 'center'}),
                  
                ])
            ])
        ])
    ], fluid=True)

### TAB 2

![image](https://github.com/user-attachments/assets/86178398-2096-4fdf-bb1b-d19a22f3f5e7)
![image](https://github.com/user-attachments/assets/3cf004c2-2a08-4ff5-8fb5-4dab15b50ee0)

### Tab3
![image](https://github.com/user-attachments/assets/4cb57319-d6b8-42be-81f8-77d680775de3)
![image](https://github.com/user-attachments/assets/67f4531d-0b5e-49b2-8877-59bd2ff3c1ae)
*For some reason I am missing 2019 Sped App values





