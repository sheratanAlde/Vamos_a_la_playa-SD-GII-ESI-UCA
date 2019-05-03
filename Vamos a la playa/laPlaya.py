# -*- coding: utf-8 -*-
import requests
import json
import csv
import re
from unicodedata import normalize

def limpiezCaracteres(poblacion):
    cadenaLimpia = poblacion.upper()

    cadenaLimpia = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize( "NFD", cadenaLimpia), 0, re.I)

    cadenaLimpia = normalize( 'NFC', cadenaLimpia)

    return cadenaLimpia

def calcularPlaya(origen, actividad):

    csvArchivo = 'PlayaTiempo.csv'

    if(actividad == ""):
        results = []
        with open(csvArchivo) as File:
            reader = csv.DictReader(File)
            for row in reader:
                results.append(row)
                if(row['Población'] == limpiezCaracteres(origen)):
                    print(row['Población'])
                    print(row['GPS'])


    limpiezCaracteres(origen)

def mostrarPlaya(nombre):
    url = requests.get(url='https://apirtod.dipucadiz.es/api/datos/playas.json')

    string_data = json.dumps(url.json())
    decode = json.loads(string_data)

    playas = decode['resources']


    for indice in range(0,int(decode['summary']['items']),1):
        if(playas[indice]['ca:nombre'] == nombre):
            gps = "["+ playas[indice]['ca:coord_latitud']+","+ playas[indice]['ca:coord_longitud']+"]"
            usos = playas[indice]['ca:usos']

        print(municipio + ";" + nombre + ";" + gps+ ";" + usos)

    return