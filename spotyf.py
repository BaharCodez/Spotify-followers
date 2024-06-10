import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your app credentials
SPOTIPY_CLIENT_ID = '31dc7e12a84047aeab377417a7fbf05a'
SPOTIPY_CLIENT_SECRET = '51f4fc49c75c4ec4aa0add23f3e05563'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'

# Define the scope
SCOPE = 'playlist-read-private user-library-read'

# Initialize the Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE))

# Get the current user's playlists
results = sp.current_user_playlists()
for item in results['items']:
    print(f"Playlist: {item['name']}, ID: {item['id']}")

# Replace with your playlist ID
playlist_id = '7isduMadThpQaFPdMr1mgA'

# Check if the playlist is followed
playlist = sp.playlist(playlist_id, fields="followers")
print(f"Number of followers: {playlist['followers']['total']}")


friend_user_id = 'friend_user_id'

# Check if the friend_user_id follows the playlist
follows = sp.playlist_is_following(playlist_id, [friend_user_id])
if follows[0]:
    print("Your friend is following your playlist!")
else:
    print("Your friend is not following your playlist.")

