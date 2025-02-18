# Import necessary libraries
import os
from dotenv import load_dotenv  # Load environment variables from .env file
load_dotenv()

import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For web scraping
import spotipy  # Spotify API wrapper
from spotipy import SpotifyOAuth  # For Spotify authentication

# ------------------------ User Input: Select Year ------------------------
# Prompt user to input a specific year in YYYY-MM-DD format
search_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = search_year.split("-")[0]  # Extract only the year

# Load Spotify credentials from environment variables
susername = os.getenv("SPOTIPY_USERNAME")

# Define request headers for web scraping (to mimic a real browser)
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Billboard URL for the selected year
url = "https://www.billboard.com/charts/hot-100/" + search_year

# ------------------------ Web Scraping Billboard Top 100 Songs ------------------------
response = requests.get(url, header)  # Send request to Billboard Hot 100 page
soup = BeautifulSoup(response.text, "html.parser")  # Parse the page content

# Find all song entries on the Billboard Hot 100 chart
song_names_spans = soup.find_all("div", class_="o-chart-results-list-row-container")

# ------------------------ Spotify Authentication ------------------------
# Authenticate with Spotify API using OAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # Scope to modify private playlists
        redirect_uri="http://example.com",  # Redirect URI for authentication
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),  # Spotify Client ID
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),  # Spotify Client Secret
        show_dialog=True,  # Prompt user for authentication
        cache_path="token.txt",  # Cache token for reuse
        username=susername,  # Spotify username
    )
)

# Get the current Spotify user's ID
user_id = sp.current_user()["id"]

# ------------------------ Searching for Songs on Spotify ------------------------
song_uris = []  # List to store Spotify URIs of songs

for song in song_names_spans:
    if song and song.find("h3"):  # Check if song entry is valid
        title = song.find("h3").get_text(strip=True)  # Extract song title
        result = sp.search(q=title, type='track')  # Search for song on Spotify

        if result['tracks']['items']:  # If a match is found
            song_uri = result['tracks']['items'][0]['uri']  # Get song URI
            song_uris.append(song_uri)  # Add to list
        else:
            print(f"Song {title} not found on Spotify")  # Log missing songs

# ------------------------ Creating a New Playlist on Spotify ------------------------
playlist_name = f"Billboard Hot 100 - {year}"  # Playlist name
description = "Top 100 songs on Billboard charts for the specified year."  # Playlist description

# Create a new private playlist on Spotify
playlist = sp.user_playlist_create(user=user_id,
                                   name=playlist_name,
                                   description=description,
                                   public=False)

# ------------------------ Adding Songs to Playlist ------------------------
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# ------------------------ OAuth Explanation ------------------------
# Spotify uses OAuth (Open Authorization) to grant third-party applications access
# to user accounts securely without exposing credentials.
# This implementation allows us to authenticate and manage Spotify playlists
# programmatically using OAuth tokens.

print(f"Playlist '{playlist_name}' created successfully with {len(song_uris)} songs!")
