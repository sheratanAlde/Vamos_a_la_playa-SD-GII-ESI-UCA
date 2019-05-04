import tweepy
import Tw_lector

def Tw_ComandoInvalido(tweetRecibido):
    mencion = Tw_lector.obtenerMencion(tweetRecibido)
    twitter = Tw_lector.autentificarTwitter()
    cad = mencion + " comando no invalido, por favor prueba con \"estoy en (donde estés) y quiero hacer (lo que quieras hacer)\""
    twitter.update_status(cad)
