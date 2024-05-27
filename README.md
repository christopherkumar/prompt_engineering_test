# Prompt Engineering Evaluation
This project was carried out to assess how well Large Language Models (LLMs) were at being able to assess scripts and short answer questions, as a marking aide.

## RESOURCES
- [ollama](https://github.com/ollama/ollama)
- [ollama-python](https://github.com/openai/openai-python)
- [Mistral-7B-Instruct-Q8](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/blob/main/mistral-7b-instruct-v0.2.Q8_0.gguf)
- `ollama create example -f Modelfile`
- [openai](https://platform.openai.com/docs/overview)
- [openai-python](https://github.com/openai/openai-python)

## SCRIPTS
create env => python=3.10.0
install packages => requirements.txt (check if requirements are correct)
### main.py (outline utils.py and clients.py):
Usage:
- `python main.py --scripts --m MODELS [MODELS ...] -d DIRECTORY`
- `python main.py --short_answers --m MODELS [MODELS ...] -d DIRECTORY`
### plot_rsquared.py
Implements total_score calculation, scatter_plots, rsquared_mse_mae
Usage:
  Run with command-line arguments:
  - `--scripts` to process script-based assessments
  - `--short_answers` to process short-answer assessments
### response_similarity
*This script is not important for the required functionality of this project*\
Usage:
  Run with command-line arguments:
  - `--scripts` to process script-based assessments
  - `--short_answers` to process short-answer assessments.py
### collate_graphs.pysage:
*This script is not important for the required functionality of this project*\
  Run with command-line arguments:
  - `python collate_graphs.py`
