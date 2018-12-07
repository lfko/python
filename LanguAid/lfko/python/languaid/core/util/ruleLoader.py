'''
Created on Dec 6, 2018

@author: lfko

    Intention: grammatical rules should be loadable, so that the application has a more universal approach

'''

import json
from pprint import pprint


class RuleLoader():
    """
    """

    def __init__(self):
        """ 
            @param category: name of the category, for which the rules should be loaded
            @return: dictionary containing the specific rules
        """

        with open('/home/lfko/git/python/LanguAid/lfko/rules.json') as f:
            self.data = json.load(f)

        # pprint(self.data)

    def find(self, argsTuple):
        """
        find the rule entries for a specific key 
        @param category:
        @param key: key to a subcategory
        @param value: value for a specific item in a subcategory
        @return: list of rule elements  

        """
        # list of specific rules for a key of a category
        if len(argsTuple) == 3:
            # tuples allow for more complex rule queries
            rules = self.data[argsTuple[0]][0][argsTuple[1]][argsTuple[2]]
        else:
            rules = self.data[argsTuple[0]][0][argsTuple[1]]

        if type(rules) == list:
            return rules[0]
        else:
            return rules
