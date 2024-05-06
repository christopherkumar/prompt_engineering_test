# ---------------------------------------------------------
# Python script for managing processing modes, reading files,
# normalizing scores, parsing responses, and managing models.
#
# This script contains functions to manage processing modes, file reading, score normalization,
# response parsing, and model management. It uses regular expressions to parse and normalize
# scoring information from text responses according to predefined rubrics. The script also includes
# functionality to manage model states on a server, emphasizing its use in contexts where responses
# from different processing modes (like 'scripts' or 'short_answers') need specific handling.
#
# Author: Christopher Vishnu Kumar
# Date: 07/05/2024
# ---------------------------------------------------------

# Standard library imports
import re
import requests

# Global variable to store the current processing mode
current_mode = None


def set_mode(mode):
    """
    Set the current processing mode ('scripts' or 'short_answers').

    Parameters:
    - mode (str): The processing mode to set.
    """
    global current_mode
    current_mode = mode


def read_file(file_path):
    """
    Read and return the content of a file specified by its path.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()


def natural_sort_key(s):
    """
    Generate a natural sort key for the given string.

    This sort key allows the sorting of strings containing numbers in a way that
    humans might expect ('item2' before 'item10').

    Parameters:
    - s (str): The string to generate the sort key for.

    Returns:
    - list: The natural sort key for the string.
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def normalize_score(score, score_synonyms):
    """
    Normalize a score by converting synonyms or numeric values to a primary score term.

    Parameters:
    - score (str): The score to normalize.
    - score_synonyms (dict): A dictionary of primary scores to lists of synonymous scores.

    Returns:
    - str: The normalized score.
    """
    score = score.strip()
    for primary_score, synonyms in score_synonyms.items():
        if score.lower() in [syn.lower() for syn in synonyms]:
            return primary_score.capitalize()
    try:
        numeric_score = int(float(score))
        return str(numeric_score)
    except ValueError:
        return score.capitalize()


def parse_scores_from_response(raw_response, score_synonyms, rubric_filename):
    """
    Extract scores from a raw response based on the criteria mentioned in the rubric filename.
    Adjusts the pattern based on the current mode ('scripts' or 'short_answers').

    Parameters:
    - raw_response (str): The raw text response from which to parse scores.
    - score_synonyms (dict): Dictionary mapping primary scores to their synonyms.
    - rubric_filename (str): The filename that may suggest the type of scores to look for.

    Returns:
    - dict: A dictionary of criteria and their parsed scores.
    """
    if current_mode == 'scripts':
        if "text" in rubric_filename.lower():
            pattern = re.compile(r"(Functionality|Logic|Code Quality|User Input Handling|Documentation):\s*([a-zA-Z]+)")
        else:
            pattern = re.compile(r"(Functionality|Logic|Code Quality|User Input Handling|Documentation):\s*(\d+)")
    elif current_mode == 'short_answers':
        if "text" in rubric_filename.lower():
            pattern = re.compile(r"(Understanding of the Topic|Argumentation and Evidence|Organization and Clarity):\s*([a-zA-Z]+)")
        else:
            pattern = re.compile(r"(Understanding of the Topic|Argumentation and Evidence|Organization and Clarity):\s*(\d+)")

    scores = {}
    matches = pattern.findall(raw_response)
    for criterion, score in matches:
        if criterion not in scores:
            normalized_score = normalize_score(score, score_synonyms)
            scores[criterion] = normalized_score
    return scores


def parse_response(raw_response, score_synonyms, rubric_filename):
    """
    Parse a raw response into structured scores based on predefined criteria.
    Adjusts the criteria based on the current mode ('scripts' or 'short_answers').

    Parameters:
    - raw_response (str): The raw response to parse.
    - score_synonyms (dict): A dictionary of score synonyms.
    - rubric_filename (str): The filename of the rubric, indicating the scoring format.

    Returns:
    - dict: A dictionary with criteria as keys and normalized scores as values.
    """
    try:
        scores = parse_scores_from_response(raw_response, score_synonyms, rubric_filename)
        if current_mode == 'scripts':
            criteria = {
                "Functionality": "Not found",
                "Logic": "Not found",
                "Code Quality": "Not found",
                "User Input Handling": "Not found",
                "Documentation": "Not found"
            }
        elif current_mode == 'short_answers':
            criteria = {
                "Understanding of the Topic": "Not found",
                "Argumentation and Evidence": "Not found",
                "Organization and Clarity": "Not found",
            }

        for criterion in criteria:
            if criterion in scores:
                criteria[criterion] = scores[criterion]
        return criteria
    except Exception as e:
        print(f"Error parsing response: {e}")
        return None


def format_response(raw_response, model_name, rubric_filename, assessment_filename, score_synonyms):
    """
    Format a raw response into a structured dictionary with model and score details.

    Parameters:
    - raw_response (str): The raw response text to format.
    - model_name (str): The name of the model that generated the response.
    - rubric_filename (str): The filename of the rubric used.
    - assessment_filename (str): The filename of the assessment processed.
    - score_synonyms (dict): A dictionary mapping scores to their synonyms.

    Returns:
    - dict: A dictionary containing the model name, rubric filename, assessment filename, scores, and the raw response.
    """
    scores = parse_response(raw_response, score_synonyms, rubric_filename)
    return {
        "modelname": model_name,
        "rubricfilename": rubric_filename,
        "assessmentfilename": assessment_filename,
        "scores": scores,
        "raw_response": raw_response
    }


def unload_model(model_name):
    """
    Send a request to unload a model from a server.

    Parameters:
    - model_name (str): The name of the model to unload.

    Returns:
    - None
    """
    url = 'http://localhost:11434/api/generate'
    data = {"model": model_name, "keep_alive": 0}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f'Model {model_name} unloaded successfully.')
    else:
        print(f'Failed to unload model {model_name}. Status code: {response.status_code}')
