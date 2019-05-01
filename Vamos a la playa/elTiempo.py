# -*- coding: utf-8 -*-
from aemet import Aemet
import json

def infoPlaya(cod):
    aemet = Aemet()
    playa = aemet.get_prediccion_especifica_playa(cod)
    data_string = json.dumps(playa)
    decode = json.loads(data_string)
    #print(aemet.get_prediccion(11012))
    #print(aemet.get_municipio("Puerto Real"))
    #print(decode)
    datosActual = decode['prediccion']['dia'][0]

    #print(datosActual)
    # if hora > 12  en 24

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