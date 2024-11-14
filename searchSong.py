import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_client():
    
    client_id = 'd613b327a8904cc488bc4c19f37561b4'      # Replace with your client_id
    client_secret = '65f3190ade91427aa4b28f800daf7000'  # Replace with your client_secret

    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


    

