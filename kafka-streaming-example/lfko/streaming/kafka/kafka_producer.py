'''
    Created on Dec 22, 2018

    @author: fb
'''
from kafka import KafkaProducer
from time import sleep
from threading import Thread


class TopicProducer(Thread):
    '''
        Will write to a Kafka topic
    '''

    def __init__(self, queue, kafka_params, prod_id):
        '''
            Constructor
        '''
        print('producer_id ', prod_id)
        Thread.__init__(self)
        self.queue = queue
        self.prod_id = prod_id
        self.producer = self.__connect__(kafka_params)
    
    def __connect__(self, kafka_params):

        return KafkaProducer(bootstrap_servers=[':'.join(kafka_params)])

    def run(self):
        while True:
            
            # retrieve the parameters from the queue
            topic, n, even = self.queue.get()
            print('params: topic {0} n {1} even {2} '.format(topic, n, even))
           
            try:
                for i in range(n):
                    # somewhat straightforward way to distinguish between even and odd numbers
                    if(even == True and n % 2 == 0):
                        self.producer.send(topic, key=b'producer %d' % self.prod_id , value=b'even')
                        self.producer.send(topic, b'msg %d' % i)
                    elif (even == False and n % 2 == 1):
                        self.producer.send(topic, b'msg %d' % i)
                        self.producer.send(topic, key=b'producer %d' % self.prod_id, value=b'odd')
                    
                    sleep(1)  # sleeps 1 second
            finally:
                self.queue.task_done()
