import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    """
    Fetches content from the given URL.
    Returns the text content from <p> tags if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return None

if __name__ == "__main__":
    test_url = "https://medium.com/womenintechnology/the-great-tech-job-migration-is-upon-us-60740e91e570"  # Replace with a real blog URL
    content = fetch_content(test_url)
    print(content)
