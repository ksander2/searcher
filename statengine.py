from enum import Enum
from regexfunction import ProcessRegex

class MethodStat(Enum):
    freq = 1
    count = 2
   
class StatEngine:
    def __init__(self, regex, method, sorter):
          self.regex = regex
          self.method = method
          self.sorter = sorter
          
    def begin(self, str_list, num_rows):
        str_list =  ProcessRegex.all_matches(self.regex, str_list)
        str_list = self.sorter.beginSorting(str_list)
        out_str = ""
        stat_list = []
        
        if self.method == MethodStat.count:
            for item in str_list:
                count_match = str_list.count(item)
                stat_str = '%-30s |   %d' % (item, count_match)
                self.__add_to_list_ifItemExist(stat_str, stat_list)
        
        if self.method == MethodStat.freq:
            size = len(str_list)
            for item in str_list:
                freq_match = str_list.count(item)/size
                stat_str = '%-30s |   %0.3f' % (item, freq_match)
                self.__add_to_list_ifItemExist(stat_str, stat_list)
        
        stat_list = self.__trimCollectionByCount(stat_list, num_rows)       
        out_str = "\n".join(stat_list)
        return out_str
    
    
    def __trimCollectionByCount(self, collection, count):
         return collection[:count]
    
    def __add_to_list_ifItemExist(self,item, collection):
        if collection.count(item) == 0:
            collection.append(item)
        
          