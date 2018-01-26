import argparse
import sys
import select
from sortfunction import Sorter

from regexfunction import ProcessRegex
from re import search

def create_stat_list(str_list, stat_metod):
    stat_set = set()
    if stat_metod == "count":
        for item in str_list:
            count_match = str_list.count(item)
            stat_str = '%-30s |   %d' % (item, count_match)
            stat_set.add(stat_str)
    if stat_metod == "freq":
        size = len(str_list)
        for item in str_list:
            freq_match = str_list.count(item)/size
            stat_str = '%-30s |   %0.3f' % (item, freq_match)
            stat_set.add(stat_str)
    return list(stat_set)

def printCollectionByCount(list_strs, count):
    if count:
        if count > len(list_strs):
            count = len(list_strs)
        for i in range(0, count):
            print(list_strs[i])
    else:
        for item in list_strs:
            print(item)
        


isReadyStdin = not sys.stdin.isatty()
#isReadyStdin = sys.stdin.isatty()

parser = argparse.ArgumentParser(description='search with regex')

parser.add_argument("-u", dest='unique_mathces_arg', action="store_true", help="List unique matches only")
parser.add_argument("-c", dest='count_mathces_arg', action="store_true", help="Get total count of found matches")
parser.add_argument("-l", dest='count_line_mathces_arg', action ="store_true", help="Get total count of lines, where at least one match was found")
parser.add_argument("-s", dest='sort_method_arg', type=str, default=None, choices=["abc", "freq"], help="Sorting of found matches by alphabet and frequency")
parser.add_argument("-o", dest='sort_order_arg', type=str, default=None, choices=["asc", "desc"], help="Sorting order")
parser.add_argument("-n", dest='num_print_rows_arg', metavar='COUNT ROWS', type=int, default=None, help="List first N matches")
parser.add_argument("--stat", dest='stat_arg', type=str, default=None,choices=["count", "freq"], help="List unique matches with statistic")
parser.add_argument('regex', metavar='PATTERN', type=str,  help='Filter PATTERN')

if isReadyStdin == False:
    parser.add_argument('file_name', metavar='FILENAME', default=None, type=str,  help='file name')
    
args = parser.parse_args()

data_strings_temp = [] 

if isReadyStdin == False:
    try:
        with open(args.file_name, "r") as data_file:
            data_strings_temp = data_file.readlines()
            
    except Exception as ex:
        print(ex)
        quit()
else:
    for line in sys.stdin:
        data_strings_temp.append(line)

data_strings = [] 

#delete backspace in rows
for item in data_strings_temp:
    data_strings.append(item.strip()) 
    
#strip regex string    
regex = args.regex

if args.count_mathces_arg and args.unique_mathces_arg:
    count = ProcessRegex.count_unique_matches(regex, data_strings)
    print("Count unique matches:", count)
else:
    if args.unique_mathces_arg:
        set_str = ProcessRegex.unique_matches(regex, data_strings)
        set_str = Sorter.sort(set_str, args.sort_method_arg, args.sort_order_arg)
        printCollectionByCount(set_str, args.num_print_rows_arg)
    
    if args.count_mathces_arg:
        count = ProcessRegex.count_matches(regex, data_strings)
        print("Count matches:", count)

if args.count_line_mathces_arg:
    count = ProcessRegex.count_line_matches(regex, data_strings)
    print("Count line matches:", count)

if not args.count_mathces_arg and not args.unique_mathces_arg and not args.count_line_mathces_arg:
    all_matches = ProcessRegex.all_matches(regex, data_strings)
    all_matches = Sorter.sort(all_matches, args.sort_method_arg, args.sort_order_arg)
    if args.stat_arg:
        all_matches= create_stat_list(all_matches, args.stat_arg)      
        all_matches = Sorter.sort(all_matches, args.sort_method_arg, args.sort_order_arg)
        
    printCollectionByCount(all_matches, args.num_print_rows_arg)
