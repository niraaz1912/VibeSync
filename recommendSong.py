import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'd613b327a8904cc488bc4c19f37561b4'
client_secret = '65f3190ade91427aa4b28f800daf7000'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

emotion_to_features = {
    "anger": {"energy": (0.8, 1.0), "valence": (0.0, 0.3), "tempo": (120, 200)},
    "disgust": {"energy": (0.4, 0.6), "valence": (0.0, 0.3), "danceability": (0.0, 0.5)},
    "fear": {"energy": (0.0, 0.4), "valence": (0.0, 0.3), "danceability": (0.0, 0.4)},
    "joy": {"energy": (0.7, 1.0), "valence": (0.7, 1.0), "danceability": (0.6, 1.0)},
    "neutral": {"energy": (0.4, 0.6), "valence": (0.4, 0.6)},
    "sadness": {"energy": (0.0, 0.3), "valence": (0.0, 0.3), "acousticness": (0.6, 1.0)},
    "surprise": {"energy": (0.6, 1.0), "valence": (0.4, 0.6), "tempo": (130, 200)}
}

all_genres = ["acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", "bluegrass", "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", "chicago-house", "children", "chill", "classical", "club", "comedy", "country", "dance", "dancehall", "death-metal", "deep-house", "detroit-techno", "disco", "disney", "drum-and-bass", "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", "french", "funk", "garage", "german", "gospel", "goth", "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock", "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays", "honky-tonk", "house", "idm", "indian", "indie", "indie-pop", "industrial", "iranian", "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", "latino", "malay", "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb", "new-age", "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", "pop-film", "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day", "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll", "rockabilly", "romance", "sad", "salsa", "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep", "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", "synth-pop", "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"]
    
    # Function to randomly select genres (no emotion mapping)
def random_genres(num_genres=5):
    # Randomly select 'num_genres' genres from the list of all genres
    selected_genres = random.sample(all_genres, num_genres)
    return selected_genres

def get_recommendations(emotion):
    features = emotion_to_features.get(emotion.lower())
    if not features:
        print("Emotion not recognized.")
        return []
    
    

    selected_genres = random_genres(5)
    
    # Print out the selected genres
    #print(f"Selected genres: {selected_genres}")
    # Map the feature ranges to Spotify API parameters
    params = {
        "limit": 10, # 10 songs
        #"seed_genres": ["pop", "rock", "electronic", "country", "classical", "jazz", "metal", "folk", "latin", "punk", "indie", "lo-fi", "chill" ,"mood", "focus"]  # Change as preferred
        "seed_genres": selected_genres
        }

    # Add audio feature filters based on emotion
    for feature, (min_val, max_val) in features.items():
        params[f"min_{feature}"] = min_val
        params[f"max_{feature}"] = max_val

    # Fetch recommendations
    #country_codes= ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC', 'SV', 'EE', 'FI', 'FR', 'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI', 'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']
    recommendations = sp.recommendations(country={"CA"},**params)

    # Display track names and artists
    tracks = []
    for track in recommendations['tracks']:
        track_info = f"{track['name']} by {track['artists'][0]['name']}"
        tracks.append(track_info)

    return tracks

# Example: Get recommendations for "joy"
#recommended_tracks = get_recommendations("joy")
