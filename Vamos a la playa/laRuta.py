# -*- coding: utf-8 -*-
import json
import requests

API_KEY = '5b3ce3597851110001cf6248e3895e67daf9425ba50b55fb0df395d6'

def sitioCoordenadas(sitio):
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    call = requests.get(
        'https://api.openrouteservice.org/geocode/search?api_key='+ API_KEY +'&text=San%20Fernando&boundary.country=ES',
        headers=headers)

    print(call.status_code, call.reason)
    print(call.text)

    string_data = json.dumps(call.json())
    decode = json.loads(string_data)

    return decode

def tiempoDistanciaRuta(origen, destino):
    poblacion = sitioCoordenadas(origen)
    playa = sitioCoordenadas(destino)

    body = {"locations":[[poblacion['elements'][0]["lat"],poblacion['elements'][0]["lon"]],
                         [playa['elements'][0]["lat"],playa['elements'][0]["lon"]]],
            "metrics":["distance","duration"],"resolve_locations":"true","units":"km"}

    headers = {'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
               'Authorization': API_KEY}

    call = requests.post('https://api.openrouteservice.org/v2/matrix/driving-car', json=body, headers=headers)

    print(call.text)

    tiemoDistancia = json.dumps(call.json())
    datosTimpoDistancia = json.loads(tiemoDistancia)

    print(datosTimpoDistancia['durations'][0][1])
    print(datosTimpoDistancia['distances'][0][1])
    print("Población: " + str(poblacion['elements'][0]["lat"]) + "," + str(poblacion['elements'][0]["lon"]))
    print("Playa: " + str(playa['elements'][0]["lat"]) + "," + str(playa['elements'][0]["lon"]))


#https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf6248e3895e67daf9425ba50b55fb0df395d6&text=San%20Fernando&boundary.country=ES
#https://github.com/mvexel/overpass-api-python-wrapper
#https://github.com/cglacet/osrm_plus