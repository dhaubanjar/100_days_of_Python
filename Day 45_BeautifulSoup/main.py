# Code that scrap website for TOp 100 movies of all time
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")
movie_names = soup.find_all("span", class_ = "content_content__i0P3p")
with open("movie_names.txt", "w") as file:  # creates a .txt file
    for movie in movie_names[:2:-1]:    # gets items of list from last excluding two [start:stop:step]
        if movie and movie.find('h2'):
            title = movie.find('h2').get_text(strip=True)
            file.write(f"{title}\n")    # writes inside the txt file