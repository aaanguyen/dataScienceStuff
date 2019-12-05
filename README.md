# Instructions

# Data Collection
Before running the python data collection scripts, you need to do the following:  
* Ensure you have numpy, pandas, and matplotlib

* Install Spotipy  
```pip3 install spotipy```
 
* Create a Spotify application to receive credentials and set up the following env variables:  
```export SPOTIPY_CLIENT_ID='your-spotify-client-id'```  
```export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'```  
```export SPOTIPY_REDIRECT_URI='your-app-redirect-url'```  

and you're good to go!  

### Featured Playlist data:  
```python3 grab_featured_playlists.py``` <-- Returns a csv called '2018_and_2019_hourly_lists.csv' with hourly featured playlist data from the start of 2018 to October 27, 2019.
  
### Album Progression Popularity data:  
```python3 grab_albums.py``` <-- Returns a csv called 'albums.csv' with track information from 40 different albums that were released in 2019.  
```python3 track_popularity.py albums.csv``` <-- Returns a new csv called 'albums_with_popularity.csv', which adds a new column 'Popularity' to 'albums.csv'.

# Data Analysis

### Album Progression Popularity Density Visualization 

* Used libraries: pandas, numpy, matplotlib

* Ensure 'albums_with_popularity.csv' is in the same folder as the 'analyze_albums.ipynb' Jupyter notebook, then run the notebook to see the graph visualization.

