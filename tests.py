import unittest
from regexfunction import ProcessRegex
from sorter import Sorter
from sorter import SortOrder
from sorter import SortMethod

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.list_tring = [
            "an_sobolev90@mail.ru",
            "an1_sobev90@mail.ru",
            "dfdfdfdfd",
            "an1_sobev90@gmail.ru   an1_aaassobev90@gmail.ru  dasdsad an1_aaccccssobev90@gmail.ru",
            "fn1_sobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru",
            "gn1_sobev90@gmail.ru   an1_aac1ssobev90@gmail.ru",
            "hn1_sobev90@gmail.ru",
            "an1_sobev90@gmai1l.ru",
            "dddfff",
            "an1_so11111bev90@gmai1l.ru",
            "an1_sobev90@gmai1l.ru",
            "an1_sobev90@gmai1l.ru",
            "bnobev90@gmail.ru",
            "bnobev90@gmail.ru"
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
        self.assertEqual(count, 20)
        
    def test_sort(self):
        all_m = ProcessRegex.all_matches(self.regex1, self.list_tring)
        sorter = Sorter(SortMethod.abc, SortOrder.asc)
        list_s = sorter.beginSorting(all_m)
        self.assertEqual(list_s[3], "an1_so11111bev90@gmai1l.ru")
        self.assertEqual(list_s[14], "bnobev90@gmail.ru")
        
        sorter = Sorter(SortMethod.abc, SortOrder.desc)
        list_s = sorter.beginSorting(all_m)
        self.assertEqual(list_s[0], "hn1_sobev90@gmail.ru")
        
        sorter = Sorter(SortMethod.freq, SortOrder.asc)
        list_s = sorter.beginSorting(all_m)
        self.assertEqual(list_s[0], "bnobev90@gmail.ru")    
    
if __name__ == '__main__':
    unittest.main()