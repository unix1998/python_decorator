#! /home/mxu/python3/mxu_pica/bin/python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello_2_mxu')
channel.basic_publish(exchange='', routing_key='hello_2_mxu', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

