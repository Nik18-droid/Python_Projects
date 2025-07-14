import requests


def get_company_news(api_key: str, company_name: str):
    """
    Fetches the latest news headlines for a specific company using the NewsAPI.

    This function connects to the NewsAPI 'everything' endpoint, retrieves the
    top 5 most recent English-language articles for a given company name,
    and prints their titles to the console.

    Args:
        api_key (str): Your personal API key from NewsAPI.org.
        company_name (str): The name of the company to search for (e.g., "Apple").
    """
    API_URL = "https://newsapi.org/v2/everything"

    params = {
        'q': company_name,
        'sortBy': 'publishedAt',
        'language': 'en',
        'apiKey': api_key
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)

        data = response.json()
        articles = data.get('articles', [])

        if not articles:
            print(f"No news articles found for '{company_name}'.")
            return

        print(f"--- Latest News for {company_name} ---")
        for article in articles[:5]:
            print(f"- {article['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to the news service. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # It's recommended to use environment variables for API keys in production,
    # but this is fine for a personal project.
    MY_API_KEY = "17313a8c325843b89b3d5d42d406a43e"
    COMPANY_TO_SEARCH = "Broadcom"

    if MY_API_KEY == "YOUR_API_KEY_HERE":
        print("Please replace 'YOUR_API_KEY_HERE' with your actual NewsAPI key.")
    else:
        get_company_news(MY_API_KEY, COMPANY_TO_SEARCH)
