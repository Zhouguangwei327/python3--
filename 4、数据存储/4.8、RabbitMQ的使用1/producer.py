import pika

QUEUE_NAME = 'scrape'
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

# 添加数据
while True:
    data = input()
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=data)
    print(data)