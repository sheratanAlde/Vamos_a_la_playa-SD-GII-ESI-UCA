# -*- coding: utf-8 -*-
import requests
import json
import csv
import re
from unicodedata import normalize
import elTiempo
import laRuta


#Función que se encarga de dar un formato uniforme a la palabra que se le pasa
def limpiezCaracteres(poblacion):
    cadenaLimpia = poblacion.upper()

    cadenaLimpia = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize( "NFD", cadenaLimpia), 0, re.I)

    cadenaLimpia = normalize( 'NFC', cadenaLimpia)

    return cadenaLimpia


#Función que intercambia latitud con longitud al formato necesario para esta API
def transformacionCoordenadar(datos):
    gpsTransformacion = json.loads(datos)
    return json.loads("[" + str(gpsTransformacion[1]) + ", " + str(gpsTransformacion[0]) + "]")



#Retorna la puntuacion metereologica de una playa en caso de tener codigo de la AEMET
def puntuacionAEMET(row, maxPuntuacionTiempo, gpsPoblacion):
    if str(row['AEMET']).isnumeric():                                                                                   # Obtenemos la calificación del tiempo de esa playa
        puntuacion = elTiempo.situacionPlaya(row['AEMET'])
        if maxPuntuacionTiempo['puntuacion'] < puntuacion:                                                              # En el caso de tener una puntuación mayor sera la elegida
            maxPuntuacionTiempo['cod'] = row['AEMET']
            maxPuntuacionTiempo['puntuacion'] = puntuacion
            maxPuntuacionTiempo['GPS'] = transformacionCoordenadar(row['GPS'])                                          # Cambiamos el orden de la coordenadas
            ruta = laRuta.tiempoDistanciaRuta(gpsPoblacion, maxPuntuacionTiempo['GPS'])
            if ruta['error'] == "":
                maxPuntuacionTiempo['horas'] = ruta['tiempo']['horas']
                maxPuntuacionTiempo['minutos'] = ruta['tiempo']['minutos']
                maxPuntuacionTiempo['KM'] = ruta['distancia']
            else:
                maxPuntuacionTiempo['error'] = ruta['error']

    return maxPuntuacionTiempo


#Función que nos retorna las playas que tienen una actividad concreta
def actividadPlaya(actividad):
    listado = list()

    url = requests.get(url='https://apirtod.dipucadiz.es/api/datos/playas.json')

    string_data = json.dumps(url.json())
    decode = json.loads(string_data)

    playas = decode['resources']

    for indice in range(0, int(decode['summary']['items']), 1):
        nombre = playas[indice]['ca:nombre']
        municipio = playas[indice]['ca:municipio']
        gps = "[" + playas[indice]['ca:coord_latitud'] + "," + playas[indice]['ca:coord_longitud'] + "]"
        usos = playas[indice]['ca:usos']

        if usos != "Sin información relevante":
            usos = str(usos).replace('.', ',')                                                                          #Con estas lineas dejamos separadas las distintas actividades de cada playa
            usos = str(usos).replace('y', ',')
            usos = str(usos).split(',')
            usosMayus = str(usos).upper()
            actividadMayus = str(actividad).upper()

            if str(usosMayus).find(actividadMayus) > 0:
                listado.append(nombre)

    return listado


#Función que determina cual es la mejor playa para el usuario
def calcularPlaya(origen, actividad):

    csvArchivo = 'PlayaTiempo.csv'
    poblacion = limpiezCaracteres(origen)

    gpsPoblacion = laRuta.sitioCoordenadas(poblacion)
    maxPuntuacion = {"cod": 0, "puntuacion": 0, "GPS": "", "nombre": "",
                           "poblacion": gpsPoblacion, "KM": 0, "horas": 0, "minutos": 0,
                           "error": ""}

    if actividad == "":                                                                                                 #Si el usuario no ha especificado ningun tipo de actividad
        results = []
        poblacionPlaya = False                                                                                          #Bandera que nos indica si la poblacion donde se esta dispone de playa

        with open(csvArchivo) as File:                                                                                  #Abrimos nuestro fichero CSV guardado en local con los datos "estaticos"
            reader = csv.DictReader(File)

            for row in reader:                                                                                          #Vamos tratando la información del fichero por linea
                results.append(row)

                if row['Población'] == poblacion:                                                                       #Comrpobamos si el usuario se encuentra en una localidad con playa
                    poblacionPlaya = True
                    codAEMET = row['AEMET']
                    maxPuntuacion['nombre'] = row['Playa']
                    maxPuntuacion = puntuacionAEMET(row, maxPuntuacion, gpsPoblacion)

        if poblacionPlaya is False:
            distanciaMenor = 2000
            with open(csvArchivo) as File:                                                                              # Abrimos nuestro fichero CSV guardado en local con los datos "estaticos"
                reader = csv.DictReader(File)

                for row in reader:                                                                                      # Vamos tratando la información del fichero por linea
                    results.append(row)
                    distancia = abs(abs(gpsPoblacion[0]) - abs(transformacionCoordenadar(row['GPS'])[0])) + \
                                abs(abs(gpsPoblacion[1]) - abs(transformacionCoordenadar(row['GPS'])[1]))               #Calculamos la distancia de todas las playas respecto a la localidad

                    if distancia < distanciaMenor:                                                                      #Se recomendará la playa mas cercana a la localidad
                        maxPuntuacion['cod'] = row['AEMET']
                        maxPuntuacion['nombre'] = row['Playa']
                        maxPuntuacion['GPS'] = transformacionCoordenadar(row['GPS'])
                        distanciaMenor = distancia

            if maxPuntuacion['cod'] != '':
                maxPuntuacion = puntuacionAEMET(row, maxPuntuacion,gpsPoblacion)
    else:
        results = []
        playas = actividadPlaya(actividad)

        with open(csvArchivo) as File:                                                                                  # Abrimos nuestro fichero CSV guardado en local con los datos "estaticos"
            reader = csv.DictReader(File)

            for row in reader:                                                                                          # Vamos tratando la información del fichero por linea
                results.append(row)
                if playas.count(row['Playa']):

                    if row['AEMET'] != '':
                        maxPuntuacion['nombre'] = row['Playa']
                        maxPuntuacion = puntuacionAEMET(row, maxPuntuacion, gpsPoblacion)

    print(maxPuntuacion)

    tiempoDistancia = "(a "
    if maxPuntuacion['horas'] != 0:
        tiempoDistancia += str(maxPuntuacion['horas'])+" H y "
    tiempoDistancia+= str(maxPuntuacion['minutos'])+" min, "+str(maxPuntuacion['KM'])+" km)"

    respuesta = "la mas cercana a tu ubicación es "+maxPuntuacion['nombre']+tiempoDistancia
    if maxPuntuacion['cod'] != '':
        respuesta += " "+elTiempo.infoPlaya(maxPuntuacion['cod'])+""

    return respuesta