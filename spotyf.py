import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your app credentials
SPOTIPY_CLIENT_ID = 'your_client_ID'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
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
playlist_id = 'your_playlist_id'

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

