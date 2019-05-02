import elTiempo
import laPlaya
import laRuta

if __name__ == "__main__":
    # dato = elTiempo.infoPlaya(1101203)
    # print(dato)

    #elTiempo.infoPlaya(1101203)
    #laPlaya.datosPlaya()
    try:
        print(laRuta.tiempoDistanciaRuta("San Fernando","El Carmen"))
    except:
        print("el GPS esta recalculando")
