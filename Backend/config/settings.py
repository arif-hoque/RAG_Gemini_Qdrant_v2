import os
from dotenv import load_dotenv
import google.generativeai as genai
import google.generativeai as gemini_client
from qdrant_client import QdrantClient
from config.load_creds import load_creds
from google.oauth2.credentials import Credentials  # Add this line

# Load environment variables from .env file
load_dotenv()

# Define the paths to the secret files
GEMINI_API_KEY_FILE = "/run/secrets/gemini_api_key"
QDRANT_URL_FILE = "/run/secrets/qdrant_url"
QDRANT_API_KEY_FILE = "/run/secrets/qdrant_api_key"

# Define the path to token.json
TOKEN_PATH = '/app/config/token.json'

# Read the API keys and other configuration variables from the secret files
with open(GEMINI_API_KEY_FILE, "r") as file:
    GEMINI_API_KEY = file.read().strip()

with open(QDRANT_URL_FILE, "r") as file:
    QDRANT_URL = file.read().strip()

with open(QDRANT_API_KEY_FILE, "r") as file:
    QDRANT_API_KEY = file.read().strip()



def load_creds_with_token_path():
    """Loads credentials from the token.json file."""
    SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        raise Exception("Invalid or missing credentials.")
    return creds

# ---------------------------------------------------------------------
creds = load_creds_with_token_path()
genai.configure(credentials=creds)

# Set up the model
generation_config = {
"temperature": 0.55,
"top_p": 1,
"top_k": 0,
"max_output_tokens": 8192,
}

safety_settings = [
{
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
]

# # Set up the tuned model
# tuned_model_name = 'gigalogychatbottrained-dvj30oqsbpa0'
tuned_model = genai.GenerativeModel(model_name="tunedModels/gigalogychatbottrained-dvj30oqsbpa0",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)
# --------------------------------------------------------------------------------------------------------

# ---------------------------------
# Configure the Gemini API key
# gemini_client.configure(api_key=GEMINI_API_KEY)

# Initialize the generative model for Gemini
genaimodel = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                   generation_config=generation_config,
                                   safety_settings=safety_settings)

# ----------------------------------



# Initialize the Qdrant client
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)
