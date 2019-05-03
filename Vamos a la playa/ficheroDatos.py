import requests
import json

def gpsDecimal(dato):
    separado = dato.split(" ")

    grados = separado[0][:str(separado).find("º")-2]
    minutos = separado[1][0:2]
    segundos = separado[2][0:2]

    gps =int(grados) + int(minutos)/60 + int(segundos)/3600

    return str(gps)

def tiempoPlaya():
    archivoCsvAEMET = "http://www.aemet.es/documentos/es/eltiempo/prediccion/playas/Playas_codigos.csv"

    csvfile =  requests.get(archivoCsvAEMET)

    filas = csvfile.text.split('\r\n')

    for fila in filas:
        if(fila.find("Cádiz") > 0):
            datos = fila.split(';')
            print(datos[0]+";"+datos[1]+";"+datos[5])

def datosPlaya():
    url = requests.get(url='https://apirtod.dipucadiz.es/api/datos/playas.json')

    string_data = json.dumps(url.json())
    decode = json.loads(string_data)

    playas = decode['resources']

    infoPlayas = "{\"playas\": ["
    for indice in range(0,int(decode['summary']['items']),1):
        municipio = playas[indice]['ca:municipio']
        nombre = playas[indice]['ca:nombre']
        gps = "["+ playas[indice]['ca:coord_latitud']+","+ playas[indice]['ca:coord_longitud']+"]"
        usos = playas[indice]['ca:usos']

        infoPlayas = infoPlayas + "{\"municipio\": \""+municipio+"\"," \
                                    "\"nombre\": \""+nombre+"\"," \
                                    "\"gps\": \""+gps+"\"," \
                                    "\"usos\": \""+usos+"\"},"

        #print(municipio + ";" + nombre + ";" + gps)

    infoPlayas = str(infoPlayas)[:len(infoPlayas)-1] + "]}"

    return infoPlayas

print(datosPlaya())
print(tiempoPlaya())
