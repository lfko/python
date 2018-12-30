'''
    Created on Dec 6, 2018

    @author: fb
    @summary: 
'''
import re

from lfko.python.languaid.core.util.ruleLoader import RuleLoader
from lfko.python.languaid.core.lang.vowel import VowelHarmonizer
from enum import Enum


class Noun(object):
    
    # enums representing the currently available noun modifications
    Number = Enum('Number', 'singular plural')
    Modes = Enum('Modes', 'possession')

    def __init__(self):
        '''
            @summary: default constructor
        '''
        self.vh = VowelHarmonizer()
        self.rl = RuleLoader()
        self.vowels = self.rl.find(['vowels'])
    
    def construct(self, noun, args=[]):
        """ 
            @summary: construct a valid noun; there are some restrictions, which should be applied 
            @param noun: the basic noun
            @param args[]: contains the suffixes we'd like to apply/attach to the basic noun, e.g. 'plural' or 'possession'
            @return: a declined noun
        """
        if noun == '' or noun == None:
            raise TypeError('empty noun supplied')
        if len(args) == 0 or args == None:
            raise TypeError('empty argument lists supplied')

        buildRule = "'" + noun + "'"

        for arg in args:

            suffix = self.rl.find(arg)  # find the suffix to attach
            if buildRule[-2] in self.vowels and suffix[0] == '_': 
                # if the word ends with a vowel we don't need to replace the '_' of the suffix with a vowel
                buildRule = buildRule + " + " + "'" + suffix.replace('_', '') + "'"
            elif buildRule[-2] in self.vowels and suffix[0] == '%':
                suffix = suffix.replace('%', 's')  # specific rule to separate sequent vowels
                buildRule = buildRule + " + " + "'" + suffix + "'"
            else:
                buildRule = buildRule + " + " + "'" + suffix + "'"

        # with eval, we are able to execute a string as actual python code
        evalBuild = eval(buildRule)
        
        return self.vh.harmonize(noun, evalBuild)
    
    def deconstruct(self, noun):
        """ 
            @summary: deconstruct an already valid noun to its separate suffixes 
            @param noun: the valid noun we'd like to deconstruct
            @return: dictionary of found suffixes
        """
        found_endings = {}
        
        suffix_order = self.rl.getSuffixOrder('noun')
        suffix_order.reverse()

        for order in suffix_order:

            suffixes = self.rl.find([order])
            
            for s in suffixes:
            
                s_tmp = s.replace('-', '.').replace('_', '.')
                
                if re.search(r"(" + s_tmp + ")$", noun):
                    found_endings[order] = s  # adds the found suffix to the dict of suffixes
                    noun = noun[:-len(s)]  # removes the ending from the noun
            
        return found_endings
