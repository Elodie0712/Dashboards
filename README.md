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

# Layout definition
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
                    # Add content for the second tab here
                ])
            ])
        ])
    ], fluid=True)
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

### TAB 2

![image](https://github.com/user-attachments/assets/86178398-2096-4fdf-bb1b-d19a22f3f5e7)
![image](https://github.com/user-attachments/assets/3cf004c2-2a08-4ff5-8fb5-4dab15b50ee0)

### Tab3
![image](https://github.com/user-attachments/assets/4cb57319-d6b8-42be-81f8-77d680775de3)
![image](https://github.com/user-attachments/assets/67f4531d-0b5e-49b2-8877-59bd2ff3c1ae)
*For some reason I am missing 2019 Sped App values





