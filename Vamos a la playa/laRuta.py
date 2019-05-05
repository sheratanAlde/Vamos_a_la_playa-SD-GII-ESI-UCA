# -*- coding: utf-8 -*-
import json
import requests

API_KEY = '5b3ce3597851110001cf624833c10ecb4a2e450d90e0e6be1dca7c31'                                                    #Key de la API


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

    gps = "["+str(decode['features'][0]['geometry']['coordinates'][0])+", "\
          +str(decode['features'][0]['geometry']['coordinates'][1])+"]"

    if str(gps) == '[-5.883249, 36.55139]':                                                                           #Cuando no encuentra la localidad solicitada siempre retorna esta posición, la cual devuelve como error
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

    tiempoDistancia = json.dumps(call.json())
    datosTiempoDistancia = json.loads(tiempoDistancia)

    distancia = datosTiempoDistancia['distances'][0][1]

    if distancia is not None:
        tiempo = datosTiempoDistancia['durations'][0][1]
        horas = int(tiempo/3600)
        minutos = int(tiempo/60)

        #print("Población: " + str(poblacion))
        #print("Playa: " + str(playa))

        return {"error": "", "distancia": distancia, "tiempo": {"horas": horas, "minutos": minutos}}
    else:
        return {"error": " batería baja en el GPS.", "distancia": 0, "tiempo": {"horas": 0, "minutos": 0}}