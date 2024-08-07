import qdrant_client  # Client for Qdrant, a vector database
import google.generativeai as genai  # Generative AI library for Gemini API
from qdrant_client import QdrantClient  # Qdrant client for interacting with Qdrant database
from config.settings import genaimodel
from services.getreleventText import generate_context



def generate_answer(question: str, collection_name, qdrant_client: QdrantClient) -> str:
    try:
        # Call the generate_context function to get the context
        context = generate_context(question, collection_name, qdrant_client)

        prompt_parts = [
        "You are a helpful assistant for Gigalogy Company, dedicated to providing accurate and relevant information within the context provided. "
        "Please aim for answers between 200-1000 words, prioritizing helpfulness and accuracy. If the answer is not found in the context, politely indicate that the question is beyond the scope of the provided context. "
        "If the question is about an endpoint or anything related to an endpoint, provide all relevant endpoint details in the following format: \n"
        "Endpoint: \n"
        "HTTP Method: \n"
        "Description: \n"
        "Parameters: \n"
        "Response Codes: \n\n"
        "When answering any other questions, carefully review the provided context and extract the most relevant information to generate a complete and accurate response.",
        f"context: {context}",
        "input: ",
        "output: "
    ]
        

        print(context)
        
        response = genaimodel.generate_content(prompt_parts)
        
        # ------------
                
        # t_model = tuned_model
        # response = t_model.generate_content(metaprompt)

        # # Remove markdown syntax from the response text
        # response_text = response.text.replace("**", "").replace("*", "").replace("`", "")

        # # Replace double newlines with single newline
        # response_text = response_text.replace("\n\n", "\n")

        # # Remove extra spaces and leading/trailing spaces
        # response_text = response_text.strip()

        print(response.text)
        return response.text
    
    except Exception as e:
        # Handle any errors that occur during the execution
        print(f"An error occurred while generating answer: {str(e)}")
        return ""


    

