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
            set_str = ProcessRegex.unique_matches(self.regex, list_str)
            if num_rows:
                set_str = set_str[:num_rows]      
            out_str = "\n".join(set_str)
            
        if self.method == MethodSearch.count:
            count = ProcessRegex.count_matches(self.regex, list_str)
            out_str = "Count matches: " + str(count)
            
        if self.method == MethodSearch.line:
            count = ProcessRegex.count_line_matches(self.regex, list_str)
            out_str = "Count line matches: " + str(count)
            
        if self.method == MethodSearch.all:
            set_str = ProcessRegex.all_matches(self.regex, list_str)
            if num_rows:
                set_str = set_str[:num_rows]  
            out_str = "\n".join(set_str)
            
        return out_str
    
    def printCollectionByCount(list_strs, count):
        if count:
            if count > len(list_strs):
                count = len(list_strs)
            for i in range(0, count):
                print(list_strs[i])
        else:
            for item in list_strs:
                print(item)
     