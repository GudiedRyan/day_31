from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.officialcharts.com/charts/singles-chart/")

top_songs = response.text

soup = BeautifulSoup(markup=top_songs, features="html.parser")

songs = soup.find_all(name="div", class_="title")
artists = soup.find_all(name="div", class_="artist")

title = []
artist = []

for song in songs:
    title.append(song.getText())
for name in artists:
    artist.append(name.getText())

with open("songs.txt", "w") as file:
    for i in range(100):
        file.write(f"{i+1}. {title[i]} by {artist[i]}\n")