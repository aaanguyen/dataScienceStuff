import spotipy
import sys
import pprint
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_popularity(id):
    track = sp.track(id)
    print("getting id %s" % id)
    return track['popularity']

def main(filename):
    csv_data = pd.read_csv(filename)
    albums = pd.DataFrame(csv_data)
    albums['popularity'] = albums['track_id'].apply(get_popularity)
    albums.to_csv('albums_with_popularity.csv')

if __name__ == '__main__':
    main(sys.argv[1])