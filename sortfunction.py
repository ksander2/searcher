class Sorter:
     @staticmethod
     def sort(list_strs, sort_method, order):
        order_map = {'asc': False, 'desc': True, None: False }
        sorted_list = []
        if(sort_method == "abc"):
            return sorted(list_strs, reverse = order_map[order] )
        if(sort_method == "freq"):
           return sorted(list_strs, key=list_strs.count, reverse=order_map[order])
        return list_strs