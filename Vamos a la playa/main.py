import elTiempo
import laPlaya
import laRuta


def calcularRespuesta(sitio, actividad):
    mensaje = "perdona, ahora estamos tomando el sol, prueba mas tarde."

    posPlaya = laPlaya.calcularPlaya(sitio, actividad)

    # mensaje = mensaje + laRuta.tiempoDistanciaRuta(posPoblacion,posPlaya)

    return mensaje


if __name__ == "__main__":

    sitio = "Benalup"
    actividad = "piragüismo"

    respuestaTwitter = calcularRespuesta(sitio, actividad)

    # print(respuestaTwitter)
    #
    #
    # # dato = elTiempo.infoPlaya(1101203)
    # # print(dato)
    #
    # #elTiempo.infoPlaya(1101203)
    # laPlaya.datosPlaya()
    # try:
    #     print(laRuta.tiempoDistanciaRuta("San Fernando","El Carmen"))
    # except:
    #     print("el GPS esta recalculando")
