# ---------------------------------------------------------
# Python script for initializing clients
# for interacting with Ollama and OpenAI APIs.
#
# This script includes functions to setup and configure
# clients to use the services provided by Ollama and OpenAI.
# The OpenAI client is specifically configured with an API key.
#
# Author: Christopher Vishnu Kumar
# Date: 07/05/2024
# ---------------------------------------------------------

# Third-party imports
import ollama
import openai


def initialize_clients(openai_key):
    """
    Initialize and configure clients for both the Ollama and OpenAI services.

    This function sets up client instances for interacting with Ollama and OpenAI APIs.
    It configures the OpenAI client with the provided API key.

    Parameters:
    - openai_key (str): The API key for authenticating with the OpenAI service.

    Returns:
    - tuple: A tuple containing the initialized Ollama client and the configured OpenAI client.
    """
    # Create an instance of the Ollama client.
    client = ollama.Client()

    # Assign the provided API key to the OpenAI client configuration.
    openai.api_key = openai_key

    # Output a message to confirm initialization.
    print("Initialized Ollama and OpenAI clients.")

    # Return the instances of both clients.
    return client, openai
