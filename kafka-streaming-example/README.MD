## How to setup the Apache Kafka environment via Docker (or maybe not) ##
1. Download a Kafka implementation (latest: 2.1.0)
2. Extract it: tar -xzf 
3a. Change to the newly extracted directories for starting the Kafka service (and the Zookeeper beforehand):
	-> ./bin/zookeeper-server-start.sh config/zookeeper.properties (starts a single-node preconfigured Zookeeper)
	-> ./bin/kafka-server-start.sh config/zookeeper.properties
3b. (verify, that everything is running just fine: netstat -pnlt | grep ':2181' AND ps aux | grep kafka
	
4a. Create a topic to which producers can communicated to: 
	-> ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic CS4BD
	>> Created topic "CS4BD".
4b. Look if everything was setup correctly: 
	->./bin/kafka-topics.sh --list --zookeeper localhost:2181
	>> CS4BD

## Let's get our hands dirty and write some python code! ##
The example uses the kafka-python implementation
1. sudo pip3.6 install kafka-python
2. Implement a very simple consumer (see kafka_consumer.py)
3. Test the consumer by sending messages to the topic via shell script:
	-> ./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic CS4BD 
	>>	>AAAAA
	>>  >BBBBB
	>>  >WWWWW
	
	... and the corresponding output from the python consumer:
	>> CS4BD:0:6: key=None value=b'AAAAA'
	>> CS4BD:0:7: key=None value=b'BBBBB'
	>> CS4BD:0:8: key=None value=b'WWWWW'


