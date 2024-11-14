import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'd613b327a8904cc488bc4c19f37561b4'
client_secret = '65f3190ade91427aa4b28f800daf7000'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

results = sp.search(q="Kehi Mitho Baat Gara", type="track", limit=1)
track_id = results['tracks']['items'][0]['id']  # Get the track ID

print(results)

# Retrieve audio features
features = sp.audio_features(track_id)[0]
print(features)
# Display audio features
print("Danceability:", features['danceability'])
print("Energy:", features['energy'])
print("Valence:", features['valence'])
print("Tempo:", features['tempo'])
print("Acousticness:", features['acousticness'])
print("Liveness:", features['liveness'])
print("Speechiness:", features['speechiness'])
print("Instrumentalness:", features['instrumentalness'])