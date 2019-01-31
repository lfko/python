'''
Created on Dec 22, 2018

@author: fb
'''
from lfko.streaming.kafka import kafka_consumer, kafka_producer

from queue import Queue
# from threading import Thread


def main():
    """ """

    queue = Queue()  # for communication with worker threads
    
    for x in range(2):
    
        worker = kafka_producer.TopicProducer(kafka_params=['localhost', '9092'], queue=queue, prod_id=x)
        worker.daemon = True
        worker.start()
    
    topic = 'CS4BD'
    queue.put((topic, 20, True))  # even number producer
    queue.put((topic, 10, False))  # odd number producer

    # queue.join()

    worker_consumer = kafka_consumer.TopicConsumer(kafka_params=['localhost', '9092'], queue=queue, topic=topic)
    worker_consumer.daemon = True
    worker_consumer.start()
    # queue.put((topic))

    queue.join()


if __name__ == '__main__':
    main()
