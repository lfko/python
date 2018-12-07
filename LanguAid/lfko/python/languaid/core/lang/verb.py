'''
Created on Dec 3, 2018

@author: lfko
'''

from lfko.python.languaid.core.util.ruleLoader import RuleLoader


class Verb():

    def __init__(self):
        """ """
        self.rl = RuleLoader()
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'ö', 'ü']

    def construct(self, word='altınlamak', args=[]):
        """ 
            @param **kwargs: key-value-params
        """
        args = [('mode', 'negation'),
                ('tense', 'present'), ('person', 'type1', 5)]
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

        evalBuild = eval("'" + word_stem + "'" + buildRule)
        print(evalBuild)

        self.__harmonizeVocals__(evalBuild, word_stem)

    def deconstruct(self, args):
        """ """

    def __harmonizeVocals__(self, word, word_stem):
        """ """
        preceding_vow = [c for c in word_stem if c in self.vowels][-1]
        print(preceding_vow)
        word2 = word.replace(word_stem, '')
        print(word2)

        high_vow = self.rl.find(('vowel_harmony', 'high_vowels'))
        print('high: ', high_vow)
        word = [c for c in word if c in high_vow]
        low_vow = self.rl.find(('vowel_harmony', 'low_vowels'))
        print('low: ', low_vow)
        word_repl = {}
        for i, c in enumerate(word2):

            print('current index {} and char {}'.format(i, c))
            if c in self.vowels or c == '_':
                # char is a valid vowel
                if c != preceding_vow and word2[(i - 1)] != '*':
                    if c == '_':
                        cNew = high_vow[preceding_vow]
                    else:
                        cNew = high_vow[c]

                    word_repl[i] = cNew

                    preceding_vow = cNew
                else:
                    preceding_vow = c

                    print('setting new vowel')

        print(word_repl)
        word_as_list = list(word2)
        for key in word_repl.keys():
            word_as_list[key] = word_repl[key]

        print(word_stem + ''.join(word_as_list))


vb = Verb()
vb.construct()
