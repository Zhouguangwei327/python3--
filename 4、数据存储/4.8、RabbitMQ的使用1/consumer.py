import pika


QUEUE_NAME = 'scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

# 回调函数
# def callback(ch, nethod, properties, body):
#     print(body)
    
# 获取数据
while True:
    input()
    method_frame, header, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
    if body:
        print(body)

