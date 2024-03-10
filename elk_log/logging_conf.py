import logging
import pika


class RabbitMQHandler(logging.Handler):

    def __init__(self, host='192.168.206.136', port=5672, exchange='my_logs', routing_key='logstash'):
        super().__init__()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=exchange, exchange_type='direct')
        self.routing_key = routing_key

    def emit(self, record):
        message = self.format(record)
        self.channel.basic_publish(exchange='my_logs', routing_key=self.routing_key, body=message)

    def close(self):
        self.connection.close()
