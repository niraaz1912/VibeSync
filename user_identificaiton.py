import random
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Spotify client credentials
CLIENT_ID = 'd613b327a8904cc488bc4c19f37561b4'
CLIENT_SECRET = '65f3190ade91427aa4b28f800daf7000'
REDIRECT_URI = 'http://127.0.0.1:5500/'

# Scopes for the app (these will allow us to access the user's recent tracks)
scope = "user-library-read user-top-read user-read-recently-played playlist-read-private"

# Initialize Spotify client with OAuth manager
sp = Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

# Prompt the user to log in and authenticate (this will open a browser window)
print("Please log in to Spotify...")

# Emotion-to-features mapping
EMOTION_TO_FEATURES = {
    "anger": {"energy": (0.8, 1.0), "valence": (0.0, 0.3), "tempo": (120, 200)},
    "disgust": {"energy": (0.4, 0.6), "valence": (0.0, 0.3), "danceability": (0.0, 0.5)},
    "fear": {"energy": (0.0, 0.4), "valence": (0.0, 0.3), "danceability": (0.0, 0.4)},
    "joy": {"energy": (0.7, 1.0), "valence": (0.7, 1.0), "danceability": (0.6, 1.0)},
    "neutral": {"energy": (0.4, 0.6), "valence": (0.4, 0.6)},
    "sadness": {"energy": (0.0, 0.3), "valence": (0.0, 0.3), "acousticness": (0.6, 1.0)},
    "surprise": {"energy": (0.6, 1.0), "valence": (0.4, 0.6), "tempo": (130, 200)}
}

# List of all genres available in Spotify
ALL_GENRES = [
    "acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", "bluegrass", "blues", 
    "bossanova", "brazil", "breakbeat", "british", "cantopop", "chicago-house", "children", "chill", "classical", 
    "club", "comedy", "country", "dance", "dancehall", "death-metal", "deep-house", "detroit-techno", "disco", 
    "disney", "drum-and-bass", "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", "french", 
    "funk", "garage", "german", "gospel", "goth", "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock", 
    "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays", "honky-tonk", "house", "idm", "indian", "indie", 
    "indie-pop", "industrial", "iranian", "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", 
    "latino", "malay", "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb", "new-age", 
    "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", "pop-film", "post-dubstep", 
    "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day", "reggae", "reggaeton", 
    "road-trip", "rock", "rock-n-roll", "rockabilly", "romance", "sad", "salsa", "samba", "sertanejo", "show-tunes", 
    "singer-songwriter", "ska", "sleep", "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", 
    "synth-pop", "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"
]



# Functions to fetch user data (top artists, tracks, recently played)
def get_user_top_artists(sp, limit=5):
    try:
        top_artists = sp.current_user_top_artists(limit=limit)
        return [artist['id'] for artist in top_artists['items']]
    except Exception as e:
        print(f"Error fetching top artists: {e}")
        return []

def get_user_top_tracks(sp, limit=5):
    try:
        top_tracks = sp.current_user_top_tracks(limit=limit)
        return [track['id'] for track in top_tracks['items']]
    except Exception as e:
        print(f"Error fetching top tracks: {e}")
        return []

def get_recently_played_tracks(sp, limit=5):
    try:
        recent_tracks = sp.current_user_recently_played(limit=limit)
        return [track['track']['id'] for track in recent_tracks['items']]
    except Exception as e:
        print(f"Error fetching recently played tracks: {e}")
        return []

# Function to randomly select genres
def random_genres(num_genres):
    return random.sample(ALL_GENRES, num_genres)

# Main function to get personalized recommendations based on emotion
def get_recommendations(emotion):
    # Validate emotion input
    features = EMOTION_TO_FEATURES.get(emotion.lower())
    if not features:
        print(f"Emotion '{emotion}' not recognized.")
        return []

    # Retrieve user data for personalization
    top_artists = get_user_top_artists(sp)
    top_tracks = get_user_top_tracks(sp)
    recent_tracks = get_recently_played_tracks(sp)
    selected_genres = random_genres(3)

    # Debugging: Print the retrieved data
   # print(f"Top Artists: {top_artists}")
    #print(f"Top Tracks: {top_tracks}")
    #print(f"Recent Tracks: {recent_tracks}")
    #print(f"Selected Genres: {selected_genres}")

    # Ensure at least one artist, track, and genre is available
    if not top_artists or not top_tracks or not selected_genres:
        print("Insufficient data in user's account. Only emotion will used to recommend songs.")
        return []

    # Convert top artists and top tracks to proper URIs for Spotify
    top_artists_uris = [f"spotify:artist:{artist}" for artist in top_artists[:3]]
    top_tracks_uris = [f"spotify:track:{track}" for track in top_tracks[:2]] if top_tracks else [f"spotify:track:{track}" for track in recent_tracks[:2]]


    # Configure recommendation parameters with user data
    params = {
        "seed_artists": top_artists_uris,  # Using URIs instead of just IDs
        #"seed_genres": selected_genres,
        "seed_tracks": top_tracks_uris,  # Using URIs instead of just IDs
        "limit": 10
    }

    
    # Add audio feature filters based on the user's emotion
    for feature, (min_val, max_val) in features.items():
        params[f"min_{feature}"] = min_val
        params[f"max_{feature}"] = max_val

    # Fetch recommendations
    try:
        recommendations = sp.recommendations(**params)
    except Exception as e:
        print(f"Error fetching recommendations: {e}")
        return []

    # Return track names and artists
    tracks = []
    for track in recommendations['tracks']:
        track_info = f"{track['name']} by {track['artists'][0]['name']}"
        tracks.append(track_info)
        

    return tracks

def get_recommendations_genre(emotion):
    # Validate emotion input
    features = EMOTION_TO_FEATURES.get(emotion.lower())
    if not features:
        print(f"Emotion '{emotion}' not recognized.")
        return []

    selected_genres = random_genres(5)
    print(f"Selected Genres: {selected_genres}")

    # Ensure at least one artist, track, and genre is available
    if not selected_genres:
        print("Error: Insufficient data for recommendation.")
        return []

    # Configure recommendation parameters with user data
    params = {
        "seed_genres": selected_genres,
        "limit": 10
    }

    
    # Add audio feature filters based on the user's emotion
    for feature, (min_val, max_val) in features.items():
        params[f"min_{feature}"] = min_val
        params[f"max_{feature}"] = max_val

    # Fetch recommendations
    try:
        recommendations = sp.recommendations(**params)
    except Exception as e:
        print(f"Error fetching recommendations: {e}")
        return []

    # Return track names and artists
    tracks = []
    for track in recommendations['tracks']:
        track_info = f"{track['name']} by {track['artists'][0]['name']}"
        tracks.append(track_info)
        

    return tracks

def recommend(emotion):
    tracks = get_recommendations(emotion)
    new_tracks = []
     
    if (len(tracks)<10):
        new_tracks = get_recommendations_genre(emotion)
        
    tracks.extend(new_tracks)
    return tracks

