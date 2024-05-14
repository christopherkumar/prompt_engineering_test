# prompt_engineering_test
This project was carried out to assess how well Large Language Models (LLMs) were at being able to assess scripts and short answer questions, as a marking aide.

## RESOURCES
ollama repo
ollama-python repo
hugging face page for mistral...
create model from .gguf ollama
openai platform docs
openai-python repo

## MY SCRIPTS
create env => python=3.10.0
install packages => requirements.txt (check if requirements are correct)
### main.py (outline utils.py and clients.py):
Usage:
    To run script-based assessments:
        python main.py --scripts --m MODELS [MODELS ...] -d DIRECTORY
   To run short-answer assessments:
        python main.py --short_answers --m MODELS [MODELS ...] -d DIRECTORY
### plot_rsquared.py
#### >> implements total_score calculation, scatter_plots, rsquared_mse_mae 
#### >> ONLY TOTAL_SCORE CALCULATION CARRIED ON, PREVIOUS FUNCTIONALITY STILL PRESENT BUT NOT USED
Usage:
  Run with command-line arguments:
  - `--scripts` to process script-based assessments
  - `--short_answers` to process short-answer assessments
### response_similarity
Usage:
  Run with command-line arguments:
  - `--scripts` to process script-based assessments
  - `--short_answers` to process short-answer assessments.py
### collate_graphs.py
#### >> USABLE FOR .html GRAPHS MADE BY plot_rsquared.py
Usage:
  Run with command-line arguments:
  - python collate_graphs.py
## STATISTICAL ANALYSIS AND PLOTTING NOW DONE USING MATLAB (USE MATLAB IDE)
.m files located in MATLAB working directory
cd('path\to\your\promptengineering_eval.m')
cd('path\to\your\promptengineering_all.m')
move testdata-scripts/scripts-total_scores-final.xlsx to MATLAB working directory
testdata-scripts/short_answers-total_scores-final.xlsx to MATLAB working directory
