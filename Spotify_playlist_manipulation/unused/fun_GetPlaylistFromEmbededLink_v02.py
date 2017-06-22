from bs4 import BeautifulSoup
#import os
from fun_osbs import osbs

import urllib
import urllib2
import json

def getWebPage(url):
    #print 'getWebPage'
    page=urllib.urlopen(url)
    lines=page.readlines()
    lines=''.join(lines)
    return lines

def bsExtractChildrenByName(webPage, X):
    #print 'bsExtractX'
    bs=osbs(webPage)

    #print (len(bs.findChildren()))
    extractList=[]
    
    for tag in bs.findChildren():
        if (tag.name==X):
            try:
                #urlList=urlList+[(tag['src'])]
                #extractList=extractList+[(tag['href'])]
                #print [(tag['href'])
                #extractList=extractList+(tag[Y])
                extractList=extractList+[tag]
            except:
                print 'error'
                pass
    #extractList = bs
    return extractList

def getFromHtmlTag(htmlTag, whatToGetFromTag):
    result = htmlTag[whatToGetFromTag]
    return result


def trimSpotifyClassList(spotifyClasses, contains):
    trimmedList = []
    for spotifyClass in spotifyClasses:
        if spotifyClass[0]==contains:
            trimmedList = trimmedList + [spotifyClass[1]]
    return trimmedList

def getNameFromID(trackID, urlBase):
    url= urlBase+trackID
    #print url
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    json1_str = the_page
    json1_data = json.loads(json1_str)
    extract = json1_data['name']
    
    return extract

"""
def getArtistFromID(ArtistID, urlBaseArtist):
    extract = 'empty'
    try:
        url= urlBaseArtist+ArtistID
        #print url
        req = urllib2.Request(url)
        #print req
        response = urllib2.urlopen(req)
        the_page = response.read()
        json1_str = the_page
        json1_data = json.loads(json1_str)
        extract = json1_data['name']
        print extract
    except:
        pass
    return extract
"""

def getArtistFromtrackID(trackID, urlBaseTracks):
    extract = 'empty'
    url= urlBaseTracks+trackID
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    json1_str = the_page
    json1_data = json.loads(json1_str)
    #extract = json1_data['name']
    
    artists = json1_data['artists']
    extract = artists[0]['name']
    
    return extract



def downloadSpotifyPlaylistByEmbededUrl(url):
    #url = 'https://embed.spotify.com/?uri=spotify%3Auser%3Aatrakaz%3Aplaylist%3A6KYNaqaP3Uz7JcTaA1KgdB'
    webPage = getWebPage(url)

    name='li'
    bsExtractList = bsExtractChildrenByName(webPage, name)

    whatToGetFromTag='class'
    spotifyClasses=[]
    for htmlTag in bsExtractList:
        spotifyClasses = spotifyClasses + [getFromHtmlTag(htmlTag, whatToGetFromTag)]
        #print getFromHtmlTag(htmlTag, whatToGetFromTag)

    trimmedSpotifyClasses=[]
    contains='track-title'
    trimmedSpotifyClasses = trimSpotifyClassList(spotifyClasses, contains)


    #"""
    # DANGEROUS!
    trimmedSpotifyClassesArtists=[]
    contains='artist'
    trimmedSpotifyClassesArtists = trimSpotifyClassList(spotifyClasses, contains)
    #"""

    
    urlBaseTracks='https://api.spotify.com/v1/tracks/'
    #urlBaseArtist='https://api.spotify.com/v1/artists/'
    urlBase = urlBaseTracks
    trackNameList = []
    trackArtistList = []
    trimmedSpotifyClassesWithLink = []
    for trackID, ArtistID in zip(trimmedSpotifyClasses, trimmedSpotifyClassesArtists):
        name = getNameFromID(trackID, urlBase)
        artist = getArtistFromtrackID(trackID, urlBaseTracks)
        trackNameList = trackNameList + [name]
        trackArtistList = trackArtistList + [artist]
        trimmedSpotifyClassesWithLink = trimmedSpotifyClassesWithLink + ['https://open.spotify.com/track/'+str(trackID)]
        #print name



    #print '\nResult:'
    #print (trimmedSpotifyClasses)
    #print (trackNameList)

    size = len(trackNameList)
    tagBegin = ["_{" for x in range(size)]
    tag = ["" for x in range(size)]
    tagEnd = ["}_" for x in range(size)]

    #return trimmedSpotifyClasses, trackNameList
    return trimmedSpotifyClassesWithLink, trackNameList, trackArtistList





if __name__ == "__main__":
    url = 'https://embed.spotify.com/?uri=spotify%3Auser%3Aatrakaz%3Aplaylist%3A6KYNaqaP3Uz7JcTaA1KgdB'
    [trimmedSpotifyClasses, trackNameList, trackArtistList] = downloadSpotifyPlaylistByEmbededUrl(url)
    print trimmedSpotifyClasses, trackNameList, trackArtistList










