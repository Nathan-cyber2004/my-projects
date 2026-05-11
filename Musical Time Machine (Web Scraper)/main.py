import requests
from bs4 import BeautifulSoup

# Webscraper Logic
user_choice = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD:- ")
year = user_choice.split('-')[0]

URL = f"https://www.billboard.com/charts/hot-100/2004-04-05/"

response = requests.get(url = URL)
response_text = response.text

soup = BeautifulSoup(response_text, 'html.parser')

song_objects = soup.find_all(name = "h3", class_ = "c-title")
song_filter = [song.getText().strip() for song in song_objects]
all_songs = []

for item in song_filter:
  if (item == 'Songwriter(s):' 
      or item == 'Producer(s):' 
      or item == 'Imprint/Promotion Label:' 
      or item == 'Gains in Weekly Performance' 
      or item == 'Additional Awards'):
    pass

  else:
    all_songs.append(item)

songs = all_songs[1:len(all_songs)-13]

