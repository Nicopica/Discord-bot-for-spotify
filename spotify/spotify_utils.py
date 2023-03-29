import sys
import os
import csv
from dotenv import load_dotenv
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotify.data_manager import data_manager, get_data_tracks, last_index
from spotify.class_track import Track
import pyshorteners
import numpy as np
import asyncio
from composers_classification import list_genre
from get_path import DATA_TRACK_PATH

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = 'http://localhost:8080'
scope = 'user-library-read'
username = 'Franz Peter Schubert'

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)  # TODO Don't let this here
# token = auth_manager=SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth=token)

list_tracks = []


def get_image_composer(name):
    results = sp.search(q=name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        if artist['images']:
            return artist['images'][0]['url']
        else:
            print(f'Photo not found for {name}')


def read_saved_tracks(limit=50, offset=0):  # You can probably improve this / adapt it to playlists
    if os.path.exists(DATA_TRACK_PATH) and os.path.isfile(DATA_TRACK_PATH) and offset == 0:
        os.remove(DATA_TRACK_PATH)
        open(DATA_TRACK_PATH, 'x')

    results = sp.current_user_saved_tracks(limit=limit, offset=offset)['items']

    if len(results) == 50:
        read_saved_tracks(offset=offset + 50)

    for r in results:
        result = r['track']
        name = result['name']

        artist = result['artists'][0]['name']
        url_spotify = result['external_urls']['spotify']
        preview = result['preview_url']

        # album_name = result['album']['name'].replace(artist, '')
        album_name = result['album']['name'].split(':')[-1].rstrip()
        # To be used
        # album_pic = result['album']['images'][0]['url']
        # album_url = result['album']['external_urls']

        if not result['preview_url']:
            preview = 'not available'

        for i in list_genre:
            if i.lower() in name.lower():
                genre = i
                break
        else:  # No break
            genre = 'not found'

        data_manager(offset=offset, name=name, artist=artist, album_name=album_name, genre=genre,
                     url_spotify=url_spotify, preview=preview)

