from bs4 import BeautifulSoup
import requests

def scrape_weather_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Replace the following line with the actual scraping logic for the website you're targeting
    weather_data = soup.find_all('div', class_='weather')

    return weather_data
