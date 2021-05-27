import bs4
import requests
import spotipy

import os
import dotenv

dotenv.load_dotenv()

song_uris = ['spotify:track:6NuJs9MZyl5WoUpGubSe4c', 'spotify:track:6fA7akEuTUL3dW1V0GELaZ',
             'spotify:track:2AW37v0bDyuOzGP3XnmFuA', 'spotify:track:3bAzkiGUK53jOG4T4UH0zX',
             'spotify:track:6HDvYZN8OPkkR5gYDtGrue', 'spotify:track:1m2xMsxbtxv21Brome189p',
             'spotify:track:0CbMZFewhr0Zi0FqGE3Oh9', 'spotify:track:3mNecsYFb6LQg7822DPXCP',
             'spotify:track:3aggzBl59puBLxg6ktaqie', 'spotify:track:6KqiVlOLfDzJViJVAPym1p',
             'spotify:track:5zn1hpm9N0ylKB7kOtpCw2', 'spotify:track:7f1Dmr246cJ9uQYdbplTbh',
             'spotify:track:1PmHkalaUHhh0fz23SBHDL', 'spotify:track:4D6bsg0MqGF0PIZLgDydWp',
             'spotify:track:6dJ2mSRaKE9ctYw9qWNGWQ', 'spotify:track:6ZOBP3NvffbU4SZcrnt1k6',
             'spotify:track:4v21wU2Ynm9KYeQBCIJm8U', 'spotify:track:1NNDZc9BHaWe9JqIsPRlNV',
             'spotify:track:4jIgNRzwUAQCctDDM3Kxd4', 'spotify:track:4cySS73lItxvQW1bZQYtOE',
             'spotify:track:3rQvHJ2K1g9tnIcL51eEWE', 'spotify:track:4du0TY3NTgvQGlelrBHfDL',
             'spotify:track:2g2GkH3vZHk4lWzBjgQ6nY', 'spotify:track:6ELYOPuCDkYFAVtsYlDY1F',
             'spotify:track:4du0TY3NTgvQGlelrBHfDL', 'spotify:track:0awvg4qIKgoUzKG1LY6Hqg',
             'spotify:track:296XGtH5MeGisqD3uAz6Q6', 'spotify:track:5S0cvScXb33JVpjTiY9Ivi',
             'spotify:track:1raT3L0NJtc10t7xNgHJZ1', 'spotify:track:65B1tEOv5W294uCKbmEcFV',
             'spotify:track:5oa2xWCtW7PhiWwFObeGBu', 'spotify:track:2JQGzPv4OmrNCkkz1W4NZu',
             'spotify:track:2J8sJTFiOdsELIyMX2X9jH', 'spotify:track:0DAVCurdi9ZqkVUKIuikzm',
             'spotify:track:0YVkQJFhdOSApmpPT6fl4z', 'spotify:track:52TV6XQPs8wijQZLJTdwVl',
             'spotify:track:2fzykVsO2Di5jnofUNX3YE', 'spotify:track:5PWbnMKUTDT4ybZD4mkT0f',
             'spotify:track:4WP1XJnAUkZfTtMdZTaN9k', 'spotify:track:3ZdA3QuqHqOJdsczRwT1hg',
             'spotify:track:1amlgIcPm6vgARnIzGG8K4', 'spotify:track:1TwVcKR6JojvPwBGbWZT36',
             'spotify:track:5J3JWlXEvTkuGyGhUpb2qD', 'spotify:track:3yfqSUWxFvZELEM4PmlwIR',
             'spotify:track:38buCDomzeOx85MeoDJgQ7', 'spotify:track:6kD36kVRn5leDDbjXpHQY0',
             'spotify:track:1bOUi73vKpUIfZbP6QzpXQ', 'spotify:track:4E5rL7YL0hVUPqeMSpjEF2',
             'spotify:track:549DBe4tw3IYPnedaz0q0J', 'spotify:track:4gM2BugovNf4bvXdjZODzG',
             'spotify:track:0io6VQqmCT8Yz1faAqBUFh', 'spotify:track:114ZIcx0S3gJkZmT3wmGte',
             'spotify:track:4BLWSqwIMKhtzqOiHc5V5r', 'spotify:track:6tFOl0bzsNRc6kGunht2VQ',
             'spotify:track:2TTYIwTM2iLC1YOyHuhRMt', 'spotify:track:229lOqe1FCzeSybDYHXMod',
             'spotify:track:3PuoEoC2QYXUJPk1DObFsU', 'spotify:track:0v1XpBHnsbkCn7iJ9Ucr1l',
             'spotify:track:5bH5uk3A1Y9Aky75Akkdvg', 'spotify:track:6GOma2yytypEqT5omVQ5mk',
             'spotify:track:4YLI2hVQu66q23ScZKFg47', 'spotify:track:0ITfVn3zfzOow3LtR337eQ',
             'spotify:track:1p8Zytmhtg4wdtCHRoL3bm', 'spotify:track:6d98A0VPJB78qopxglnp5D',
             'spotify:track:4tnJTKfVbWkOUiVCEEgp6i', 'spotify:track:54FliVaE2u8yKFfOWJG8Wo',
             'spotify:track:71EMeSBrRJjWMJ314mPayo', 'spotify:track:1H5tvpoApNDxvxDexoaAUo',
             'spotify:track:6naxalmIoLFWR0siv8dnQQ', 'spotify:track:0pMUR7Uvp6vxlbG0qBFvgM',
             'spotify:track:5r6xAztoVWbGkiKTTkswk1', 'spotify:track:1C2Q3AymKS17bw7T5gfq6p',
             'spotify:track:49AafGjLBR5if7lX6pilFs', 'spotify:track:3LqfjCXU1oLcu7XTGBcFFM',
             'spotify:track:635PqgECfFbL0MNLogX7Yv', 'spotify:track:5P05t0BBXPLYxUZbBi4BTg',
             'spotify:track:2rNljPJ1YPRIuP1fyhvn2N', 'spotify:track:3vw9SYwBycWsZof1ExtRwT',
             'spotify:track:5H3B1WtZYGmyOYOXgQltKU', 'spotify:track:2tzf1KhNuANrujMqN10fvF',
             'spotify:track:2v2TCrLcmFLkWZLTHBSVgv', 'spotify:track:5Kb1BTrvG9QLzflX08etmH',
             'spotify:track:4n7yQZmiQyVESOeBvpZiyZ', 'spotify:track:6frPth5B1zneT8EV71ZO0V',
             'spotify:track:1jRzdY7oUBOhrylNtiMtBD', 'spotify:track:0QnFAlSin3Ox9QxWh6xfY9',
             'spotify:track:2h2J06UFc4C2g5tnSgFZ5u', 'spotify:track:0Cjl6YCM4JQSgdg3xaFPxk']
