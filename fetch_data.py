import requests
from bs4 import BeautifulSoup
import tweepy
def fetch_cert_in():
    url = "https://www.cert-in.org.in/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    alerts = soup.find_all("marquee")  # Adjust based on structure

    for alert in alerts:
        data = {"source": "CERT-In", "type": "Advisory", "details": alert.text.strip()}
        print(data)  # Print the fetched data instead of inserting into MongoDB

def fetch_abuse_ipdb():
    API_KEY = "your_api_key"
    url = "https://api.abuseipdb.com/api/v2/reports"
    headers = {"Accept": "application/json", "Key": API_KEY}
    
    response = requests.get(url, headers=headers).json()
    for report in response["data"]:
        print({"source": "AbuseIPDB", "type": "Malicious IP", "details": report["ipAddress"]})  # Print the fetched data

def fetch_twitter():
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_SECRET = "your_access_secret"

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    tweets = api.search_tweets(q="cyber attack India", count=5)
    for tweet in tweets:
        print({"source": "Twitter", "type": "Threat Alert", "details": tweet.text})  # Print the fetched data

def fetch_threats():
    fetch_cert_in()
    fetch_abuse_ipdb()
    fetch_twitter()
    return "Fetched data successfully!"
