# -*- coding: utf-8 -*-

import os
import sys
import spotipy
import spotipy.util as util
import time
from json.decoder import JSONDecodeError

username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

#User Info
user = spotifyObject.current_user()
displayName = user['display_name']

track = spotifyObject.current_user_playing_track()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

print()
print(">>> Welcome to Spotify " + displayName + " :)")
print()



while True:

    track = spotifyObject.current_user_playing_track()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']

    if artist !="":
        np = ("🎵 Tocando: " + artist + " - " + track)
        f = open("np.txt", "w")
        f.write(np)
        print(np)
        time.sleep(5)
