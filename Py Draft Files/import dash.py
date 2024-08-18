import dash
from dash import dcc, html, Input, Output
import openai

# Initialize the app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        id='writing-input',
        placeholder='Enter the writing response here...',
        style={'width': '100%', 'height': 200}
    ),
    html.Button('Grade Response', id='submit-button', n_clicks=0),
    html.Div(id='grading-output')
])

@app.callback(
    Output('grading-output', 'children'),
    Input('submit-button', 'n_clicks'),
    Input('writing-input', 'value')
)
def grade_response(n_clicks, response_text):
    if n_clicks > 0 and response_text:
        # Example rubric (can be customized)
        rubric = {
            "clarity": "Is the response clear and easy to understand?",
            "grammar": "Are there any grammatical errors?",
            "content": "Does the response adequately cover the topic?"
        }

        # Call ChatGPT (OpenAI API)
        result = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Please grade the following response based on this rubric: {rubric}. Response: {response_text}"}
            ]
        )
        grading_result = result.choices[0].message['content']
        return grading_result
    return "Enter a response and click 'Grade Response' to see feedback."

if __name__ == '__main__':
    app.run_server(debug=True)
