'''
Created on Dec 6, 2018

@author: fb
'''
import re

from lfko.python.languaid.core.util.ruleLoader import RuleLoader


class Noun(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
            default constructor
        '''
        self.rl = RuleLoader()
        self.vowels = self.rl.find(['vowels'])
    
    def constructNoun(self, noun, args=[]):
        """ construct a valid noun; there are some restrictions, which should be applied 
        
        
        @param noun: the basic noun
        @param **kwargs: contains the suffixes we'd like to apply/attach to the basic noun, e.g. 'plural' or 'possession' (dictionary!)
        
        
        """
        buildRule = "'" + noun + "'" 

        for arg in args:

            suffix = self.rl.find(arg) # find the suffix to attach
            if buildRule[-1] in self.vowels and suffix[0] == '_': 
                # if the word ends with a vowel we don't need to replace the '_' of the suffix with a vowel
                buildRule = buildRule + " + " + "'" + suffix.replace('_', '') + "'"
            else:
                buildRule = buildRule + " + " + "'" + suffix + "'"

        # with eval, we are able to execute a string as actual python code
        evalBuild = eval(buildRule)
        print(evalBuild)
        
        # for key, value in kwargs.items():
        # completeNoun = map(lambda value: noun.join(value) , **kwargs.values())
        
        # return evalBuild
        return self.__harmonizeVowels__(noun, evalBuild)
    
    def __harmonizeVowels__(self, word_stem, built_word):
        """ 
            
        """
        preceding_vow = [c for c in word_stem if c in self.vowels][-1]
        
        # get the dictionary of high vowels - this is the only one needed for nouns
        # high_vow = self.rl.find(('vowel_harmony', 'high_vowels'))
        # low_vow = self.rl.find(('vowel_harmony', 'low_vowels'))
        high_vow = self.rl.find(['high_vowels'])
        low_vow = self.rl.find(['low_vowels'])

        if built_word.find('_') > 0:
            built_word = built_word.replace('_', high_vow[preceding_vow])
        if built_word.find('-') > 0:
            built_word = built_word.replace('-', low_vow[preceding_vow])

        return built_word
    
    def deconstructNoun(self, noun='cantalarim'):
        """ deconstruct an already valid noun to its separate suffixes 
        
        @param noun: the valid noun we'd like to deconstruct
        @return: dictionary of found suffixes
        """
        found_endings = {}
        
        # suffix_order = self.rl.find(('noun', 'order'))
        suffix_order = self.rl.getSuffixOrder('noun')
        suffix_order.reverse()

        for order in suffix_order:
            print(order)
            suffixes = self.rl.find([order])
            
            for s in suffixes:
            
                s_tmp = s.replace('-', '.').replace('_', '.')
                
                if re.search(r"(" + s_tmp + ")$", noun):
                    found_endings[order] = s # adds the found suffix to the dict of suffixes
                    noun = noun[:-len(s)] # removes the ending from the noun
            
        return found_endings


n = Noun()
endings = n.deconstructNoun()
print(endings)
naun = n.constructNoun(noun='canta', args=[['plural'], ['possession', 0]])
print(naun)
