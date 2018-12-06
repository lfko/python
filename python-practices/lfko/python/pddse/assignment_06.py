'''
Created on Dec 5, 2018

@author: fb (s76343)

'''

import requests


def assignment_06_01():
    """ reads random files from csv files, sums them up and returns the result 
    @return: list of summed up values
    """

    import glob  # for matching certain patterns
    import os
    import fileinput  # reads input of multiple files at once

    csv_files = glob.glob(os.path.join('data/', 'random_numbers', '*.csv'))

    # sum_of_values = 0
    # for line in fileinput.input(csv_files):
    #    sum_of_values = sum_of_values + int(line)

    return sum(map(lambda line: int(line), fileinput.input(csv_files)))


def assignment_06_02(url):
    """ reads a wikipedia page and extracts the infobox and returns the information as key value dict 
    @param url: URL to a wikipedia page
    @return: dictionary of all infobox entries
    """
    from bs4 import BeautifulSoup

    if(url == '' or url == None):
        raise ValueError('no @param url supplied')

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # infobox table
    table = soup.find("table", {"id": "Vorlage_Infobox_Hochschule"})

    # get all elements with tag <tr> from the table
    infobox_trs = table.findAll('tr')

    # creates a nested list of lists, which contain the infobox entries
    box_items = list(
        map(lambda item: item.getText().strip().split('\n\n'), infobox_trs))

    # create the dictionary by reading out the key value pairs from the nested
    # list
    result = {}
    for entries in box_items:
        for entry in entries[1:]:
            result[entries[0]] = entry

    return result


def assignment_06_03():
    """ reads a JSON containing all of Berlin's christmas markets 
    @return: name district with the most christmas markets
    """

    import json
    from collections import Counter

    christmas_market_url = 'https://www.berlin.de/sen/web/service/maerkte-feste/weihnachtsmaerkte/index.php/index/all.json?q='
    data = json.loads(requests.get(christmas_market_url).content)
    # count all occurences of unique 'Bezirk' in the json dict
    borough_counter = Counter(borough['bezirk'] for borough in data['index'])

    # return the district which value (sum of christmas markets) is the
    # hightest
    return max(dict(borough_counter), key=dict(borough_counter).get)


""" """
if __name__ == '__main__':
    beuth_url = "https://de.wikipedia.org/wiki/Beuth_Hochschule_f%C3%BCr_Technik_Berlin"
    assignment_06_01()
    assignment_06_02(beuth_url)
    assignment_06_03()
