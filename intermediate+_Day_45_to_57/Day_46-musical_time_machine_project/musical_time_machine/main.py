
"""
    Musical Time Machine

    Takes user input as YEAR-MONTH-DAY and create a spotify playlist
    of Top 100 tracks of this date.

"""

import bs4
import requests
import spotipy

import os
import dotenv

dotenv.load_dotenv()  # Loads Environment Variables file

# Holds Spotify Client ID and KEY
sp_client_id = os.getenv('CLIENT_ID')
sp_client_key = os.getenv('CLIENT_KEY')
redirect_uri = 'http://localhost'


def user_input():
    """ Takes user input and create URL """
    billboard = "https://www.billboard.com/charts/hot-100/"
    date_year = input(f"Where would you like to travel?\nType the date "
                      f"YYYY-MM-DD: ")
    date_month = input(f"Month in Numbers: ")
    date_day = input(f"Day in Numbers: ")

    billboard_endpoint = f"{billboard}{date_year}-{date_month}-{date_day}"
    return billboard_endpoint, date_year, date_month, date_day


def create_songs_list():
    """ Creates the list of the songs from the input dated """
    billboard_response = requests.get(url)
    print(billboard_response.status_code)
    # Provides request data from the billboard to the BS4
    soup = bs4.BeautifulSoup(billboard_response.text, 'html.parser')
    songs_list = soup.find_all('span', class_='chart-element__information__song')
    print(len(songs_list))

    songs_list = [song.text for song in songs_list]  # Creates the list of the songs name
    return songs_list  # Return songs list


def create_songs_URI():
    """ Create spotify URIs for each song name in the songs list """
    for song in songs:
        # Search for the song using sp object created using Spotify class
        result = sp.search(f"track:{song} year:{year}", type='track')
        # Handles the exception if the songs is not found
        try:
            uri = result['tracks']['items'][0]['uri']  # Holds the URI of the current song
            song_uris.append(uri)  # Append the URI to the songs_uri list
        except IndexError:
            print(f"Track \"{song}\" doesn't exist in Spotify. Skipped")


def create_playlist():
    """ Creates playlist and return created playlist ID """
    playlist_ep = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    header_playlist = {
        'Authorization': f"Bearer {os.getenv('CREATE_PLAYLIST_TOKEN')}"
    }
    create_pl_parameters = {
        'name': f"{year}-{month}-{day} Billboard Top 100",
        'public': False,
        'description': f"Top 100 songs from {month}-{year}"
    }
    pl_response = requests.post(
        url=playlist_ep,
        headers=header_playlist,
        json=create_pl_parameters
    )
    print(f"Playlist response: {pl_response.status_code}")
    play_id = pl_response.json()['id']  # Holds the playlist id from the response text
    print(f"Playlist ID: {play_id}")
    return play_id  # Return playlist ID


def add_tracks():
    """ Add tracks to the spotify playlist using songs URIs """
    add_tracks_endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    add_tracks_header = {
        'Authorization': f"Bearer {os.getenv('ADD_ITEMS_TOKEN')}",
        'Content-Type': 'application/json'}
    add_tracks_params = {'uris': song_uris}

    response_add_tracks = requests.post(
        url=add_tracks_endpoint,
        headers=add_tracks_header,
        json=add_tracks_params
    )

    print(response_add_tracks.status_code)
    print(response_add_tracks.text)


url, year, month, day = user_input()  # Creates variables from the user input

songs = create_songs_list()  # Call function to create playlist

# Create and Authorize spotify user
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
user_id = sp.current_user()["id"]  # Hold the current user ID
print(user_id)

song_uris = []

create_songs_URI()  # Calls the func to create songs URIs and append them to song_uri list

print(len(song_uris))

playlist_id = create_playlist()  # Calls the func to create playlist and return its ID

add_tracks()  # Add tracks to the Spotify Playlist

"""
    The code is working fine without any errors. 
    
    The problem is with the Access Token. It expires within few minutes. 
    So, OAuthorization2.0 is needed to be added for a robust application. 
    Will work on it soon. 
    
"""
