from enum import Enum


class SortOrder(Enum):
    asc = 1
    desc = 2

class SortMethod(Enum):
    freq = 1
    abc = 2
    

class Sorter:
    def __init__(self, method, order):
        self.method = method
        self.order = order
        self.order_dict ={SortOrder.asc: False, SortOrder.desc: True} 
        
    def beginSorting(self, list_strs):
        if self.method == SortMethod.abc:
            return sorted(list_strs, reverse = self.order_dict[self.order] )
        if self.method == SortMethod.freq:
            return sorted(list_strs, key=list_strs.count, reverse = not self.order_dict[self.order])
