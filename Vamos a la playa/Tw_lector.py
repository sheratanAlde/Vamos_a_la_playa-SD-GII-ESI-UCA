# -*- coding: utf-8 -*-
import tweepy
import pika
import send

######################Constantes#######################
# Cuenta: 
# Contaseña:  

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

################Clase MyStreamListener################
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        channel = send.channel
        print(status.text + "/" + status.author.screen_name)
        if "lista" in status.text:
            message = status.author.screen_name + "/" + status.text
            channel.basic_publish(exchange='', routing_key='lista', body=message)
        elif "compra:" in status.text:
            message = status.author.screen_name + "/" + status.text
            channel.basic_publish(exchange='', routing_key='compra', body=message)
        else:
            message = status.author.screen_name + "/" + status.text
            channel.basic_publish(exchange='', routing_key='error', body=message)

################Autentificacion en twitter################
def autentificarTwitter():
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

################Crear objeto MyStreamListener################
def crearListener():
    api = autentificarTwitter()
    my_listener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = my_listener)
    return myStream

################Autentificacion en twitter################
#tweetRecibido ha de ser un String con el tweet del que se quiere obtener la mencion
def obtenerMencion(tweetRecibido):
    mencion = "@"
    i = 0
    while tweetRecibido[i] != 'estoy en ':
        mencion = mencion + tweetRecibido[i]
        i = i + 1
    return mencion
