import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

@tool
def get_news():
  """This function scrapes news headlines"""

  try:
    url = "https://www.bbc.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all h2 tags with data-test id= "card-headline" 
    headline_tags = soup.find_all("h2", attrs={"data-testid": "card-headline"})

    # Extract text from each tag
    headlines = [tag.get_text(strip=True) for tag in headline_tags]

    # Remove any duplicates
    unique_headlines = list(dict.fromkeys(headlines))

    return unique_headlines
  
  except Exception as E:
    print("There was an error... " + E)