'''
Created on Jan 24, 2019

@author: fb
'''

from pyspark import SparkContext, SparkConf

if __name__ == '__main__':
    conf = SparkConf().setAppName("create").setMaster("local")
    sc = SparkContext(conf=conf)
    
    inputStrings = ["Stefan 52", "Patrick 41", "Felix 43"]
    regularRDDs = sc.parallelize(inputStrings)
    
    # separate the strings into name and age
    pairRDDs = regularRDDs.map(lambda s: (s.split(" ")[0], s.split(" ")[1]))
    # coalesce - verbinden
    pairRDDs.coalesce(1).saveAsTextFile("out/myRegularRDD")
