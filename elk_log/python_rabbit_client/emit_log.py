import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.206.136',port=5672))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [x] Sent {message}")
connection.close()