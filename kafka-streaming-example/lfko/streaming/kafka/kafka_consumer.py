'''
Created on Dec 22, 2018

@author: fb
'''

from kafka import KafkaConsumer


class TopicConsumer():
    '''
        Will consume a Kafka topic
    '''

    def __init__(self, topic):
        '''
        Constructor
        '''
        self.topic = topic
        self.consumer = self.__connect__()
        
    def __connect__(self, host='localhost', port=2181):
        """ """
        # return KafkaConsumer(self.topic, bootstrap_servers=host + ':' + str(port))
        # creating a new KafkaConsumer instance, listening on the supplied topic (with an additional timeout of 10s))
        return KafkaConsumer(self.topic, consumer_timeout_ms=10000)
        
    def readFromTopic(self):
        """ """
        for message in self.consumer:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))    
