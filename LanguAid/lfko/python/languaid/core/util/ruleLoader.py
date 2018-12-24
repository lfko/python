'''
Created on Dec 6, 2018

@author: lfko

    Intention: grammatical rules should be loadable, so that the application has a more universal approach

'''

import configparser
import json
import pathlib
from pprint import pprint


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
            
        print('loaded', rules)

        return [rules] if type(rules) != list else rules

