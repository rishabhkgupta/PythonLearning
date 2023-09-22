
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "tesla"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

ACCOUNT_SID = ''
AUTH_TOKEN = ''

NUMBER = ""
TO_NUMBER = ""

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

daily_stock_data = stock_data["Time Series (Daily)"]

keys = list(daily_stock_data.keys())
first_key = keys[0]
second_key = keys[1]
current = float(daily_stock_data[first_key]["4. close"])
previous = float(daily_stock_data[second_key]["4. close"])

difference = round((current - previous) / previous * 100.0)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(difference) > 5:
    news_parameters = {
        "q": COMPANY_NAME,
        "sortBy":"publishedAt",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formated_articles = [f"{STOCK}:{up_down}{difference}%\nHeadline: {article['title']}.\nbreif: {article['description']}" for article in three_articles]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formated_articles:
        message = client.messages.create(
        from_=NUMBER,
        body=article,
        to=TO_NUMBER
        )
