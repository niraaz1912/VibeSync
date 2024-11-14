import spotipy
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

def get_recommendations(emotion):
    features = emotion_to_features.get(emotion.lower())
    if not features:
        print("Emotion not recognized.")
        return []
    
    #print(features)

    # Map the feature ranges to Spotify API parameters
    params = {
        "limit": 10, # 10 songs
        #"seed_genres": ["pop", "rock", "electronic", "country", "classical", "jazz", "metal", "folk", "latin", "punk", "indie", "lo-fi", "chill" ,"mood", "focus"]  # Change as preferred
        "seed_genres": ["pop", "rock", "electronic", "afrobeat"]
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
