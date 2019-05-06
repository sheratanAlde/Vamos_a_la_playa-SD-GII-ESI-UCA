import laPlaya


def calcularRespuesta(sitio, actividad):

    try:
        mensaje = laPlaya.calcularPlaya(sitio, actividad)
    except:
        mensaje = "perdona, ahora estamos tomando el sol, prueba mas tarde."

    #print("Mi funcion" + mensaje)
    return mensaje


if __name__ == "__main__":

    sitio = "Tarifa"
    actividad = ""

    respuestaTwitter = calcularRespuesta(sitio, actividad)
