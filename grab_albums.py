import os, sys, spotipy, pprint
import spotipy.util as util
import pandas as pd
import csv
from spotipy.oauth2 import SpotifyClientCredentials

def main():
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    albums = ['spotify:album:1NAmidJlEaVgA3MpcPFYGq','spotify:album:4g1ZRSobMefqF6nelkgibi','spotify:album:0FgZKfoU2Br5sHOfvZKTI9','spotify:album:1LVNYhjG7hkowdUwgwOdXj', \
            'spotify:album:6KT8x5oqZJl9CcnM66hddo','spotify:album:1Uf67JAtkVWfdydzFFqNF2','spotify:album:1AvXa8xFEXtR3hb4bgihIK','spotify:album:0xzScN8P3hQAz3BT3YYX5w', \
            'spotify:album:2fYhqwDWXjbpjaIJPEfKFw','spotify:album:65T18oWoikW2MAilg9j8lW','spotify:album:0S0KGZnfBGSIssfF54WSJh','spotify:album:1nzUj7VkiaytMmf2KrhK2L', \
            'spotify:album:1qgJNWnPIeK9rx7hF8JCPK','spotify:album:1NsTSXjVNE7XmZ8PmyW0wl','spotify:album:1bnHPO4dKK7IjvgrtVBcQh','spotify:album:3oIFxDIo2fwuk4lwCmFZCx', \
            'spotify:album:1MmVkhiwTH0BkNOU3nw5d3','spotify:album:41GuZcammIkupMPKH2OJ6I','spotify:album:2fYhqwDWXjbpjaIJPEfKFw','spotify:album:6tkjU4Umpo79wwkgPMV3nZ', \
            'spotify:album:6ylFfzx32ICw4L1A7YWNLN','spotify:album:5658aM19fA3JVwTK6eQX70','spotify:album:3Qa0qW4ged1J4HGeLXbFsC','spotify:album:6xJ38Up5iUhTh30FdwHN1d', \
            'spotify:album:2Ni5tXmyXPTG4jeQxvSqjv','spotify:album:7acEciVtnuTzmwKptkjth5','spotify:album:5Or2XM0Gjy6Y8qlaERqsSn','spotify:album:1G2YEQPXaOj1JZwa3ZiGe8', \
            'spotify:album:5zi7WsKlIiUXv09tbGLKsE','spotify:album:0XLwImzaZEtqHE4NHAepDz','spotify:album:6JKkXVEljQJ1wKbRG5MywC','spotify:album:1A3nVEWRJ8yvlPzawHI1pQ', \
            'spotify:album:5gnWhEFNbtCn0RLG2cp90g','spotify:album:46xdC4Qcvscfs3Ai2RIHcv','spotify:album:1C1qYeSC9RdgbrKXpZCTSJ','spotify:album:754RY5WpZ2LTUZsk8kDBju', \
            'spotify:album:2c7gFThUYyo2t6ogAgIYNw','spotify:album:2n3quCZ0anEa46j2IveacI','spotify:album:3oFEUoJSqKrOgDKE3kHfwP','spotify:album:02FX4aLHDNacfV4bMnO9Kv', \
            'spotify:album:4AokGqTuwsYw5jvpku4Ljp','spotify:album:7ki5b310cwDVVJBevBLwdw','spotify:album:0RedX0LZkGUFoRwFntAaI0','spotify:album:0aA9rYw8PEv9G7tVIJ9dKg']

    master_list = []
    for urn in albums:
        album = sp.album(urn)
        for song in album['tracks']['items']:
            track_info = []
            track_info.append(album['artists'][0]['name'])
            track_info.append(album['name'])
            track_info.append(song['track_number'])
            track_info.append(song['name'])
            track_info.append(song['id'])
            master_list.append(track_info)
            
    with open('albums.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['artist','album','track_number','track_name','track_id'])
        writer.writerows(master_list)

if __name__ == "__main__":
    main()