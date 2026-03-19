import requests

def fetch_market_data(sector: str):
    try:
        url = f"https://newsapi.org/v2/everything?q={sector}+india&apiKey=YOUR_NEWS_API"
        res = requests.get(url)
        data = res.json()

        articles = []
        for article in data.get("articles", [])[:5]:
            articles.append(article["title"])

        return "\n".join(articles)

    except:
        return "No real-time data available"
        