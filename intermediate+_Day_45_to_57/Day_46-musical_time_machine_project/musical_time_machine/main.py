import bs4
import requests
import spotipy

import os
import dotenv

dotenv.load_dotenv()

sp_client_id = os.getenv('CLIENT_ID')
sp_client_key = os.getenv('CLIENT_KEY')
redirect_uri = 'http://localhost'

billboard = "https://www.billboard.com/charts/hot-100/"
date_year = input(f"Where would you like to travel?\nType the date "
             f"YYYY-MM-DD: ")
date_month = input(f"Month in Numbers: ")
date_day = input(f"Day in Numbers: ")

url = f"{billboard}{date_year}-{date_month}-{date_day}"
print(url)

# data = open('data.html')

response = requests.get(url)
print(response.status_code)
# print(response.text)


soup = bs4.BeautifulSoup(response.text, 'html.parser')
songs = soup.find_all('span', class_='chart-element__information__song')
# print(len(songs))

songs_list = [song.text for song in songs]

print(songs_list)

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

song_uris = []

for song in songs_list:
    result = sp.search(f"track:{song} year:{date_year}", type='track')
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"Track \"{song}\" doesn't exist in Spotify. Skipped")

print(song_uris)
print(len(song_uris))
