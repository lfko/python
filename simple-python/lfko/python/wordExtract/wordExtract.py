'''
    @author: fbe
    @summary: Tool using regex to extract search terms from search queries
'''

import re
import csv
import pandas as pd

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

    return query


def findMatches(remainQuery):
    '''
        @summary: return all terms which are not enclosed by quotes (TODO: keep word coherence)
    '''
    query = removeAbbreviations(removeSpecialChars(removeParams(removeTwitter(remainQuery))))
    query = re.sub(r'(\sAND|\sand|\sNOT|\snot|\sOR|\sor|NEAR\/\d)', ')(', query)
    query = re.sub(r'(\s{2}[0-9][0-9]+){1}', '', query)
    # select everything inside parentheses
    query = '(' + query + ')'
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
    # return as a set so as to filter out duplicates
    return set(terms)



if __name__ == '__main__':
    '''
        @summary: main
    '''

    #fname = 'Searches_Automotive.csv'
    fname = 'Searches_Energy.csv'
    
    # read the csv file
    with open(fname) as csvfile:
        freader = csv.reader(csvfile)
        for row in freader:

            terms = findMatches(row[1])
            lt = list(terms)
            # add the keyword to the beginning of the list
            lt.insert(0, 'KW: ' + row[0])
            # print values tab separated
            print(*lt, sep='\t')
