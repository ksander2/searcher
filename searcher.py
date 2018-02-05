import argparse
import sys
from sortfunction import Sorter
from regexfunction import ProcessRegex

from searchengine import SearchEngine
from searchengine import MethodSearch





def create_stat_list(str_list, stat_metod):
    stat_list = []
    if stat_metod == "count":
        for item in str_list:
            count_match = str_list.count(item)
            stat_str = '%-30s |   %d' % (item, count_match)
            if stat_list.count(stat_str) == 0:
                stat_list.append(stat_str)
    if stat_metod == "freq":
        size = len(str_list)
        for item in str_list:
            freq_match = str_list.count(item)/size
            stat_str = '%-30s |   %0.3f' % (item, freq_match)
            if stat_list.count(stat_str) == 0:
                stat_list.append(stat_str)
    return stat_list


def printCollectionByCount(list_strs, count):
    if count:
        if count > len(list_strs):
            count = len(list_strs)
        for i in range(0, count):
            print(list_strs[i])
    else:
        for item in list_strs:
            print(item)

if __name__ == "__main__":
            
    #isReadyStdin = not sys.stdin.isatty()
    
    parser = argparse.ArgumentParser(description='search with regex')
    
    parser.add_argument("-u", 
                        dest='unique_mathces_arg', 
                        action="store_true", 
                        help="List unique matches only")
    
    parser.add_argument("-c", 
                        dest='count_mathces_arg', 
                        action="store_true", 
                        help="Get total count of found matches")
    
    parser.add_argument("-l", 
                        dest='count_line_mathces_arg', 
                        action="store_true", 
                        help="Get total count of lines, where at least one match was found")
    
    parser.add_argument("-s", 
                        dest='sort_method_arg', 
                        type=str, default=None, 
                        choices=["abc", "freq"], 
                        help="Sorting of found matches by alphabet and frequency")
    
    parser.add_argument("-o", 
                        dest='sort_order_arg', 
                        type=str, 
                        default=None, 
                        choices=["asc", "desc"], 
                        help="Sorting order")
    
    parser.add_argument("-n", 
                        dest='num_print_rows_arg', 
                        metavar='COUNT ROWS', 
                        type=int, 
                        default=None, 
                        help="List first N matches")
    
    parser.add_argument("--stat", 
                        dest='stat_arg', 
                        type=str, 
                        default=None,
                        choices=["count", "freq"], 
                        help="List unique matches with statistic")
    
    parser.add_argument('regex', 
                        metavar='PATTERN', 
                        type=str,  
                        help='Filter PATTERN')
    
    #if not isReadyStdin:
    parser.add_argument('file_name', 
                        metavar='FILENAME', 
                        default=None, 
                        type=str,  
                        help='file name')
        
    args = parser.parse_args()
    
    data_strings_temp = [] 
    
    #if not isReadyStdin:
    try:
        with open(args.file_name, "r") as data_file:
            data_strings_temp = data_file.readlines()
            
    except Exception as ex:
        print(ex)
        quit()
    #else:
    #    for line in sys.stdin:
    #        data_strings_temp.append(line)
    
    data_strings = [] 
    
    for item in data_strings_temp:
        data_strings.append(item.strip()) 
          
    regex = args.regex
    
    method_search_state = MethodSearch.all
    
    if args.count_mathces_arg and args.unique_mathces_arg:
        method_search_state = MethodSearch.unique_count
    else:
        if args.unique_mathces_arg:
            method_search_state = MethodSearch.unique   
        if args.count_mathces_arg:
            method_search_state = MethodSearch.count   
    if args.count_line_mathces_arg:
        method_search_state = MethodSearch.line

    s_e = SearchEngine(regex, method_search_state, None)
    
    print(s_e.begin(data_strings, args.num_print_rows_arg))
    
    
    