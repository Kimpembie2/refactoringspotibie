import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "443883fd510c43e29bb9ee1e295cddd5"
SPOTIFY_CLIENT_SECRET = "f6de4aa660244f8d8689aea1b94344de"
SPOTIFY_REDIRECT_URI = "https://5000-kimpembie2-spotibie-vxumfk9y9qi.ws-eu117.gitpod.io/callback" 

sp_oauth = SpotifyOAuth(
client_id=SPOTIFY_CLIENT_ID,
client_secret=SPOTIFY_CLIENT_SECRET,
redirect_uri=SPOTIFY_REDIRECT_URI,
scope="user-read-private",
show_dialog=True 
)

def get_spotify_object(token_info):
    return spotipy.Spotify( auth=token_info['access_token'])