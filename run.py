import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import time

# Spotify API Credentials (Replace with your own if needed)
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8888/callback"

# Spotify Authentication
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

# Function to get tracks from a playlist
def get_playlist_tracks(playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            tracks.append((track['id'], track['name'], track['artists'][0]['name']))
        results = sp.next(results) if results['next'] else None
    return tracks

# Function to run the tournament
def run_tournament(tracks):
    rankings = []
    round_number = 1
    while len(tracks) > 1:
        print(f"\nRound {round_number}: {len(tracks)} songs remaining, {len(tracks) // 2} matchups")
        random.shuffle(tracks)
        winners = []
        losers = []
        for i in range(0, len(tracks), 2):
            if i + 1 >= len(tracks):
                winners.append(tracks[i])  # If odd number, auto-advance last song
                continue
            
            track1, track2 = tracks[i], tracks[i + 1]
            print(f"1: {track1[1]} - {track1[2]}")
            print(f"2: {track2[1]} - {track2[2]}")
            choice = input("Choose (1 or 2): ")
            if choice == "1":
                winners.append(track1)
                losers.append(track2)
            elif choice == "2":
                winners.append(track2)
                losers.append(track1)
            else:
                print("Invalid choice, defaulting to 1.")
                winners.append(track1)
                losers.append(track2)
        
        rankings = losers + rankings  # Append losers to rankings
        tracks = winners
        round_number += 1
    
    rankings.insert(0, tracks[0])  # Insert the ultimate winner at the top
    return rankings

# Function to reorder playlist based on preferences
def reorder_playlist(playlist_id, ranked_tracks):
    track_ids = [track[0] for track in ranked_tracks]
    sp.user_playlist_replace_tracks(sp.me()['id'], playlist_id, track_ids)
    print("Playlist reordered successfully!")
    
    # Print final ranked list
    print("\nFinal ranked order:")
    for idx, track in enumerate(ranked_tracks, 1):
        print(f"{idx}. {track[1]} - {track[2]}")

if __name__ == "__main__":
    playlist_id = input("Enter your Spotify playlist ID: ")
    tracks = get_playlist_tracks(playlist_id)
    
    if not tracks:
        print("No tracks found in playlist.")
        exit()
    
    print(f"Loaded {len(tracks)} songs. Let's begin the tournament!")
    ranked_tracks = run_tournament(tracks)
    
    print(f"The best song in your playlist is: {ranked_tracks[0][1]} - {ranked_tracks[0][2]}")
    
    reorder = input("Do you want to reorder your playlist based on rankings? (yes/no): ")
    if reorder.lower() == "yes":
        reorder_playlist(playlist_id, ranked_tracks)
