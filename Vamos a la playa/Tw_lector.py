import tweepy
import pika
import send

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def autentificarTwitter():
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def obtenerMencion(tweetRecibido):
    mencion = "@"
    i = 0
    while tweetRecibido[i] != 'estoy en ':
        mencion = mencion + tweetRecibido[i]
        i = i + 1
    return mencion
