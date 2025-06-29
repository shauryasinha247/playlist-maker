import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
import sys

# === CONFIGURE YOUR APP CREDENTIALS HERE ===
client_id='c842b533d6d34fbf962911bca48ae38a',
client_secret='a2a1614730514b8590c43f57b6aae612',
redirect_uri='https://example.com/callback',  # match this in your app settings

# === SETUP AUTHENTICATION ===
scope = "user-read-private user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= client_id,
    client_secret= client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

try:
    # === STEP 1: CONFIRM USER INFO WORKS ===
    user = sp.me()
    print(f"\n✅ Logged in as: {user['display_name']} (ID: {user['id']})")

    # === STEP 2: SEARCH FOR A TRACK ===
    print("\n🔍 Searching for 'Blinding Lights'...")
    result = sp.search(q="track:Blinding Lights", type="track", limit=1)
    track = result['tracks']['items'][0]
    print(f"Found: {track['name']} by {track['artists'][0]['name']}")
    track_id = track['id']
    print(f"Track ID: {track_id}")

    # === STEP 3: GET AUDIO FEATURES ===
    print("\n🎧 Getting audio features...")
    features = sp.audio_features([track_id])
    if features and features[0]:
        print("✅ Audio features retrieved:")
        for key, val in features[0].items():
            print(f"{key}: {val}")
    else:
        print("❌ No audio features found.")

except SpotifyException as e:
    print("\n🚨 Spotify API error:")
    print(f"Status: {e.http_status}, Message: {e.msg}")
    sys.exit(1)

except Exception as ex:
    print("\n❌ Unexpected error:")
    print(type(ex).__name__, ex)
    sys.exit(1)
