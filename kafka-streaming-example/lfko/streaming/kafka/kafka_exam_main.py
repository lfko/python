'''
Created on Dec 22, 2018

@author: fb
'''

from lfko.streaming.kafka.kafka_consumer import TopicConsumer
from lfko.streaming.kafka.kafka_producer import TopicProducer


def main():
    """ """
    topic = 'CS4BD'
    my_producer1 = TopicProducer(topic)
    my_producer1.writeToTopic('msg', 10)
    
    my_consumer = TopicConsumer(topic)
    my_consumer.readFromTopic()


if __name__ == '__main__':
    main()
