# -*- coding: utf-8 -*-
import json
import requests

API_KEY = '5b3ce3597851110001cf6248e3895e67daf9425ba50b55fb0df395d6'                                                    #Key de la API


#Indicandole el nombre de una población devuelve la posición gps de la misma(SOLO PROVINCIA DE CÁDIZ)
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

    gps = "["+str(decode['features'][0]['geometry']['coordinates'][1])+", "\
          +str(decode['features'][0]['geometry']['coordinates'][0])+"]"

    if str(gps) == '[36.55139, -5.883249]':                                                                           #Cuando no encuentra la localidad solicitada siempre retorna esta posición, la cual devuelve como error
        return "no se ha encontrado la población"
    else:
        return json.loads(gps)


#Función que calcula la distancia y el tiempo que se tarda en realizar el camino desde el origen(dato en gps) y el destino(dato en gps)
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
    datosTiempoDistancia = json.loads(tiemoDistancia)

    tiempo = datosTiempoDistancia['durations'][0][1]
    horas = int(tiempo/3600)
    minutos = int(tiempo/60)


    #print("Población: " + str(poblacion))
    #print("Playa: " + str(playa))

    return {"distancia": distancia, "tiempo": {"horas": horas, "minutos": minutos}}