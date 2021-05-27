
import bs4
import requests
import spotipy

import os
import dotenv
dotenv.load_dotenv()


sp_client_id = os.getenv('CLIENT_ID')
sp_client_key = os.getenv('CLIENT_KEY')
redirect_uri = 'http://localhost'

# billboard = "https://www.billboard.com/charts/hot-100/"
# date = input(f"Where would you like to travel?\nType the date "
#              f"YYYY-MM-DD: ")
#
# url = f"{billboard}{date}"
# # print(url)
#
# # data = open('data.html')
#
# response = requests.get(url)
# print(response.status_code)
# # print(response.text)
#
#
# soup = bs4.BeautifulSoup(response.text, 'html.parser')
# songs = soup.find_all('span', class_='chart-element__information__song')
# # print(len(songs))
#
# songs_list = [song.text for song in songs]
#
# print(songs_list)

sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=redirect_uri,
        client_id=sp_client_id,
        client_secret=sp_client_key,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

print(sp.current_user())

