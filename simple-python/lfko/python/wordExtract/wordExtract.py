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
    row = re.sub(r'(\s*NOT)*(\s(N|n)ot\s)*((\s|\W)AND)*((\s|\W)(A|a)nd)*(\sOR)*(\sor)*((\s|\W)NEAR\/(\d|\w|\s|\W))*((\s|\W)NEXT\/\d+)*', ')(', currRow)

    # remove country abbreviation (.de, .ch)
    row = re.sub(r'(.\w\w\/)', '', row)
    
    # remove gender m/w
    row = re.sub(r'(\w\/\w)', '', row)

    # remove rt|RT - which means retweet
    row = re.sub(r'("rt|"RT)', '', row)

    # remove strings like field=xxx
    row = re.sub(r'(:?[a-z]*\s?[a-z]+=["]*?[a-z\s]+["]*)', ' ', row)

    # remove twitter handles (e.g. @rwe_ag)
    row = re.sub(r'(@\w+.\w+)', '', row)

    # remove special characters
    row = re.sub(r'[^\u00C0-\u017Fa-zA-Z0-9-"&|,.+_\s]', ' ', row, re.UNICODE)

    return row


def removeAbbreviations(query):
    '''
        @summary: remove abbreviations like country codes or gender
    '''
    # remove country abbreviation (.de, .ch)
    query = re.sub(r'(\.\w\w\/)', '', query)
    
    # remove gender m/w
    query = re.sub(r'(\w\/\D)', '', query)

    # print('removeAbbreviations: ', query)
    return query


def removeSpecialChars(query):
    '''
        @summary: remove special characters
    '''
    query = re.sub(r'[^\u00C0-\u017Fa-zA-Z0-9-"&|,.+/_\s]', ' ', query, re.UNICODE)

    # print('removeSpecialChars: ', query)
    return query


def removeParams(query):
    '''
        @summary: remove strings like field=xxx
    '''
    query = re.sub(r'(:?[a-z]*\s?[a-z]+=["]*?[a-z\s]+["]*)', ' ', query)

    # print('removeParams: ', query)
    return query


def removeTwitter(query):
    '''
        @summary: remove twitter-related entries from the query
    '''
    # remove twitter handles (e.g. @rwe_ag)
    query = re.sub(r'(@\w+.\w+)', '', query)
        
    # remove rt|RT - which means retweet
    query = re.sub(r'("rt|"RT)', '', query)

    # print('removeTwitter: ', query)
    return query


def findQuoted(query):
    '''
        @summary: return all terms which are enclosed by quotes ('" "')
    '''
    query = removeSpecialChars(removeAbbreviations(removeParams(removeTwitter(query))))
    pattern = re.compile(r'".*?.*?"', re.UNICODE)

    foundTerms = []
    matches = pattern.findall(query)
    for match in matches:
        # write the found term into a list
        term = match.replace('"', '')
        foundTerms.append(term.strip())
        # remove it from the query afterwards
        query = query.replace(match, '')
    
    return foundTerms, query


def findNonQuoted(remainQuery):
    '''
        @summary: return all terms which are not enclosed by quotes (TODO: keep word coherence)
    '''
    # print('findNonQuoted remainQuery: ', remainQuery)
    query = removeAbbreviations(removeSpecialChars(removeParams(removeTwitter(remainQuery))))
    # print('Query beforeBefore: ', query)
    query = re.sub(r'(\sAND|\sand|\sNOT|\snot|\sOR|\sor|NEAR\/\d)', ')(', query)
    query = re.sub(r'(\s{2}[0-9][0-9]+){1}', '', query)
    # select everything inside parentheses
    query = '(' + query + ')'
    # print('Query before: ', query)
    terms = []
    pattern = re.compile(r'\((.*?)\)', re.UNICODE)
    matches = pattern.findall(query)
    for match in matches:

        # write the found term into a list
        term = match.replace('"', '')
        terms.append(term.strip())
        for te in term.strip().split():
            terms.append(te)
        # remove it from the query afterwards
        query = query.replace(match, '')
    
    terms = [t for t in terms if t != '']
    return set(terms)
    # print(matches)
    # print('Remaining Query: ', remainQuery)


if __name__ == '__main__':
    '''
        @summary: main
    '''

    fname = 'Searches_Automotive.csv'
    # fname = 'Searches_Energy.csv'
    
    # read the csv file
    with open(fname) as csvfile:
        freader = csv.reader(csvfile)
        for row in freader:
            print('Keyword: ', row[0])
            print('Row: ', row[1])
            # terms, remainQuery = findQuoted(row[1])
    # terms, remainQuery = findQuoted('((Strom NEAR/3 Preis*) OR Strompreis*) NEAR/5 (*entwicklung* OR *entwickel* OR Prognose* OR steig* OR fall* OR sink* OR Kurs) OR Strompreisentwicklung*')
            terms = findNonQuoted(row[1])
            print(terms)
            # print('keyword: ', row[0])
            # print("k \t {:^10}   \t {:^25}   \t {:^15}".format("Best point", "Good point", "Worst point"))
            # print(extractWord(applyRegEx(row[1])))

