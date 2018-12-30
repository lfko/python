'''
    Created on Dec 3, 2018

    @author: fb
    @summary: 
'''

from lfko.python.languaid.core.util.ruleLoader import RuleLoader
from lfko.python.languaid.core.lang.vowel import VowelHarmonizer

from enum import Enum


class Verb():
    
    # enums representing the currently available verb modifications
    Tenses = Enum('Tenses', 'past present futur')
    Modes = Enum('Modes', 'negation reciprocal passive')
    Imperative = Enum('Imperative', 'voluntative imperative')  

    def __init__(self):
        """ 
            @summary: default constructor
        """
        self.vh = VowelHarmonizer()
        self.rl = RuleLoader()
        self.vowels = self.rl.find(['vowels'])

    def construct(self, word, args=[]):
        """ 
            @summary: construct a verb with the requested suffixes
            @param word: the verb to decline (in its infinitive form)
            @param args: list of parameters
            @return: a conjugated verb
        """
        if word == '' or word == None:
            raise TypeError('empty word supplied')
        if len(args) == 0 or args == None:
            raise TypeError('empty argument lists supplied')

        # the basic build rule: replace the suffix of the infinitive
        word_stem = word.replace('mak', '').replace('mek', '')

        buildRule = "'" + word_stem + "'"

        for arg in args:

            suffix = self.rl.find(arg)

            if len(buildRule) > 0:

                if buildRule[-2] == '-' and suffix[0] == '%':
                    suffix = suffix.replace('%', 'y')  # to separate sequent vowels we include an 'y'
                elif buildRule[-2] in self.vowels:
                    if (suffix[0] in self.vowels) or (suffix[0] in ['_', '-']):
                        buildRule = buildRule[:-2] + "'"
                        word_stem = word_stem[:-1]

            buildRule = buildRule + " + " + "'" + suffix + "'"

        # with eval, we are able to execute a string as actual python code
        evalBuild = eval(buildRule)
        
        return self.vh.harmonize(word_stem, evalBuild)

    def deconstruct(self, word):
        """ 
            @summary: deconstruct an already valid verb to its separate suffixes 
            @param word: the verb to analyse
            @return: a dict containing the found suffixes
        """
        import re
        
        found_suffixes = {}
        
        suffix_order = self.rl.getSuffixOrder('verb')  # load the building rules for verbs
        suffix_order.reverse()  # and reverse them
        
        # iterate the order and load the corresponding rule
        for order in suffix_order:

            suffixes = self.rl.find([order])
            
            for s in suffixes:
                # replace the vowel wildcard characters with a '.' so we can use regex
                s_tmp = s.replace('-', '.').replace('_', '.')

                # look for a match at the end of the word string
                if re.search(r"(" + s_tmp + ")$", word):
                    found_suffixes[order] = s  # adds the found suffix to the dict of suffixes
                    word = word[:-len(s)]  # removes the ending from the noun
        
        return found_suffixes

