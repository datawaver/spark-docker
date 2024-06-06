import requests
from bs4 import BeautifulSoup


def fetch_covid_cases():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    cases = soup.find_all("div", class_="maincounter-number")
    total_cases = cases[0].text.strip().replace(",", "")
    return int(total_cases)
