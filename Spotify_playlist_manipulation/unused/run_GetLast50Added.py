from m.auth.auth import getAuthToken
import spotipy
from GetLast50Added import GetLast50Added

sp = spotipy.Spotify(getAuthToken())
GetLast50Added(sp)
