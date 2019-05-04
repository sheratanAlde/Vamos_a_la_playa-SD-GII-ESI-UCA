# utf-8
import tweepy
import LectorTwitter
import urllib2

######################Constantes#######################
url = "http://localhost:8080/????/"

######################Twittear respuesta#######################
def Tw_responder(tweetRecibido):

    mencion = Tw_lector.obtenerMencion(tweetRecibido)

    estoy = tweetRecibido.split("estoy en ")[1]
    estoy = estoy.split(" y quiero hacer")
    deporte = tweetRecibido.split(" y quiero hacer ")[1]

    playaRecomendada = x(estoy,deporte)
    ve_a=localizacion(playaRecomendada)

    tiempoQueTarda = y(estoy,ve_a)
    distanciaQueHay = z(estoy,ve_a)

    viento(ve_a)
    radiacion(ve_a)
    cielo(ve_a)

    tweet = mencion + " te recomendamos ir a " + playaRecomendada +
    "(a " + tiempoQueTarda + " min " + distanciaQueHay + " - km) y las condiciones climatologicas son: +
    " viento " + viento + " radiacion uv " + radiacion + "y está " + cielo 


    api = Tw_lector.autentificarTwitter()
    api.update_status(tweet)
