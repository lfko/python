'''
Created on Jan 24, 2019

@author: fb
'''

import os
from pip._vendor.colorama.ansi import Back
from pyspark import SparkConf, SparkContext


def main():
    """
        @summary: plain main method
    """
    
    file_out_name = 'out/word_counts'
    
    sparkCtx = initSpark()
    
    myRDD = readFile(sparkCtx, "t8.shakespeare.txt")
    wordCounts = myRDD.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)

    # sort by values descending
    wcByValue = wordCounts.sortBy(lambda wordCounts: wordCounts[1], ascending=False)
    
    # print on console
    # printResult(wcByValue)
    
    # print the result to a file    
    wcByValue.coalesce(1).saveAsTextFile(file_out_name)


def printResult(resRDD):
    """
        @summary: prints out the resulting tuples
    """
    for word, count in resRDD.collect():
        print("{} : {} ".format(word, count))


def prepFile(fname, start, stop):
    """
        @summary: removing lines from a file, beginning by @start, ending by @stop
        @param fname: filename
        @param start: line number to start
        @param stop: line number to stop
    """
    import fileinput

    for line in fileinput.input(fname, inplace=1, backup='.orig'):
        if start <= fileinput.lineno() < start + stop:
            pass
        else:
            print(line[:-1])
     
    fileinput.close()


def readFile(sc, filename):
    """
        @summary: reads in a file with the given name and returns a RDD
        @param sc: SparkContext
    """
    
    # fname = 'in/numbers.txt'
    prepFile("in/" + filename, 0, 243)
        
    return sc.textFile("in/" + filename)


def initSpark():
    """
        @summary: initialises the SparkContext
    """
    conf = SparkConf().setAppName("CountWords").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    return sc


if __name__ == '__main__':
    main()
