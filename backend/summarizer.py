import openai
import logging

#openai.api_key = "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" 
openai.api_key = "***REMOVED***"

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
