# Importing Dependencies
import pandas as pd
from pathlib import Path
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'notebook'

# Loading files
Data3 = Path("Overview Data/Data Team Performance Task_Raw Dataset.xlsx - 2018-19 CAMPUS (2).csv")

Data_df3 = pd.read_csv(Data3)

# Layout definition
# Layout definition
def layout():
    return dbc.Container([
        html.H1("School District Dashboard"),
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
    ], fluid=True)

# Callbacks remain unchanged

# Callbacks
def register_callbacks(app):
    @app.callback(
        [
            Output("Mathg", "figure"),
            Output("rlag", "figure"),
            Output("scienceg", "figure"),
            Output("ssg", "figure"),
            Output("cgg", "figure"),
            Output("cg2g", "figure")
        ],
        [Input("SD", "value"),
         Input("SchoolType", "value")]
    )
    def update_cards(selected_district, selected_school_type):
        # Filter DataFrame based on selected district
        if selected_district == 'All':
            filtered_df = Data_df3
        else:
            filtered_df = Data_df3[Data_df3['DISTNAME'] == selected_district]

        # Further filter by school type
        if selected_school_type != 'All':
            filtered_df = filtered_df[filtered_df['GRDTYPE'] == selected_school_type]

        # Calculate the total number of possible points (rows in filtered_df)
        total_possible_points = filtered_df.shape[0]

        # Check if there are no rows to avoid division by zero
        if total_possible_points == 0:
            return (px.pie(names=["N/A"], values=[1], hole=0.5),) * 6
        
        # Calculate counts
        Ma = filtered_df['CAD_MATH'].sum()
        Rla = filtered_df['CAD_READ'].sum()
        sc = filtered_df['CAD_SCIE'].sum()
        ss = filtered_df['CAD_SOCI'].sum()
        cad = filtered_df['CAD_PROGRESS'].sum()
        pro = filtered_df['CAD_GAP'].sum()
        
        # Create pie charts with percentage representation
        def create_pie_chart(count, total):
            return px.pie(
                names=['Earned', 'Not Earned'],
                values=[count, total - count],
                title=f"{count} out of {total} possible points",
                hole=0.5,
                labels={'Earned': 'Earned', 'Not Earned': 'Not Earned'},
                color_discrete_sequence=['red', 'green']
            ).update_layout(
                title_text=f"{count/total*100:.1f}%",
                title_x=0.5,
                title_y=0.85
            )

        # Generate pie charts
        pie_math = create_pie_chart(Ma, total_possible_points)
        pie_rla = create_pie_chart(Rla, total_possible_points)
        pie_science = create_pie_chart(sc, total_possible_points)
        pie_ss = create_pie_chart(ss, total_possible_points)
        pie_cg = create_pie_chart(cad, total_possible_points)
        pie_cg2 = create_pie_chart(pro, total_possible_points)
        
        return (pie_math, pie_rla, pie_science, pie_ss, pie_cg, pie_cg2)

    @app.callback(
        Output("Graph1", "figure"),
        [Input("SD", "value"),
         Input("SchoolType", "value")]
    )
    def update_graphs(selected_district, selected_school_type):
        # Filter DataFrame based on selected district
        if selected_district == 'All':
            filtered_df = Data_df3
        else:
            filtered_df = Data_df3[Data_df3['DISTNAME'] == selected_district]

        # Further filter by school type
        if selected_school_type != 'All':
            filtered_df = filtered_df[filtered_df['GRDTYPE'] == selected_school_type]
        
        # Group by 'C_RATING' and count occurrences
        rating_counts = filtered_df.groupby('C_RATING').size().reset_index(name='Count')
        
        # Define color mapping for each rating
        color_map = {
            'A': 'green',
            'B': 'blue',
            'C': 'orange',
            'D': 'purple',
            'Data Integrity Issues': 'pink',
            'F': 'red',
            'Not Rated': 'black'
        }
        
        # Order the categories
        rating_order = ['A', 'B', 'C', 'D', 'F', 'Data Integrity Issues', 'Not Rated']
        
        # Create bar chart
        fig1 = px.bar(
            rating_counts,
            x='C_RATING',
            y='Count',
            title='School Rating Count',
            color='C_RATING',
            color_discrete_map=color_map,
            category_orders={'C_RATING': rating_order}
        )
        
        # Update the legend title
        fig1.update_layout(
            legend_title_text='School Ratings',
            title='',
            xaxis_title='School Rating',
            yaxis_title=''
        )
        
        return fig1
