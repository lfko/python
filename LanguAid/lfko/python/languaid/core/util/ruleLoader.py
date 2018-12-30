'''
    Created on Dec 6, 2018

    @author: lfko
    @summary: : grammatical rules should be loadable, so that the application has a more universal approach

'''

import json
from lfko.python.languaid.core.util.settings import Settings


class RuleLoader():

    def __init__(self):
        """ 
            @summary: default constructor
            @param category: name of the category, for which the rules should be loaded
            @return: dictionary containing the specific rules
        """
        
        self.appSet = Settings()

        with open(self.appSet.getValue('RULES', 'file')) as f:
            self.data = json.load(f)

    def findAllKeys(self, key_type):
        """ 
            @todo: not yet used
        """
        foodict = {k: v for k, v in self.data.items() if k.startswith(key_type)}
        
        print([v for k, v in foodict[type][0].items() if k.startswith('suffixes')])

    def find(self, argsTuple):
        """
            @summary: find the rule entries for a specific key 
            @param argsTuple: value for a specific item in a subcategory
            @return: list of rule elements or the element itself
        """
        rules = []
        # list of specific rules for a key of a category
        if len(argsTuple) == 2:
            # tuples allow for more complex rule queries
            rules = self.data[argsTuple[0]][0]['items'][argsTuple[1]]
        elif len(argsTuple) == 1:
            rules = self.data[argsTuple[0]][0]['items']

        return rules[0] if len(rules) == 1 else rules

    def getSuffixOrder(self, wordType):
        """ 
            @summary: 
            @param wordType:
            @return:  
        """
        suffixOrder = self.data[wordType][0]['order']

        return suffixOrder

