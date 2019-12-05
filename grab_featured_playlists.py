import os, sys, json, spotipy
import spotipy.util as util
import pandas as pd
import csv
from spotipy.oauth2 import SpotifyClientCredentials

if __name__ == '__main__':
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    master_list = []
    for yearNumber in [2018,2019]:
        for month in range(11):
            if month == 10 and yearNumber == 2019:
                break
            monthNumber = '{num:02d}'.format(num=month + 1)
            for day in range(27):
                dayNumber = '{num:02d}'.format(num=day + 1)
                for hour in range(24):
                    hourNumber = '{num:02d}'.format(num=hour)
                    timestamp = '{year}-{month}-{day}T{hour}:00:00'.format(year=yearNumber,month=monthNumber,day=dayNumber,hour=hourNumber)

                    response = sp.featured_playlists(timestamp=timestamp)
                    # print(response['message'])

                    playlists_list = [timestamp]

                    if hour >= 23 or hour < 6:                  # between 11pm and 5am
                        playlists_list.append('Sleeptime')
                    elif hour >= 6 and hour < 11:               # between 6am and 10am
                        playlists_list.append('Morning')
                    elif hour >= 11 and hour < 18:              # between 11am and 5pm
                        playlists_list.append('Daytime')
                    elif hour >= 18 and hour < 23:              # between 6pm and 10pm
                        playlists_list.append('Dinnertime')

                    while response:
                        playlists = response['playlists']
                        for i, item in enumerate(playlists['items']):
                            playlists_list.append(item['name'])

                        if playlists['next']:
                            response = sp.next(playlists)
                        else:
                            response = None

                    master_list.append(playlists_list)
                    print("successfully grabbed playlists up to %s" % timestamp)


    with open('2018_and_2019_hourly_lists.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp","time_of_day","1","2","3","4","5","6","7","8","9","10","11","12","13"])
        writer.writerows(master_list)