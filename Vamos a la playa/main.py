import elTiempo
import laPlaya
import laRuta

if __name__ == "__main__":
    # dato = elTiempo.infoPlaya(1101203)
    # print(dato)

    #elTiempo.infoPlaya(1101203)
    #laPlaya.datosPlaya()
    try:
        print(laRuta.tiempoDistanciaRuta("San Fernando","Madrid"))

        #laRuta.sitioCoordenadas("Medina")
    except:
        print("el GPS esta recalculando")
