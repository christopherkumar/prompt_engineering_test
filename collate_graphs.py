from dash import Dash, html, dcc, Input, Output
import os

app = Dash(__name__)

# Define the directories for scripts and short_answers
base_directory_scripts = 'C:/path/to/your/testdata-scripts/'
base_directory_short_answers = 'C:/path/to/your/testdata-short_answers/'


def generate_file_paths(base_directory, max_complexity):
    file_paths = {}
    for complexity in range(1, max_complexity + 1):
        path = os.path.join(base_directory, f'complexity{complexity}/results_final/interactive_plot.html')
        if os.path.exists(path):
            file_paths[f'Complexity {complexity}'] = path
    return file_paths


# Initial file paths (can start with either based on preference)
initial_files = generate_file_paths(base_directory_scripts, 6)

app.layout = html.Div([
    dcc.RadioItems(
        id='assessment-type',
        options=[
            {'label': 'Scripts', 'value': 'scripts'},
            {'label': 'Short Answers', 'value': 'short_answers'}
        ],
        value='scripts',
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': key, 'value': value} for key, value in initial_files.items()],
        value=next(iter(initial_files.values())) if initial_files else None
    ),
    html.Iframe(
        id='display-frame',
        style={'width': '100%', 'height': '700px'}
    )
])


@app.callback(
    Output('file-dropdown', 'options'),
    Output('file-dropdown', 'value'),
    Input('assessment-type', 'value')
)
def update_file_dropdown(assessment_type):
    if assessment_type == 'scripts':
        files = generate_file_paths(base_directory_scripts, 6)
    else:
        files = generate_file_paths(base_directory_short_answers, 4)
    options = [{'label': key, 'value': value} for key, value in files.items()]
    return options, next(iter(files.values())) if files else None


@app.callback(
    Output('display-frame', 'srcDoc'),
    Input('file-dropdown', 'value')
)
def update_iframe(src):
    if src:
        try:
            with open(src, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Error loading graph: {str(e)}"
    return "Please select a file to display."


if __name__ == '__main__':
    app.run_server(debug=False)


# Usage with pyinstaller
# pyinstaller --onefile --add-data="path/to/assets;assets" collate_graphs.py
# pyinstaller collate_graphs.spec
# .\dist\collate_graphs.exe
