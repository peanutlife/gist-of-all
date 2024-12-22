from dotenv import load_dotenv
import openai
import logging

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)



def summarize_text(content, keywords):
    """
    Summarizes the given content focusing on the provided keywords.
    """
    logging.info("Received request for summarization")
    try:
        prompt = f"Summarize the following content focusing on these keywords: {', '.join(keywords)}.\n\nContent:\n{content[:2000]}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use 'gpt-4' if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Error in summarization."
