# -*- coding: utf-8 -*-
import json
import requests

API_KEY = '5b3ce3597851110001cf6248e3895e67daf9425ba50b55fb0df395d6'

def sitioCoordenadas(sitio):
    headers = {'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8'}

    call = requests.get(
        'https://api.openrouteservice.org/geocode/search/structured?'
        'api_key='+ API_KEY +'&'
        'region=Cádiz&'
        'locality='+ sitio +'&'
        'boundary.country=ES',
        headers=headers)

    #print(call.status_code, call.reason)
    #print(call.text)

    string_data = json.dumps(call.json())
    decode = json.loads(string_data)

    gps = decode['features'][0]['geometry']['coordinates']

    if (str(gps) == '[-5.883249, 36.55139]'):
        return "no se ha encontrado la población"
    else:
        return gps

def tiempoDistanciaRuta(origen, destino):
    poblacion = origen
    playa = destino

    body = {"locations": [poblacion, playa],
            "metrics":["distance","duration"],"resolve_locations":"true","units":"km"}

    headers = {'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
               'Authorization': API_KEY}

    call = requests.post('https://api.openrouteservice.org/v2/matrix/driving-car', json=body, headers=headers)

    #print(call.text)

    tiemoDistancia = json.dumps(call.json())
    datosTimpoDistancia = json.loads(tiemoDistancia)

    tiempo = datosTimpoDistancia['durations'][0][1]
    horas = int(tiempo/3600)
    minutos = int(tiempo/60)

    distancia = datosTimpoDistancia['distances'][0][1]

    #print("Población: " + str(poblacion))
    #print("Playa: " + str(playa))

    return "está a " + str(distancia) + " Km, " + "%s:%s" % (horas,minutos) + " aprox"