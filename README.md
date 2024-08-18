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
- **[Tab 1](#tab-1)**
- **[Tab 2](#tab-2)**
- **[Tab 3](#tab-3)**

### Tab 1


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
![image](https://github.com/user-attachments/assets/7fa0b4dc-8dac-4480-bdba-df994021b146)
![image](https://github.com/user-attachments/assets/8b9236a3-752c-438f-bfbd-97bcf67364f1
![image](https://github.com/user-attachments/assets/5902199d-e170-4dc1-ae21-092a467f982c)

### TAB 2

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

![image](https://github.com/user-attachments/assets/86178398-2096-4fdf-bb1b-d19a22f3f5e7)
![image](https://github.com/user-attachments/assets/3cf004c2-2a08-4ff5-8fb5-4dab15b50ee0)

### Tab3


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
![image](https://github.com/user-attachments/assets/4cb57319-d6b8-42be-81f8-77d680775de3)
![image](https://github.com/user-attachments/assets/67f4531d-0b5e-49b2-8877-59bd2ff3c1ae)
*For some reason I am missing 2019 Sped App values





