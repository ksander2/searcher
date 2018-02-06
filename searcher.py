import argparse
from sys import stdin

from regexfunction import ProcessRegex

from searchengine import SearchEngine
from searchengine import MethodSearch

from statengine import StatEngine
from statengine import MethodStat

from sorter import Sorter
from sorter import SortOrder
from sorter import SortMethod

sort_method_map = {}
sort_method_map['abc'] = SortMethod.abc
sort_method_map['freq'] = SortMethod.freq

sort_order_map = {}
sort_order_map['asc'] = SortOrder.asc
sort_order_map['desc'] = SortOrder.desc

stat_method_map = {}
stat_method_map['count'] = MethodStat.count
stat_method_map['freq'] = MethodStat.freq

if __name__ == "__main__":
            
    isReadyStdin = not stdin.isatty()
    
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
    
    if not isReadyStdin:
        parser.add_argument('file_name', 
                            metavar='FILENAME', 
                            default=None, 
                            type=str,  
                            help='file name')
        
    args = parser.parse_args()
    
    data_strings_temp = [] 
    
    if not isReadyStdin:
        try:
            with open(args.file_name, "r") as data_file:
                for line in data_file:
                    data_strings_temp.append(line)
               
        except Exception as ex:
            print(ex)
            quit()
    else:
        for line in stdin:
            data_strings_temp.append(line)
    
    data_strings = [] 
    
    for item in data_strings_temp:
        data_strings.append(item.strip()) 
          
    regex = args.regex
    method_search_state = MethodSearch.all
    method_sorting = SortMethod.abc
    sortOrder = SortOrder.asc
    stat_method_state = MethodStat.count
    
    if args.count_mathces_arg and args.unique_mathces_arg:
        method_search_state = MethodSearch.unique_count
    else:
        if args.unique_mathces_arg:
            method_search_state = MethodSearch.unique   
        if args.count_mathces_arg:
            method_search_state = MethodSearch.count   
    if args.count_line_mathces_arg:
        method_search_state = MethodSearch.line

    if args.sort_method_arg:
        method_sorting = sort_method_map[args.sort_method_arg]
    
    if args.sort_order_arg:
        sortOrder = sort_order_map[args.sort_order_arg]

    sorter = Sorter(method_sorting,sortOrder)
    
    if args.stat_arg:
        stat_engine = StatEngine(regex, stat_method_map[args.stat_arg], sorter)
        print(stat_engine.begin(data_strings, args.num_print_rows_arg))
    else:
        search_engine = SearchEngine(regex, method_search_state, sorter)
        print(search_engine.begin(data_strings, args.num_print_rows_arg))
