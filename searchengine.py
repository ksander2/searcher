from regexfunction import ProcessRegex
from enum import Enum


class MethodSearch(Enum):
    all = 1
    unique = 2
    count = 3
    unique_count = 4
    line = 5
    
class SearchEngine:
    def __init__(self, regex, method, sorter):
          self.regex = regex
          self.method = method
          self.sorter = sorter
 
    def begin(self, list_str, num_rows ):
        out_str = ""
 
        if self.method == MethodSearch.unique_count:
            count = ProcessRegex.count_unique_matches(self.regex, list_str)
            out_str = "Count unique matches: " + str(count)
            
        if self.method == MethodSearch.unique:
            list_str = ProcessRegex.unique_matches(self.regex, list_str)
            if num_rows:
                list_str = self.__trimCollectionByCount(list_str, num_rows)   
            list_str = self.sorter.beginSorting(list_str)      
            out_str = "\n".join(list_str)
            
        if self.method == MethodSearch.count:
            count = ProcessRegex.count_matches(self.regex, list_str)
            out_str = "Count matches: " + str(count)
            
        if self.method == MethodSearch.line:
            count = ProcessRegex.count_line_matches(self.regex, list_str)
            out_str = "Count line matches: " + str(count)
            
        if self.method == MethodSearch.all:
            list_str = ProcessRegex.all_matches(self.regex, list_str)
            if num_rows:
                list_str = self.__trimCollectionByCount(list_str, num_rows)  
            list_str = self.sorter.beginSorting(list_str)
            out_str = "\n".join(list_str)
            
        return out_str
    
    def __trimCollectionByCount(self, collection, count):
         return collection[:count]