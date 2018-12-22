'''
Created on Dec 22, 2018

@author: fb
'''
from kafka import KafkaProducer


class TopicProducer():
    '''
        Will write to a Kafka topic
    '''

    def __init__(self, topic):
        '''
        Constructor
        '''
        self.producer = self.__connect__()
        self.topic = topic
    
    def __connect__(self, host='localhost', port=2181):
        """ """
        # do something
        return KafkaProducer()

    def writeToTopic(self, msg, times=1):
        """  """
        for i in range(times):
            self.producer.send(self.topic, b'msg %d' % i)
        
