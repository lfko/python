##
##  Apache Spark
##  toy example
##  FB 24.01.2019

Install Apache Spark via Docker:
1. using the gettyimages/spark image: docker pull gettyimages/spark
2. install docker-compose: sudo apt install docker-compose
3. cloning the github repository and running docker-compose up
4. it now starts (-d for non-verbose mode)

pyspark
1. sudo pip3.6 install pyspark

The written python code can be found in the repository (counts_words_app.py)

## the 24 most used words
('', 516057) # not actually a word 
1. ('the', 23160)
    ('I', 19529)
    ('and', 18241)
    ('to', 15563)
    ('of', 15487)
    ('a', 12508)
    ('my', 10818)
    ('in', 9540)
    ('you', 9052)
    ('is', 7825)
    ('that', 7502)
    ('And', 7049)
    ('not', 6934)
    ('with', 6702)
    ('his', 6206)
    ('your', 5996)
    ('be', 5979)
    ('for', 5591)
    ('have', 5230)
    ('it', 4896)
    ('me', 4832)
    ('this', 4756)
    ('he', 4543)
24. ('as', 4262)