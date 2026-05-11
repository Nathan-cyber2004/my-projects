import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Constants
CLIENT_ID = "0cc56953d68a4bc2b7de03a134b45b99"
CLIENT_SECRET = "2318734a672445d2ac04579862e4e67a"

# API Logic
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Nathan Augustine Pereira", 
    )
)
user_id = sp.current_user()["id"]

