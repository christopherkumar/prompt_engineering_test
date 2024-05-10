# ---------------------------------------------------------
# Assessment Analysis and Plotting Tool
# ---------------------------------------------------------
# This script facilitates the analysis and visualization of assessment scores.
# It supports input from JSON formatted score data and provides functionality
# to process either script-based or short-answer assessments. Results include
# calculated metrics like R-squared, Mean Squared Error (MSE), and Mean Absolute Error (MAE),
# and are visualized using Plotly for an interactive review of performance comparisons.
#
# Usage:
#   Run with command-line arguments:
#   - `--scripts` to process script-based assessments
#   - `--short_answers` to process short-answer assessments
#
# Author: Christopher Vishnu Kumar
# Date: 07/05/2024
# ---------------------------------------------------------

# Standard library imports
import os
import argparse
import json

# Third-party imports
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from plotly.offline import plot
import plotly.graph_objs as go

# Define command-line arguments
parser = argparse.ArgumentParser(description="Analyze and plot R-squared values based on the selected mode.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--scripts', action='store_true', help='Analyze script-based assessments.')
group.add_argument('--short_answers', action='store_true', help='Analyze short answer assessments.')
args = parser.parse_args()


# Define scoring scale and weights
scoring_scale = {
    'Poor': 1,
    'OK': 2,
    'Competent': 3,
    'Excellent': 4,
    'Perfect': 5,
    'Not found': 0  # Handling "Not found" as per instruction
}

# Adjust settings based on user input
if args.scripts:
    weights = {
        'Functionality': 0.10,
        'Logic': 0.30,
        'Code Quality': 0.30,
        'User Input Handling': 0.20,
        'Documentation': 0.10
    }
    base_directory_path = 'C:/path/to/you/testdata-scripts/'
elif args.short_answers:
    weights = {
        'Understanding of the Topic': 0.30,
        'Argumentation and Evidence': 0.60,
        'Organization and Clarity': 0.10
    }
    base_directory_path = 'C:/path/to/your/testdata-short_answers/'


# Calculate the maximum possible weighted score
max_possible_score = sum(weights[category] * 5 * 20 for category in weights)  # Assume highest score is 5 ("Perfect")


def parse_score(score):
    """ Parse the score to handle numeric values, ranges, and text. """
    if isinstance(score, str):
        numeric_parts = ''.join(filter(str.isdigit, score.split('-')[0]))
        if '-' in score and numeric_parts.isdigit():
            low, high = map(float, score.split('-'))
            return (low + high) / 2  # Median of the range
        elif numeric_parts.isdigit():
            return float(numeric_parts)
        else:
            return scoring_scale.get(score, 0)
    return float(score)


def process_scores_text(filename):
    """ Process textual scores and calculate weighted total scores, ensuring they do not exceed 100. """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for entry in data:
                scores = entry['scores']
                weighted_scores = sum(parse_score(score) * weights[category] * 20 for category, score in scores.items())
                scaled_score = (weighted_scores / max_possible_score) * 100
                entry['total_score'] = min(scaled_score, 100)  # Ensure score does not exceed 100
        return data
    except IOError:
        print(f"Error reading file: {filename}")
        return []


def process_scores_numeric(filename):
    """ Process numeric scores and calculate total scores based on the file name, ensuring they do not exceed 100. """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for entry in data:
                scores = entry['scores']
                if 'nonweighted' in filename:
                    weighted_scores = sum(parse_score(score) * weights[category] * 20 for category, score in scores.items())
                elif 'weighted' in filename:
                    weighted_scores = sum(parse_score(score) for score in scores.values())
                else:
                    weighted_scores = sum(parse_score(score) * weights[category] * 20 for category, score in scores.items())
                scaled_score = (weighted_scores / max_possible_score) * 100
                entry['total_score'] = min(scaled_score, 100)  # Ensure score does not exceed 100
        return data
    except IOError:
        print(f"Error reading file: {filename}")
        return []


def decide_and_process(filename):
    """ Decide the processing method based on the content type inferred from the filename. """
    # Open the file to inspect the scores
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        # Determine if scores are numeric by checking if any entry has a non-numeric score
        if all(isinstance(score, (int, float)) or score.isdigit() for entry in data for score in entry['scores'].values()):
            # Extract all numeric scores from the data
            all_scores = [float(score) for entry in data for score in entry['scores'].values() if score.isdigit()]

            # Determine processing method based on the maximum score present
            max_score = max(all_scores, default=0)  # Use default=0 to handle empty data gracefully

            if max_score <= 5:
                # Treat as numeric and nonweighted
                filename += "_nonweighted"  # Append to filename to influence processing in process_scores_numeric
                return process_scores_numeric(filename)
            elif max_score == 6:
                # Treat as numeric and weighted
                filename += "_weighted"  # Append to filename to influence processing in process_scores_numeric
                return process_scores_numeric(filename)
        else:
            # If any scores are not numeric, use text processing
            return process_scores_text(filename)

    except IOError:
        print(f"Error reading file: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {filename}")
        return []


def load_and_scale_data(manual_scores, model_scores):
    """Normalize manual and model scores using StandardScaler"""
    scaler = StandardScaler()
    scores = np.array(manual_scores + model_scores).reshape(-1, 1)
    scaled_scores = scaler.fit_transform(scores)
    return scaled_scores[:len(manual_scores)], scaled_scores[len(manual_scores):]


def calculate_metrics(manual_scores, model_scores):
    """Calculate R-squared, MSE, and MAE for provided scores"""
    rsquared = r2_score(manual_scores, model_scores)
    mse = mean_squared_error(manual_scores, model_scores)
    mae = mean_absolute_error(manual_scores, model_scores)
    return rsquared, mse, mae


# Iterate over possible complexities
max_complexity = 6  # Define maximum number of folders
results = []

for complexity in range(1, max_complexity + 1):
    directory_path = os.path.join(base_directory_path, f'complexity{complexity}/results_final')

    if not os.path.exists(directory_path):
        print(f"Directory does not exist: {directory_path}")
        continue  # Skip this complexity level if the directory does not exist

    all_data = []
    manual_scores = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            if 'manual' in filename:  # Treat 'manual' files as 'text'
                processed_data = process_scores_text(file_path)  # Use text processing for manual scores
                manual_scores.extend([d['total_score'] for d in processed_data])  # Populate manual_scores
                all_data.append(processed_data)
            elif 'text' in filename:
                processed_data = process_scores_text(file_path)
                all_data.append(processed_data)
            elif 'numeric' in filename:
                processed_data = process_scores_numeric(file_path)
                all_data.append(processed_data)
            elif 'taskonly' in filename or 'text' in filename or 'numeric' in filename:
                processed_data = decide_and_process(file_path)
                all_data.append(processed_data)

    total_scores_data = []

    for data in all_data:
        if data:
            for entry in data:
                total_scores_data.append({
                    'modelname': entry['modelname'],
                    'rubricfilename': entry['rubricfilename'],
                    'assessmentfilename': entry['assessmentfilename'],
                    'total_score': entry['total_score']
                })

    # Create a pandas DataFrame from the total scores data
    total_scores_df = pd.DataFrame(total_scores_data)

    # Save the DataFrame to an Excel file
    total_scores_filepath = os.path.join(directory_path, 'totalscores.xlsx')
    total_scores_df.to_excel(total_scores_filepath, index=False)

    # R-squared calculations
    results = []
    for data in all_data:
        if data and 'modelname' in data[0]:
            model_scores = [d['total_score'] for d in data]
            if len(manual_scores) >= len(model_scores):
                scaled_manual_scores, scaled_model_scores = load_and_scale_data(manual_scores[:len(model_scores)], model_scores)
                rsquared, mse, mae = calculate_metrics(scaled_manual_scores, scaled_model_scores)
                results.append({
                    'modelname': data[0]['modelname'],
                    'rubricfilename': data[0]['rubricfilename'],
                    'rsquared': rsquared,
                    'mse': mse,
                    'mae': mae
                })

    # Output metrics for each model
    for result in results:
        print(f"Model: {result['modelname']}, Rubric: {result['rubricfilename']}, R^2: {result['rsquared']}, MSE: {result['mse']}, MAE: {result['mae']}")

    # Save evaluation scores to .xlsx
    df = pd.DataFrame(results)
    df = df[['modelname', 'rubricfilename', 'rsquared', 'mse', 'mae']]
    excel_filepath = os.path.join(directory_path, 'evaluation_scores.xlsx')
    df.to_excel(excel_filepath, index=False)

    # Plotly plotting
    traces = []

    # Plot manual scores against themselves for baseline
    traces.append(go.Scatter(
        x=manual_scores,
        y=manual_scores,
        mode='lines',
        name='Manual (Baseline)',
        text=['Manual'] * len(manual_scores)
    ))

    # Plot other models against manual total scores
    for data in all_data:
        if data:
            # Ensure that `manual_scores` length matches the data length for plotting
            x = manual_scores[:len(data)]
            y = [d['total_score'] for d in data]
            hover_text = [f'Model: {d["modelname"]}, Rubric: {d["rubricfilename"]}, Script: {d["assessmentfilename"]}' for d in data]
            name = f"{data[0]['modelname']} ({data[0]['rubricfilename']})"
            mode = 'markers'

            # Modify hover text to include other overlapping points
            for i, (xi, yi) in enumerate(zip(x, y)):
                overlap_indices = [j for j, (xj, yj) in enumerate(zip(x, y)) if xi == xj and yi == yj and j != i]
                if overlap_indices:
                    hover_text[i] += "<br> Overlapping points:"
                    for index in overlap_indices:
                        hover_text[i] += f"<br> - {name}: {y[index]}, Script: {data[index]['assessmentfilename']}"

            traces.append(go.Scatter(
                x=x,
                y=y,
                mode=mode,
                name=name,
                text=hover_text,
                hoverinfo='text'
            ))

    layout = go.Layout(
        title='Comparison of Model Scores Against Manual Total Scores',
        xaxis=dict(title='Manual Total Scores'),
        yaxis=dict(title='Model Total Scores'),
        hovermode='closest'
    )

    fig = go.Figure(data=traces, layout=layout)
    plot_filename = os.path.join(directory_path, 'interactive_plot.html')
    plot(fig, filename=plot_filename, auto_open=True)


# To run:
# python plot_rsquared.py --scripts
# or
# python plot_rsquared.py --short_answers

# Example usage:
# Evaluate script-based assessments:
# python plot_rsquared.py --scripts

# Evaluate short answer-based assessments:
# python plot_rsquared.py --short_answers
