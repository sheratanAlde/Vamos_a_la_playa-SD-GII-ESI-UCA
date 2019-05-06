# -*- coding: utf-8 -*-
from aemet import Aemet
import json
from datetime import datetime


#Función que en base al dato de la AEMET del tipo de oleaje da una calificación
def calculoOleaje (dato):
    if dato == "débil":
        return 9
    if dato == "moderado":
        return 6
    if dato == "fuerte":
        return 3
    return 10


#Función que en base al dato de la AEMET de la fuerza del viento se da una calificación
def calculoViento(dato):
    if dato == "flojo":
        return 9
    if dato == "moderado":
        return 6
    if dato == "fuerte":
        return 3
    return 10


#Función que en base al dato de la AEMET de las distintas temperaturas se da una calificación
def calculoTemperaturas(sensacion, agua, maxima):
    valorTemperatura = 0

    if sensacion == "suave":                                                                                            #Sensación termica
        valorTemperatura = 9
    if sensacion == "calor agradable":
        valorTemperatura = 6
    if sensacion != "suave" and sensacion != "calor agradable":
        valorTemperatura = 3

    if int(agua) > 20:                                                                                                  #Temperatura del agua
        valorTemperatura += 10
    elif int(agua) > 18:
        valorTemperatura += 5
    else:
        valorTemperatura += 0

    if int(maxima) > 35:                                                                                                #Temperatura maxima
        valorTemperatura += 3
    elif int(maxima) > 30:
        valorTemperatura += 6
    elif int(maxima) > 25:
        valorTemperatura += 10
    elif int(maxima) > 20:
        valorTemperatura += 6
    elif int(maxima) > 15:
        valorTemperatura += 3
    else:
        valorTemperatura += 0

    return int(valorTemperatura/3)


#Función que en base al dato de la AEMET de la intensidad de UV se da una calificación
def calculoIndiceUV(dato):
    if int(dato) > 10:
        return 0
    elif int(dato) > 7:
        return 2
    elif int(dato) > 5:
        return 4
    elif int(dato) > 2:
        return 8
    else:
        return 10


#Por medio del código de una playa se devuelve una calificación de las condiciones de playa a nivel climatologico
def situacionPlaya(codPlaya):
    ahora = datetime.now()

    aemet = Aemet()
    playa = aemet.get_prediccion_especifica_playa(int(codPlaya))
    data_string = json.dumps(playa)
    decode = json.loads(data_string)
    datosActual = decode['prediccion']['dia'][0]

    if ahora.hour > 13:                                                                                                 #Según la franja horaria en la que nos encontremos mirara el dato de por la mañana o por la tarde
        #cielo = datosActual['estadoCielo']['descripcion2']
        viento = datosActual['viento']['descripcion2']
        oleaje = datosActual['oleaje']['descripcion2']
    else:
        #cielo = datosActual['estadoCielo']['descripcion1']
        viento = datosActual['viento']['descripcion1']
        oleaje = datosActual['oleaje']['descripcion1']

    temperaturaMaxima = datosActual['tMaxima']['valor1']
    sensacionTermica = datosActual['sTermica']['descripcion1']
    temperaturaAgua = datosActual['tAgua']['valor1']
    indiceUv = datosActual['uvMax']['valor1']

    puntuacion = calculoOleaje(oleaje)
    puntuacion += calculoViento(viento)
    puntuacion += calculoTemperaturas(sensacionTermica,temperaturaAgua,temperaturaMaxima)
    puntuacion += calculoIndiceUV(indiceUv)

    return puntuacion/4


def infoPlaya(cod):
    aemet = Aemet()
    ahora = datetime.now()
    playa = aemet.get_prediccion_especifica_playa(cod)
    data_string = json.dumps(playa)
    decode = json.loads(data_string)
    datosActual = decode['prediccion']['dia'][0]

    if ahora.hour > 13:                                                                                                 # Según la franja horaria en la que nos encontremos mirara el dato de por la mañana o por la tarde
        cielo = datosActual['estadoCielo']['descripcion2']
        viento = datosActual['viento']['descripcion2']
        #oleaje = datosActual['oleaje']['descripcion2']
    else:
        cielo = datosActual['estadoCielo']['descripcion1']
        viento = datosActual['viento']['descripcion1']
        #oleaje = datosActual['oleaje']['descripcion1']

    #temperaturaMaxima = datosActual['tMaxima']['valor1']
    sensacionTermica = datosActual['sTermica']['descripcion1']
    #temperaturaAgua = datosActual['tAgua']['valor1']
    indiceUv = datosActual['uvMax']['valor1']

    return "y hay una previsión de viento " + viento + " con el cielo " + cielo + "," \
           " con una sensación de " + str(sensacionTermica) + " y el indice UV es de " + str(indiceUv) + "."