'''
    @author: fbe
    @summary: Tool using regex to extract search terms from search queries
'''

import re
import csv
import pandas as pd


def extractWord(row):
    '''
    '''
    # print('row before: ', row)
    # pattern = re.compile(r'[\u00C0-\u017Fa-zA-Z0-9]*[\u00C0-\u017Fa-zA-Z][\u00C0-\u017Fa-zA-Z0-9]*')
    # pattern = re.compile(r'(\W*\s[0-9]+){1}')
    # pattern to find only number-strings; they shall be excluded
    pattern = re.compile(r'(\s{2}[0-9][0-9]+){1}')
    word = pattern.findall(row)
    ret = []

    if(len(word) > 0):
        for match in word:
            row = row.replace(match, '')
            # print('row after: ', row)
            # ret = row.split()
    # else:
        # ret = row.split()

    # pattern = re.compile(r'(["]{1}[\w|\s]*["]{1})')
    '''
        find words, which are enclosed with quotation marks (e.g. "Foo Bar Faz")
        they will be extracted and removed afterwards from the string
    '''
    # pattern = re.compile(r'(["]{1}[\w]+[\w|\s]+["]{1})', re.UNICODE)
    pattern = re.compile(r'".*?.*?"', re.UNICODE)
    quoted_terms = []
    ret = pattern.findall(row)
    for match in ret:
        quoted_terms.append(match)
        row = row.replace(match, '')

    ret = row.split()
    [ret.append(x) for x in quoted_terms]

    ret = list(map(lambda x: x.replace('"', ''), ret))
    ret = [x for x in ret if x != '']

    # return as set so that only unique values are included
    return set(ret)


def applyRegEx(currRow):
    '''

    '''
    
    re.findall(r'(.+?(?=\sAND\s|\sand\s|\sOR\s|\sor\s))', currRow)
    
    # remove logical operators
    row = re.sub(r'(\s*NOT)*(\s(N|n)ot\s)*((\s|\W)AND)*((\s|\W)(A|a)nd)*(\sOR)*(\sor)*((\s|\W)NEAR\/(\d|\w|\s|\W))*((\s|\W)NEXT\/\d+)*', '', currRow)

    # remove country abbreviation (.de, .ch)
    row = re.sub(r'(.\w\w\/)', '', row)
    
    # remove gender m/w
    row = re.sub(r'(\w\/\w)', '', row)

    # remove rt|RT - which means retweet
    row = re.sub(r'("rt|"RT)', '', row)

    # remove strings like field=xxx
    # row = re.sub(r'([a-z]+=["]*?[a-z\s]+["]*?)',' ', row)
    row = re.sub(r'(:?[a-z]*\s?[a-z]+=["]*?[a-z\s]+["]*)', ' ', row)

    # remove twitter handles (e.g. @rwe_ag)
    row = re.sub(r'(@\w+.\w+)', '', row)

    # remove special characters
    row = re.sub(r'[^\u00C0-\u017Fa-zA-Z0-9-"&|,.+_\s]', ' ', row, re.UNICODE)

    return row


# fname = 'Searches_Automotive.csv'
fname = 'Searches_Energy.csv'
# read the csv file
with open(fname) as csvfile:
    freader = csv.reader(csvfile)
    for row in freader:
        print('keyword: ', row[0])
        print("k \t {:^10}   \t {:^25}   \t {:^15}".format("Best point", "Good point", "Worst point"))
        # print(extractWord(applyRegEx(row[1])))

