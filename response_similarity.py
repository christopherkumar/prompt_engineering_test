# ---------------------------------------------------------
# Response Similarity Analysis Tool
# ---------------------------------------------------------
# This script calculates the similarity of responses to assessment standards,
# supporting both script-based and short-answer assessments. It leverages
# edit distance to measure similarity and outputs the results to an Excel file.
#
# Usage:
#     python response_similarity.py --scripts|--short_answers
#
# Example:
#     Evaluate script-based assessments:
#     python response_similarity.py --scripts
#
#     Evaluate short answer-based assessments:
#     python response_similarity.py --short_answers
#
# Author: Christopher Vishnu Kumar
# Date: 07/05/2024
# ---------------------------------------------------------

# Standard library imports
import json
import os
import argparse

# Third-party imports
import pandas as pd
from nltk.metrics import edit_distance

# Define command-line arguments
parser = argparse.ArgumentParser(description='Calculate response similarity based on the selected mode.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--scripts', action='store_true', help='Calculate similarity for script-based assessments.')
group.add_argument('--short_answers', action='store_true', help='Calculate similarity for short answer assessments.')
args = parser.parse_args()

# Define the base directory based on the selected mode
if args.scripts:
    base_directory = "C:\\path\\to\\your\\testdata-scripts"
    max_range = 7
    score_keys = ['Functionality', 'Logic', 'Code Quality', 'User Input Handling', 'Documentation']
elif args.short_answers:
    base_directory = "C:\\path\\to\\your\\testdata-short_answers"
    max_range = 5
    score_keys = ['Understanding of the Topic', 'Argumentation and Evidence', 'Organization and Clarity']


def format_desired_response(scores):
    """
    Generate a formatted response string based on the assessment scores.

    Parameters:
        scores (dict): A dictionary containing score categories and their respective values.

    Returns:
        str: A formatted string listing each score category with its value.
    """
    return ', '.join([f"{key}: {scores[key]}" for key in score_keys])


def compute_similarity(response1, response2):
    """
    Compute the similarity between two responses using the normalized edit distance.

    Parameters:
        response1 (str): The first response string.
        response2 (str): The second response string.

    Returns:
        float: The similarity score ranging from 0 (no similarity) to 1 (identical).
    """
    return 1 - (edit_distance(response1, response2) / max(len(response1), len(response2)))


# Create a list to store data for DataFrame
score_data = []

for i in range(1, max_range):  # Iterate through complexities
    directory = os.path.join(base_directory, f"complexity{i}\\results_final")
    for filename in os.listdir(directory):
        if "manual" not in filename and filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as file:
                data = json.load(file)
                if data:  # Check if data is not empty
                    similarities = []
                    # Get model and rubricfilename from the first JSON object
                    model = data[0]['modelname']
                    rubricfilename = data[0]['rubricfilename']
                    for item in data:
                        desired_response = format_desired_response(item['scores'])
                        raw_response = item['raw_response']
                        similarity = compute_similarity(desired_response, raw_response)
                        similarities.append(similarity)
                    if similarities:  # Check if there are any scores collected
                        average_similarity = sum(similarities) / len(similarities)
                        score_data.append([model, rubricfilename, average_similarity])

# Create a DataFrame from the list
df_scores = pd.DataFrame(score_data, columns=['modelname', 'rubricfilename', 'average similarity score'])

# Write the DataFrame to an Excel file
excel_path = os.path.join(base_directory, 'average_similarity_scores.xlsx')
df_scores.to_excel(excel_path, index=False)

print(f"Excel file has been created at {excel_path}")
