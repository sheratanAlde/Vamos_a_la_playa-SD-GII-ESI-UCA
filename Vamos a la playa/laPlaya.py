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


#Función que determina cual es la mejor playa para el usuario
def calcularPlaya(origen, actividad):

    csvArchivo = 'PlayaTiempo.csv'
    poblacion = limpiezCaracteres(origen)

    gpsPoblacion = laRuta.sitioCoordenadas(poblacion)
    maxPuntuacionTiempo = {"cod": 0, "puntuacion": 0, "GPS": "", "poblacion": gpsPoblacion, "KM": 0, "horas": 0, "minutos": 0}

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

                    if str(codAEMET).isnumeric():                                                                       #Obtenemos la calificación del tiempo de esa playa
                        puntuacion = elTiempo.situacionPlaya(codAEMET)
                        if maxPuntuacionTiempo['puntuacion'] < puntuacion:                                              #En el caso de tener una puntuación mayor sera la elegida
                            maxPuntuacionTiempo['cod'] = codAEMET
                            maxPuntuacionTiempo['puntuacion'] = puntuacion
                            maxPuntuacionTiempo['GPS'] = row['GPS']
                            ruta = laRuta.tiempoDistanciaRuta(gpsPoblacion,json.loads(row['GPS']))
                            maxPuntuacionTiempo['horas'] = ruta['tiempo']['horas']
                            maxPuntuacionTiempo['minutos'] = ruta['tiempo']['minutos']
                            maxPuntuacionTiempo['KM'] = ruta['distancia']

        if poblacionPlaya is False:
            with open(csvArchivo) as File:                                                                              # Abrimos nuestro fichero CSV guardado en local con los datos "estaticos"
                reader = csv.DictReader(File)

                for row in reader:                                                                                      # Vamos tratando la información del fichero por linea
                    results.append(row)
                    codAEMET = row['AEMET']


                    if str(codAEMET).isnumeric():                                                                       # Obtenemos la calificación del tiempo de esa playa
                        puntuacion = elTiempo.situacionPlaya(codAEMET)
                        if maxPuntuacionTiempo[
                            'puntuacion'] < puntuacion:                                                                 # En el caso de tener una puntuación mayor sera la elegida
                            maxPuntuacionTiempo['cod'] = codAEMET
                            maxPuntuacionTiempo['puntuacion'] = puntuacion
                            maxPuntuacionTiempo['GPS'] = row['GPS']

        #print(str(maxPuntuacionTiempo['cod'])+" "+str(maxPuntuacionTiempo['puntuacion'])+" "+str(maxPuntuacionTiempo['GPS']))
    else:
        print(actividad)
    print(maxPuntuacionTiempo)

def mostrarplaya(nombre):
    url = requests.get(url='https://apirtod.dipucadiz.es/api/datos/playas.json')

    string_data = json.dumps(url.json())
    decode = json.loads(string_data)

    playas = decode['resources']

    for indice in range(0,int(decode['summary']['items']),1):

        if playas[indice]['ca:nombre'] == nombre:
            municipio = playas[indice]['ca:municipio']
            gps = "["+ playas[indice]['ca:coord_latitud']+","+ playas[indice]['ca:coord_longitud']+"]"
            usos = playas[indice]['ca:usos']

        print(municipio + ";" + nombre + ";" + gps+ ";" + usos)

    return