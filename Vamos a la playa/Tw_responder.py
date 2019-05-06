import tweepy
import tw_lector
import laPlaya

def Tw_responder(tweetRecibido):

    mencion = Tw_lector.obtenerMencion(tweetRecibido)

    estoy = tweetRecibido.split("-estoy en ")[1]
    estoy = estoy.split(" y quiero hacer")
    deporte = tweetRecibido.split(" y quiero hacer ")[1]

    tweet = mencion + calcularRespuesta(estoy,deporte)

    api = Tw_lector.autentificarTwitter()
    api.update_status(tweet)

def calcularRespuesta(sitio, actividad):

    try:
        mensaje = laPlaya.calcularPlaya(sitio, actividad)
    except:
        mensaje = "perdona, ahora estamos tomando el sol, prueba mas tarde."

    #print("Mi funcion" + mensaje)
    return mensaje