import pika, json

params = pika.URLParameters('amqps://zrizjelx:5a-2hcXtDjsYZuwtTW9pvTc1B0BvGuxG@codfish.rmq.cloudamqp.com/zrizjelx')
# your rabbitmq url

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
