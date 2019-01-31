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

## To do it with docker eventually (great tutorial: https://jaceklaskowski.gitbooks.io/apache-kafka/kafka-docker.html)
(using the wurstmeister/kafka image for running both kafka and the zookeeper in separate container)
1. clone the repository to the local machine: https://github.com/wurstmeister/kafka-docker
2. open shell and change to the directory
3. execute docker-compose up
4. (many things will happen)
5. kafka_1      | [2019-01-31 12:52:13,798] INFO [KafkaServer id=1001] started (kafka.server.KafkaServer)
6. test the connection:

	lfko@Sartre ~ $ sudo nc -vz localhost 9092
	Connection to localhost 9092 port [tcp/*] succeeded!


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


