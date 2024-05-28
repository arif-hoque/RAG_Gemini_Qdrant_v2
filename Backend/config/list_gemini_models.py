import pprint
import google.generativeai as genai
from load_creds import load_creds
from google.auth.transport.requests import Request


def main():
    creds = load_creds()
    genai.configure(credentials=creds)

    # Retrieve the list of available models
    models = genai.list_models()

    # Filter for the base model that supports 'createTunedModel'
    base_model = next((m for m in models if "createTunedModel" in m.supported_generation_methods), None)

    # Print the base model details if found
    if base_model:
        print(base_model)
    else:
        print("No model supporting 'createTunedModel' found.")

    name = f'tuned-gemini-model'

    

if __name__ == '__main__':
    main()
