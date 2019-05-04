import pika
import sys
import Tw_lector

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

if __name__ == "__main__":

        channel.queue_declare(queue='peticionesOK')
        channel.queue_declare(queue='error')


        twitterStream = LectorTwitter.crearListener()
        twitterStream.filter(track=["@Go_to_the_beach"])

        print(" [x] Sent %r" % message)
        connection.close()
