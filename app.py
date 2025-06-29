import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from itertools import islice
import random

client_id = 'c842b533d6d34fbf962911bca48ae38a'
client_secret = 'a2a1614730514b8590c43f57b6aae612'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def generate_playlist_name(mood):
    moods = {
        "happy": [
            "sunny side up", "smile juice", "high-key happy", "cheese & grins"
        ],
        "chill": [
            "couch potato club", "low battery mode", "nap time anthems", "no rush, just vibin'"
        ],
        "sad": [
            "waterworks playlist", "tears & toast", "sad songs & snacks", "melancholy mix-up"
        ],
        "party": [
            "dance floor casualty", "too cool to sleep", "bass drops & dad jokes", "party like a procrastinator"
        ],
        "focus": [
            "brain fuel only", "concentration station", "serious business tunes", "do not disturb mode"
        ]
    }
    return random.choice(moods.get(mood.lower(), [f"{mood} playlist"])).lower()

def main():
    print("hi! welcome to playlist maker! please answer the next few questions to get a playlist.\n")
    print("\navailable genres: pop, rock, hip-hop, country, jazz, electronic, classical, r&b, metal, indie")
    genre = input("preferred genre: ")
    start_year = int(input("start year (e.g. 2020): "))
    end_year = int(input("end year (e.g. 2024): "))

    print("\navailable moods: happy, chill, sad, party, focus")
    mood = input("choose a mood from above for playlist name: ")

    print("\nfetching tracks... this may take a few seconds.\n")

    query_main = f'genre:"{genre}" year:{start_year}-{end_year}'
    results_main = sp.search(q = query_main, type = 'track', limit = 50)

    track_info = []
    seen_tracks = set()

    for item in results_main['tracks']['items']:
        key = (item['name'].lower(), item['artists'][0]['name'].lower())
        if key not in seen_tracks:
            track_info.append({'id': item['id'], 'name': item['name'], 'artist': item['artists'][0]['name']})
            seen_tracks.add(key)

    random.shuffle(track_info)
    playlist_tracks = track_info[:25]

    playlist_name = generate_playlist_name(mood)

    print(f"\n🎧 your generated playlist name: {playlist_name}\n")
    print("🎶 here are your tracks:\n")
    for i, track in enumerate(playlist_tracks, 1):
        print(f"{i}. {track['name']} - {track['artist']}")

if __name__ == "__main__":
    main()