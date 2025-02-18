# Scrape Top 100 songs in particular year of choice from Billboard
# Create the list of songs
# Use Spotify API to create the playlist of the list
# pip install spotipy --upgrade
import os
from dotenv import load_dotenv
load_dotenv()
from os.path import split

import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy import SpotifyOAuth

# Declaring variables

search_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = search_year.split("-")[0]
susername = os.getenv("SPOTIPY_USERNAME")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + search_year

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all("div", class_="o-chart-results-list-row-container")
artist_names_spans = soup.find_all("span", class_= "a-no-trucate")


# Create a spotify Client for authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret= os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username= susername,
    )
)
user_id = sp.current_user()["id"]


# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]

song_uris = []
for song in song_names_spans:
    if song and song.find("h3"):
        title = song.find("h3").get_text(strip=True)
        result =  sp.search(q=title, type='track')

        if result['tracks']['items']:
            song_uri = result['tracks']['items'][0]['uri']
            song_uris.append(song_uri)
        else:
            print(f"Song {title} not found on Spotify")

# ------- Creating a new playlist on Spotify -----------
playlist_name = f"Billboard Hot 100 - {year}"
description = "Top 100 songs on Billboard charts for the specified year."

playlist = sp.user_playlist_create(user=user_id,
                                   name=playlist_name,
                                   description=description,
                                   public=False)

# -------- Adding songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items= song_uris)





# OAuth:
# Spotify uses OAuth to allow third-party applications, OAuth is not an API or a service
# It's an open standard for authorization and anyone can implement it



