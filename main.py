# -----------------------------------------------------------------------------------
# Assessment Script Runner
# -----------------------------------------------------------------------------------
# Description:
#     This script facilitates the assessment of various models, handling scripts or short answers
#     based on provided inputs. It leverages command line arguments for specifying directories
#     and models, uses environment variables for API keys, and performs file I/O operations.
#     Results are systematically generated and stored in a designated output directory.
#
# Author: Christopher Vishnu Kumar
# Date: 07/05/2024
#
# Usage:
#     To run script-based assessments:
#         python main.py --scripts --m MODELS [MODELS ...] -d DIRECTORY
#     To run short-answer assessments:
#         python main.py --short_answers --m MODELS [MODELS ...] -d DIRECTORY
#
# Example:
#     python main.py --scripts -m gpt-3.5-turbo mistral-7b-instruct-v0.2 -d 1
#     python main.py --short_answers -m gpt-3.5-turbo mistral-7b-instruct-v0.2 -d a
#
# Models used:
#     Ollama:
#       gemma, llama2, llama3, mistral, mistral-7b-instruct-v0.2, wizardlm2
#     OpenAI:
#       gpt-3.5-turbo, gpt-4-turbo-preview, gpt-4
# -----------------------------------------------------------------------------------

# Standard library imports
import os
# import time
import argparse
import json

# Third-party imports
from dotenv import load_dotenv

# Local application imports
from clients import initialize_clients
from utils import set_mode, read_file, natural_sort_key, format_response, unload_model

# Load environment variables
load_dotenv()


def main():
    """
    Main function to run assessment scripts or short answers on specified models.
    Parses command-line arguments to define the operational mode, directories, and models.
    Initializes API clients using an API key and manages the workflow of processing and output generation.
    """

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Run assessment scripts/shortanswers on various models.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--scripts', action='store_true', help='Select script processing mode.')
    group.add_argument('--short_answers', action='store_true', help='Select short answers processing mode.')
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory number (1-6) or "a" for all directories.')
    parser.add_argument('-m', '--models', nargs='+', required=True, help='List of models to process.')
    args = parser.parse_args()

    # Set the mode based on the input arguments
    set_mode('scripts' if args.scripts else 'short_answers')

    # Determine the directories to process
    if args.short_answers:
        directories = ['1', '2', '3', '4', '5'] if args.directory == 'a' else [args.directory]
        data_type = "short_answers"
    elif args.scripts:
        directories = ['1', '2', '3', '4', '5', '6'] if args.directory == 'a' else [args.directory]
        data_type = "scripts"

    base_path = "C:/Users/u1092815/Desktop/LLMassessment/testdata-{}/complexity{}"
    system_prompt_base = "C:/Users/your-user/Desktop/LLMassessment/testdata-{}/systemprompt.txt"

    # Initialize API clients with the environment variable for the OpenAI key (Currently hard coded API key)
    openai_key = os.environ.get('OPENAI_API_KEY', 'your-api-key-here')
    ollama_client, openai_client = initialize_clients(openai_key)

    # Define synonyms for assessment scores
    score_synonyms = {
        # Define synonyms for various score levels
        "Poor": ["Bad", "Subpar", "Inferior", "Lacking", "Insufficient"],
        "OK": ["Acceptable", "Fair", "Decent", "Satisfactory", "Minimal"],
        "Competent": ["Capable", "Adequate", "Proficient", "Effective"],
        "Excellent": ["Outstanding", "Superior", "Exceptional"],
        "Perfect": ["Flawless", "Impeccable", "Ideal"]
    }

    # Process each directory specified
    for dir_number in directories:
        base_dir = base_path.format(data_type, dir_number)
        assessments_dir = os.path.join(base_dir, data_type)
        rubrics_dir = os.path.join(base_dir, "rubrics")
        system_prompt_file = system_prompt_base.format(data_type)
        output_dir = os.path.join(base_dir, "results_final")

        # Create results directory if it does not exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Read and extract task name from system prompt
        system_prompt = read_file(system_prompt_file)
        task_name = os.path.basename(os.path.dirname(assessments_dir))

        for model_name in args.models:
            rubric_files = sorted(os.listdir(rubrics_dir), key=natural_sort_key)
            for rubric_filename in rubric_files:
                rubric_base = rubric_filename.replace('.txt', '')
                output_file_path = os.path.join(output_dir, f'{task_name}_{model_name}_{rubric_base}.json')
                print(f"Starting processing for model {model_name} with rubric {rubric_filename}.")

                responses = []
                rubric_content = read_file(os.path.join(rubrics_dir, rubric_filename))
                assessment_files = sorted(os.listdir(assessments_dir), key=natural_sort_key)

                for assessment_filename in assessment_files:
                    assessment_content = read_file(os.path.join(assessments_dir, assessment_filename))
                    print(f"Processing {assessment_filename} with {model_name}.")
                    prompt = f"{rubric_content}\n{assessment_content}"

                    # Call model API based on model type
                    if model_name.startswith("gpt"):
                        # time.sleep(0.7)  # Artificial delay for GPT models
                        response = openai_client.chat.completions.create(
                            model=model_name,
                            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
                            seed=1,
                            temperature=0.2,
                            # response_format={"type": "json_object"}

                        )
                        response_content = response.choices[0].message.content
                    else:
                        response = ollama_client.chat(
                            model=model_name,
                            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
                            options={
                                'seed': 1,
                                'temperature': 0.2,
                                'num_predict': 2048,  # workaround for issue: "https://github.com/ollama/ollama/issues/1863"
                                # "format": "json"
                            }
                        )
                        response_content = response.get('message', {}).get('content', '')
                        unload_model(model_name)

                    # Format and record response
                    response_data = format_response(response_content, model_name, rubric_filename, assessment_filename, score_synonyms)
                    responses.append(response_data)

                    print(f"Completed processing {assessment_filename} with {model_name}.")

                # Write all responses for this model and rubric to a JSON file
                with open(output_file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(responses, json_file, indent=4)

                print(f"Completed all processing for model {model_name} with rubric {rubric_filename}.")

    print("All processing completed.")


if __name__ == "__main__":
    main()

# Command to put the computer into sleep mode after processing
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
