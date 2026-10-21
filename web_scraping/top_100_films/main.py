import requests
from bs4 import BeautifulSoup

empires_response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(empires_response.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movies_list = []

for movie in all_movies:
    movies_list.append(movie.string)

with open("movies.txt", mode="w") as file:
    for movie in range(len(movies_list) - 1, -1, -1):
        file.write(f"{movies_list[movie]}\n")
