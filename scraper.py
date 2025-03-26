import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        for script in soup(["script", "style", "noscript"]):
            script.decompose()

        text = soup.get_text(separator=' ')
        lines = [line.strip() for line in text.splitlines()]
        return " ".join(line for line in lines if line)
    except Exception as e:
        return f"Error fetching URL: {e}"

