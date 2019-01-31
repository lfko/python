'''
    Created on Dec 22, 2018

    @author: fb
'''

from kafka import KafkaConsumer
from threading import Thread


class TopicConsumer(Thread):
    '''
        Will consume a Kafka topic
    '''

    def __init__(self, queue, kafka_params, topic):

        Thread.__init__(self)
        self.queue = queue
        
        self.consumer = self.__connect__(kafka_params, topic)
        
    def __connect__(self, kafka_params, topic):
        """ """
        # return KafkaConsumer(self.topic, bootstrap_servers=host + ':' + str(port))
        # creating a new KafkaConsumer instance, listening on the supplied topic (with an additional timeout of 10s))
        return KafkaConsumer(topic, consumer_timeout_ms=10000, bootstrap_servers=[':'.join(kafka_params)])

    def run(self):
        while True:
            try:
                for message in self.consumer:
                    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))
                    # print (message.headers)
                    # print('Received message: {0}'.format(message.value()))    
            finally:
                self.queue.task_done()
