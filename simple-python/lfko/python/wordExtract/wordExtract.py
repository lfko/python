'''
    @author: fbe
    @summary: Tool using regex to extract search terms from search queries
'''

import re
import csv
import pandas as pd

import rdflib as rdf
from pprint import pprint

from urllib.request import urlopen
from urllib.parse import quote_plus
import json
import codecs


def synonyms(term,lang = None):
    
    if not lang == None:
        langFilter = """?rel2 ?name FILTER ( lang(?name)="%s" ).""" % lang
        goalTerm = """"%s"@%s""" % (term,lang)
    else:
        langFilter = ""
        goalTerm = "\"%s\"" % term
    
    query = """SELECT DISTINCT ?target ?name WHERE {
            VALUES ?rel {rdfs:label  skos:altLabel}
            VALUES ?rel2 {rdfs:label skos:altLabel}
            ?target ?rel %s;
            %s
            FILTER ( ?rel != ?rel2) }""" % (goalTerm,langFilter)
    
    return query

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

def processRow(row):
    lsTerms = []
    # read the csv file
    #with codecs.open(inputFile,"r","utf-8") as csvfile:
    #    freader = csv.reader(csvfile)
    #    for row in freader:

    terms = findMatches(row[1])
    lsTerms.append(terms)
    # add the keyword to the beginning of the list
    #lsTerms.insert(0, row[0])
    # print values tab separated
    #print(*lt, sep='\t')
    
    return lsTerms

if __name__ == '__main__':
    '''
        @summary: main
    '''
    #inputFile = 'Searches_Automotive.csv'
    inputFile = 'Searches_Energy.csv'

    #inputFile = "Cornelsen-Thesaurus-1.0-nodes.csv"
    wikiDataURL = "https://query.wikidata.org/sparql?format=json&query="
    language = "de"

    # out file
    with codecs.open("WikiData-Synonyms.csv","w","utf-8") as o:
        with codecs.open(inputFile,"r","utf-8") as f:
        #.readline()
            freader = csv.reader(f)
            for row in freader:
                wordList = processRow(row)
                #wordList = set([line.split("\t")[0] for line in f.readlines() ])
                o.write(row[0])
                for word in wordList:
                    for w in word:
                        x = urlopen(wikiDataURL + quote_plus(synonyms(w,"de")))
                        raw_data = x.read()
                        encoding = x.info().get_content_charset('utf8')  # JSON default
                        data = json.loads(raw_data.decode(encoding))

                        noOfSynonyms = len(data['results']['bindings'])
                        
                        o.write('' + "\t" + w + "\t" + "\t".join([entry['name']['value'] for entry in data['results']['bindings']]) + "\n") 


    '''
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
    '''
