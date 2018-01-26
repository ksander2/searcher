import unittest
from regexfunction import ProcessRegex

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.list_tring = [
            "an_sobolev90@mail.ru",
            "an1_sobev90@mail.ru",
            "dfdfdfdfd",
            "an1_sobev90@gmail.ru   an1_aaassobev90@gmail.ru  dasdsad an1_aaccccssobev90@gmail.ru",
            "fn1_sobev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru",
            "gn1_sobev90@gmail.ru   an1_aac1ssobev90@gmail.ru",
            "hn1_sobev90@gmail.ru",
            "an1_sobev90@gmai1l.ru",
            "dddfff",
            "an1_so11111bev90@gmai1l.ru",
            "an1_sobev90@gmai1l.ru",
            "an1_sobev90@gmai1l.ru",
            "bn.obev90@gmail.ru",
            "bn.obev90@gmail.ru"
            ]
        
        self.regex1 = "\w+@[\w.-_]+"
        self.regex2 = "\w+@([\w.-_]+)"

    def test_CountMatches(self):
        count = ProcessRegex.count_matches(self.regex1, self.list_tring)
        self.assertEqual(count, 23)
        
    def test_UniqueCountMatches(self):
        count = ProcessRegex.count_unique_matches(self.regex1, self.list_tring)
        self.assertEqual(count, 12)
        
    def test_Unique(self):
        all_m = ProcessRegex.unique_matches(self.regex1, self.list_tring)
        num = len(all_m)
        self.assertEqual(num, 12)
        
    def test_allMathces(self):
        all_m = ProcessRegex.all_matches(self.regex1, self.list_tring)
        self.assertEqual(all_m[16], "hn1_sobev90@gmail.ru")  
          
    def test_count_line_Mathces(self):
        count = ProcessRegex.count_line_matches(self.regex1, self.list_tring)
        self.assertEqual(count, 10)
        
    #def test_sort(self):
       # all_m = ProcessRegex.all_matches(self.regex1, self.list_tring)
       # list_s = searcher.sort(all_m, "abc", "desc")
       # self.assertEqual(list_s[4], "an1_so11111bev90@gmai1l.ru")
       # self.assertEqual(list_s[14], "obev90@gmail.ru")    
    

if __name__ == '__main__':
    unittest.main()