songs_list = ['Incomplete', 'Bent', "It's Gonna Be Me", "Jumpin', Jumpin'", 'Try Again', 'I Wanna Know',
              'Everything You Want', 'Absolutely (Story Of A Girl)', 'Higher', "Doesn't Really Matter", 'I Need You',
              'No More', "He Wasn't Man Enough", "Let's Get Married", 'Back Here', 'There You Go',
              '(Hot S**t) Country Grammar', 'Kryptonite', 'Desert Rose', 'Wifey', "I Think I'm In Love With You",
              'You Sang To Me', 'Breathe', 'I Wanna Be With You', 'Wonderful', "What'Chu Like", 'The Next Episode',
              'Be With You', 'I Turn To You', "That's The Way", 'Separated', 'I Will Love Again', 'I Hope You Dance',
              'What About Now', "Big Pimpin'", 'Smooth', 'Purest Of Pain (A Puro Dolor)', "Prayin' For Daylight",
              'It Must Be Love', 'I Try', 'Music', 'Where I Wanna Be', 'Faded', 'One Voice', 'Amazed', 'Dance Tonight',
              'Come On Over Baby (All I Want Is You)', 'Whatever', 'The Real Slim Shady', 'Flowers On The Wall',
              'Just Be A Man About It', 'Simple Kind Of Life', 'Yes!', 'Could I Have This Kiss Forever', 'The Light',
              'Swear It Again', "Callin' Me", 'Taking You Home', 'I Will...But', "I'll Be", 'Lucky', 'What You Want',
              'Change Your Mind', "It's My Life", 'No Matter What They Say', "Don't Think I'm Not", 'Your Everything',
              "You'll Always Be Loved By Me", 'Last Resort', 'Cold Day In July', 'As We Lay', 'Californication',
              'Crash And Burn', 'Broadway', 'Treat Her Like A Lady', 'Who Let The Dogs Out', 'Oops!...I Did It Again',
              'Country Comes To Town', 'Better Off Alone', 'When You Need My Love', "It's Always Somethin'",
              'Dance With Me', "Let's Make Love", 'West Side Story', 'Most Girls', 'With Arms Wide Open', 'Sour Girl',
              'I Disappear', 'I Think God Can Explain', 'The One', 'Same Script, Different Cast', "Don't Call Me Baby",
              'Some Things Never Change', 'The Chain Of Love', 'Got It All', 'Wobble Wobble', 'Shake Ya Ass',
              'Hey Papi', 'Imagine That', 'Ta Da']


sp_client_id = os.getenv('CLIENT_ID')
sp_client_key = os.getenv('CLIENT_KEY')
redirect_uri = 'http://localhost'
#
# billboard = "https://www.billboard.com/charts/hot-100/"
date_year = input(f"Where would you like to travel?\nType the date "
                  f"YYYY-MM-DD: ")
date_month = input(f"Month in Numbers: ")
date_day = input(f"Day in Numbers: ")

# url = f"{billboard}{date_year}-{date_month}-{date_day}"
# print(url)
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
print(user_id)

# song_uris = []


# for song in songs_list:
#     result = sp.search(f"track:{song} year:{date_year}", type='track')
#     # print(result)
#     try:
#         uri = result['tracks']['items'][0]['uri']
#         song_uris.append(uri)
#     except IndexError:
#         print(f"Track \"{song}\" doesn't exist in Spotify. Skipped")

# print(song_uris)
print(len(song_uris))

# playlist = sp.user_playlist_create(
#     user=user_id,
#     name=f"{date_year}-{date_month}-{date_day} BillBoard 100",
#     description=f"Top 100 songs from the year {date_year}"
# )
#
# print(playlist['id'])
#
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

playlist_EP = f"https://api.spotify.com/v1/users/{user_id}/playlists"
header_playlist = {
    'Authorization': 'Bearer BQCiUsPebj7biFiu4_Oo_mixnE7NW2c-Y_C5nIOGg34PrgmlLv7ja-SoEt8xJKP9xSRBlZOcJcdP1Byd8tQwkR0L4EvWbIYr7iPfxiKAwjgl5YAGwUiZVerTg-VVK3xPAPivNCJJ53Ox9A6OnqeVbWDqY5uW8b3ebNx7tdMlyOZhx8ddtH86XTvPSW_fzYM'
}

create_pl_parameters = {
    'name': f"{date_year}-{date_month}-{date_day} BillBoard 100",
    'public': False,
    'description': f"Top 100 songs from the year {date_year}"
}


pl_response = requests.post(
    url=playlist_EP,
    headers=header_playlist,
    json=create_pl_parameters
)

print(pl_response.status_code)
print(pl_response.text)
