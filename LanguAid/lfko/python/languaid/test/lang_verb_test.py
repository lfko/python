'''
Created on Dec 27, 2018

    @author: fb
    @summary: unit tests for verb construction/deconstruction
'''
import unittest
from lfko.python.languaid.core.lang.verb import Verb


class LangCoreVerbTest(unittest.TestCase):
    
    def testVerbConstructPresent(self):
        """ 
        
        """
        vb = Verb()
        self.assertEqual(vb.construct('kullanmak', [[vb.Modes.negation.name], [vb.Tenses.present.name, 5]]), 'kullanmıyorlar')
        self.assertEqual(vb.construct('yürümek', [[vb.Modes.negation.name], [vb.Tenses.present.name, 2]]) , 'yürümüyor')
        self.assertEqual(vb.construct('okumak', [[vb.Modes.negation.name], [vb.Tenses.present.name, 3]]) , 'okumuyoruz')
        self.assertEqual(vb.construct('söylemek', [[vb.Tenses.present.name, 4]]) , 'söylüyorsunuz')
        self.assertEqual(vb.construct('aramak', [[vb.Tenses.present.name, 5]]), 'arıyorlar')
        self.assertEqual(vb.construct('yürümek', [[vb.Tenses.present.name, 3]]), 'yürüyoruz')

    def testVerbConstructPast(self):
        """
        
        """
        vb = Verb()
        self.assertEqual(vb.construct('kullanmak', [[vb.Tenses.past.name, 0]]), 'kullandım')
        self.assertEqual(vb.construct('aramak', [[vb.Modes.negation.name], [vb.Tenses.past.name, 4]]), 'aramadınız')
        self.assertEqual(vb.construct('dilmek', [[vb.Modes.negation.name], [vb.Tenses.past.name, 0]]), 'dilmedim')
        
    def testVerbConstructFutur(self):
        """
        
        """
        vb = Verb()
        self.assertEqual(vb.construct('uyukmak', [[vb.Tenses.futur.name, 3]]), 'uyukacağız')  
        self.assertEqual(vb.construct('yazmak', [[vb.Tenses.futur.name, 1]]), 'yazacağın')
        
    def testVerbConstructVoluntative(self):
        """ 
        
        """
        self.assertEqual(Verb().construct('yapmak', [[Verb().Imperative.voluntative.name, 0]]), 'yapayım')
        self.assertEqual(Verb().construct('yapmak', [[Verb().Imperative.voluntative.name, 1]]), 'yapalım')
        # self.assertEqual(Verb().construct('gitmek', [[Verb().Imperative.voluntative.name, 1]]), 'gidelim')      
    
    def testVerbDeconstruct(self):
        """ 
        
        """
        vb = Verb()
        print(vb.deconstruct('yiyeyim'))


if __name__ == "__main__": 
    unittest.main()
