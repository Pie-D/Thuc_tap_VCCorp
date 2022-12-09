import pika

# ket noi voi may chu PrabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# tao ra mot hang doi, de dam bao rang hang doi da ton tai
channel.queue_declare(queue='hello')

#publish tin nhan bang exchange mac dinh, tin nhan duoc gui den queue: 'hello' voi noi dung 'Hello World' 
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print("[x] Sent 'Hello World!'")
connection.close()
