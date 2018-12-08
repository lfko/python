'''
Created on Dec 3, 2018

@author: lfko
'''

from lfko.python.languaid.core.util.ruleLoader import RuleLoader


class Verb():

    def __init__(self):
        """ """
        self.rl = RuleLoader()
        # actual turkish vowels
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'ö', 'ü']

    def construct(self, word, args=[]):
        """ 
            @param **kwargs: key-value-params
        """

        # TODO check arguments

        #args = [('mode', 'negation'),
        #        ('tense', 'present'), ('person', 'type1', 5)]
        # at first, read the args dict and identify, which rules should be
        # loaded (e.g. for a specific tense)
        # the basic build rule: replace the suffix of the infinitive
        word_stem = word.replace('mak', '').replace('mek', '')

        buildRule = ''

        for arg in args:

            suffix = self.rl.find(arg)

            if len(buildRule) > 0:

                if buildRule[-2] == suffix[0]:
                    suffix = 'y' + suffix
                else:

                    if buildRule[-2] in self.vowels:
                        buildRule = buildRule.replace(
                            buildRule[-2], '')
                    #suffix = suffix.replace(suffix[len(suffix) - 1], '')
                    #suffix = reduce(lambda a, b: a.replace(b, ''), self.vowels, suffix)
                    # print(suffix)
            buildRule = buildRule + " + " + "'" + suffix + "'"

        # with eval, we are able to execute a string as actual python code
        evalBuild = eval("'" + word_stem + "'" + buildRule)

        return self.__harmonizeVowels__(evalBuild, word_stem)

    def deconstruct(self, args):
        """ """

    def __harmonizeVowels__(self, word, word_stem):
        """ """
        preceding_vow = [c for c in word_stem if c in self.vowels][-1]
        # create a copy of the word, reduced by the word stem
        # strings in python are immutables
        word = word.replace(word_stem, '')

        # get the dictionary of high vowels
        high_vow = self.rl.find(('vowel_harmony', 'high_vowels'))
        # get the dictionary of low vowels
        low_vow = self.rl.find(('vowel_harmony', 'low_vowels'))

        # since strings are immutable, we manage a list of replacements, which
        # will be applied afterwards to the word
        word_repl = {}
        for i, c in enumerate(word):

            print('current index {} and char {}'.format(i, c))
            if c in self.vowels or c in ['-', '_']:
                # char is a valid vowel
                if c != preceding_vow and word[(i - 1)] != '*':
                    if c == '_':
                        cNew = high_vow[preceding_vow]
                    elif c == '-':
                        cNew = low_vow[preceding_vow]
                    else:
                        cNew = high_vow[c]

                    word_repl[i] = cNew

                    preceding_vow = cNew
                else:
                    preceding_vow = c

                    print('setting new vowel')

        # get the word as a list, so we can replace characters (i.e. vowels)
        word_as_list = list(word)
        for key in word_repl.keys():
            word_as_list[key] = word_repl[key]

        # final word
        word = word_stem + ''.join(word_as_list)
        print(word_stem + ''.join(word_as_list))

        return word


#vb = Verb()
#vb.construct()
