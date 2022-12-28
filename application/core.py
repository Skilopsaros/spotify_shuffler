import spotipy
import random
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()
  
username = 'skilopsaross'
clientID = os.getenv('SPOTIPY_CLIENT_ID')
clientSecret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri, scope="streaming")
token = oauth_object.get_access_token(as_dict=False)
spotify = spotipy.Spotify(auth=token)
user_name = spotify.current_user()

def get_playlist_tracks(playlist_id):
	results = spotify.playlist_tracks(playlist_id)
	tracks = results['items']
	while results['next']:
		results = spotify.next(results)
		tracks.extend(results['items'])
	return(tracks)


def shuffle_playlist(play_id):
	playlist = get_playlist_tracks(play_id)
	order = list(range(len(playlist)))
	random.shuffle(order)
	for i, value in enumerate(order):
		print(playlist[value]["track"]["name"])
		#spotify.add_to_queue(playlist[value]["track"]["id"])
		yield(playlist[value]["track"]["name"], i, len(order))
		sleep(1)