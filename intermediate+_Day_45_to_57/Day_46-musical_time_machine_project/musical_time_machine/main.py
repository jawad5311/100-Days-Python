
import bs4
import requests


billboard = "https://www.billboard.com/charts/hot-100/"

date = input(f"Where would you like to travel?\nType the date"
             f"YYYY-MM-DD: ")

url = f"{billboard}{date}"
# print(url)

# data = open('data.html')

response = requests.get(url)
print(response.status_code)
# print(response.text)


soup = bs4.BeautifulSoup(response.text, 'html.parser')
songs = soup.find_all('span', class_='chart-element__information__song')
# print(len(songs))

songs_list = [song.text for song in songs]

print(songs_list)








