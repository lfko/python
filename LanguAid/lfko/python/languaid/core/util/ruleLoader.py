'''
Created on Dec 6, 2018

@author: lfko

    Intention: grammatical rules should be loadable, so that the application has a more universal approach

'''

import configparser
import json
import pathlib


class RuleLoader():
    """
    """

    def __init__(self):
        """ 
            @param category: name of the category, for which the rules should be loaded
            @return: dictionary containing the specific rules
        """
        # TODO be aware, that directories can change
        ini_dir = pathlib.Path('../../../../../')
        for file in ini_dir.iterdir():
            if str(file).find('settings.ini') > 0:
                ini_file = file
        
        config = configparser.ConfigParser()
        config.read(ini_file)
        # print(config.sections())
        # print(config['RULES']['file'])

        with open(config['RULES']['file']) as f:
            self.data = json.load(f)

        # self.data = json.dumps(self.data)
        # print(self.data)
        # pprint(self.data)

    def findAllKeys(self, type='person'):
        """ """
        foodict = {k: v for k, v in self.data.items() if k.startswith(type)}
        # print(foodict)
        print([v for k, v in foodict[type][0].items() if k.startswith('suffixes')])
        # print(foodict.keys())
        # print(foodict.items())
        # print(foodict.values())
        # bardict = {k: v for k, v in foodict.keys().items() if k.startswith('category')}
        # print(bardict)
        # [v for k in self.data.keys() if k == type]
    
    def find(self, argsTuple):
        """
        find the rule entries for a specific key 
        @param category:
        @param key: key to a subcategory
        @param value: value for a specific item in a subcategory
        @return: list of rule elements  

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
        
        """
        suffixOrder = self.data[wordType][0]['order']
        
        return suffixOrder


rl = RuleLoader()
rl.findAllKeys()
