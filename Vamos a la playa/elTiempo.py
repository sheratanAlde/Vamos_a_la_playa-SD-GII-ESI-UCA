# -*- coding: utf-8 -*-
from aemet import Aemet
import json
from datetime import datetime, date, time, timedelta

def calculoOleaje(dato):


def situacionPlaya(codPlaya):
    ahora = datetime.now()

    aemet = Aemet()
    playa = aemet.get_prediccion_especifica_playa(cod)
    data_string = json.dumps(playa)
    decode = json.loads(data_string)
    datosActual = decode['prediccion']['dia'][0]

    if(ahora.hour() > 14):
        cielo = datosActual['estadoCielo']['descripcion2']
        viento = datosActual['viento']['descripcion2']
        oleaje = datosActual['oleaje']['descripcion2']
    else:
        cielo = datosActual['estadoCielo']['descripcion1']
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
    playa = aemet.get_prediccion_especifica_playa(cod)
    data_string = json.dumps(playa)
    decode = json.loads(data_string)
    datosActual = decode['prediccion']['dia'][0]

    # if hora > 14  en 24

    #else
    cielo = datosActual['estadoCielo']['descripcion2']
    viento = datosActual['viento']['descripcion2']
    oleaje = datosActual['oleaje']['descripcion2']

    temperaturaMaxima = datosActual['tMaxima']['valor1']
    sensacionTermica = datosActual['sTermica']['descripcion1']
    temperaturaAgua = datosActual['tAgua']['valor1']
    indiceUv = datosActual['uvMax']['valor1']

    print("EL cielo esta " + cielo + " con un viento " + viento + ", por lo que el oleaje es " + oleaje + ", la temperatura es de "
          + str(temperaturaMaxima) + ", mientras que la sensación termica es " + str(sensacionTermica) + " y la temperatura del agua "
          + str(temperaturaAgua) + ", pero cuidado que el indice UV es de " + str(indiceUv) + ".")


# str | Código de playa http://www.aemet.es/documentos/es/eltiempo/prediccion/playas/Playas_codigos.csv
#https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html
#http://jsonviewer.stack.hu/
#http://www.aemet.es/es/eltiempo/prediccion/playas/la-victoria-1101203