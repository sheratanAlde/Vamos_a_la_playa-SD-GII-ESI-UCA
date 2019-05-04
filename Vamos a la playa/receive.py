import pika
import TwittearListaCompra
import Tw_ComandoInvalido
import TwittearPrecioCompra


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='peticionesOK')
channel.queue_declare(queue='error')

def callbackPeticionesOK(ch, method, properties, body):
    print(body)
    Tw_responder.Tw_responder(body)

channel.basic_consume(callbackPeticionesOK,
                      queue='peticionesOK',
                      no_ack=True)

def callbackError(ch, method, properties, body):
    print(body)
    Tw_responder.Tw_responder(body)

channel.basic_consume(callbackError,
                      queue='error',
                      no_ack=True)

print(' [*] Esperando mensajes. Para salir, pusla CTRL+C')
channel.start_consuming()