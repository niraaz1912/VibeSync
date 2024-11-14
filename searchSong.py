import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'd613b327a8904cc488bc4c19f37561b4'      # Replace with your client_id
client_secret = '65f3190ade91427aa4b28f800daf7000'  # Replace with your client_secret

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

results = sp.search(q='Imagine', limit=5)
for idx, track in enumerate(results['tracks']['items']):
    print(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")