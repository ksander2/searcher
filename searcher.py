import argparse
from regexfunction import ProcessRegex

def sort(list_strs, sort_method, order):
    order_map = {'asc': False, 'desc': True, None: False }
    if(sort_method == "abc"):
        return sorted(list_strs, reverse = order_map[order] )
    if(sort_method == "freq"):
       return sorted(list_strs, key=list_strs.count, reverse = order_map[order] )
   
    return list_strs

def create_stat_set(str_list, stat_metod):
    stat_set = set()
    if stat_metod == "count":
        for item in str_list:
            count_match = str_list.count(item)
            str_count_match = str(count_match)
            stat_set.add(item + " | " + str_count_match)
    if stat_metod == "freq":
        size = len(str_list)
        for item in str_list:
            count_match = round(str_list.count(item)/size, 3)
            str_count_match = str(count_match)
            stat_set.add(item + " | " + str_count_match)
    return stat_set
    

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("-u", dest='unique_mathces_arg', action="store_true", help="Количество дней, прошедших с даты в названии папки(для удаления)")
parser.add_argument("-c", dest='count_mathces_arg', action="store_true", help="Количество дней, прошедших с даты в названии папки(для удаления)")
parser.add_argument("-l", dest='count_line_mathces_arg', action ="store_true", help="Количество дней, прошедших с даты в названии папки(для удаления)")
parser.add_argument("-s", dest='sort_method_arg', type=str, default=None, choices=["abc", "freq"], help="Количество дней, прошедших с даты в названии папки(для удаления)")
parser.add_argument("-o", dest='sort_order_arg', type=str, default=None, choices=["asc", "desc"], help="Количество дней, прошедших с даты в названии папки(для удаления)")
parser.add_argument("-n", dest='num_print_rows_arg', type=int, default=None, help="Количество дней, прошедших с даты в названии папки(для удаления)")
parser.add_argument("--stat", dest='stat_arg', type=str, default=None,choices=["count", "freq"], help="Количество дней, прошедших с даты в названии папки(для удаления)")
parser.add_argument('regex', metavar='PATTERN', type=str,  help='an integer for the accumulator')
parser.add_argument('file_name', metavar='FILENAME', type=str,  help='an integer for the accumulator')

args = parser.parse_args()

data_strings_temp = []

try:
    with open(args.file_name, "r") as data_file:
        data_strings_temp = data_file.readlines()
        
except Exception as ex:
    print(ex)
    quit()


data_strings = [] 

#delete backspace in rows
for item in data_strings_temp:
    data_strings.append(item.strip()) 
    
#strip regex string    
regex = args.regex[1:-1]

if args.count_mathces_arg and args.unique_mathces_arg:
    count = ProcessRegex.count_unique_matches(regex, data_strings)
    print("Count unique matches:", count)
else:
    if args.unique_mathces_arg:
        set_str = ProcessRegex.unique_matches(regex, data_strings)
        for item in set_str:
            print(item)
    
    if args.count_mathces_arg:
        count = ProcessRegex.count_matches(regex, data_strings)
        print("Count matches:", count)

if args.count_line_mathces_arg:
    count = ProcessRegex.count_line_matches(regex, data_strings)
    print("Count line matches:", count)

if not args.count_mathces_arg and not args.unique_mathces_arg and not args.count_line_mathces_arg:
    all_matches = ProcessRegex.all_matches(regex, data_strings)
    all_matches = sort(all_matches, args.sort_method_arg, args.sort_order_arg)
    if args.stat_arg:
        all_matches= create_stat_set(all_matches, args.stat_arg)      
    for item in all_matches:
        print(item)
        
ggg = "%-10d".format(25)
sd = '%-12d sdsdsds' % 2770
a = 0
        