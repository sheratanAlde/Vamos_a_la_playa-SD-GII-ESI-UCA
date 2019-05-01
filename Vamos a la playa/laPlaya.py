# -*- coding: utf-8 -*-
import requests

def datosPlaya():
    url = requests.get(url='https://apirtod.dipucadiz.es/api/datos/playas.json')

    print(url.json())