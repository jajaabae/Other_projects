#import sys
#import spotipy
import spotipy.util as util

def authValues():
    username = 'Atrakaz'
    client_id='f1226bc32f3643d19641c8cb353e3d83'
    client_secret='aedf7c606ec24328859a143b59aa493c'
    redirect_uri='http://folk.uio.no/jajaabae/index.htm'
    return username, client_id, client_secret, redirect_uri

def getToken(username, client_id, client_secret, redirect_uri):
    #scope = 'user-library-read'
    #scope = 'playlist-modify-public'
    #scope = 'playlist-modify-private'
    #scope = 'playlist-modify-private playlist-modify-public user-library-read'
    #scope = 'playlist-read-private playlist-modify-private playlist-modify-public user-library-read'
    scope = ''
    scope += 'playlist-read-private '
    scope += 'playlist-modify-private '
    scope += 'playlist-modify-public '
    scope += 'user-library-read '
    
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    return token

def getAuthToken():
    username, client_id, client_secret, redirect_uri = authValues()
    token = getToken(username, client_id, client_secret, redirect_uri)
    return token


if __name__ == '__main__':
    token =  getAuthToken()
    print token
    #f = open('token.txt', 'w')
    #f.write(token)
    #f.close()
    



