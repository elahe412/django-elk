import logging
import pika

# class RabbitMQHandler(logging.Handler):
#
#     def __init__(self, host='192.168.206.136', port=5672, exchange='my_logs', routing_key='logstash'):
#         super().__init__()
#         try:
#             self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, heartbeat=600))
#             self.channel = self.connection.channel()
#             self.channel.exchange_declare(exchange=exchange, exchange_type='direct')
#             self.routing_key = routing_key
#
#         except pika.exceptions.AMQPConnectionError as e:
#             pass
#         except pika.exceptions.AMQPChannelError as e:
#             pass
#
#     # Handle channel errors
#     def emit(self, record):
#         message = self.format(record)
#         self.channel.basic_publish(exchange='my_logs', routing_key=self.routing_key, body=message)
#
#     def close(self):
#         self.connection.close()


import pika
import logging


class RabbitMQHandler(logging.Handler):
    def __init__(self, host='192.168.206.136', port=5672, exchange='my_logs', routing_key='logstash'):
        super().__init__()
        self.host = host
        self.port = port
        self.exchange = exchange
        self.routing_key = routing_key
        self.connection = None
        self.channel = None
        self.connect()

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, heartbeat=600))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type='direct')

    def emit(self, record):
        if not self.connection or self.connection.is_closed:
            self.connect()
        message = self.format(record)
        self.channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=message)

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
