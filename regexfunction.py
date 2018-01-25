import re
class ProcessRegex:
    
    @staticmethod
    def unique_matches(regex_str, list_str):
        set_str = set()
        for item in list_str:
            s_list = re.findall(regex_str, item, 0)
            for match in s_list:
                set_str.add(match)
        return set_str
    
    @staticmethod
    def count_matches(regex_str, list_str):
        all_matches = []
        for item in list_str:
            s_list = re.findall(regex_str, item, 0)
            all_matches.extend(s_list)
        return len(all_matches)
    
    @staticmethod
    def count_unique_matches(regex_str, list_str):
        set_str = set()
        for item in list_str:
            s_list = re.findall(regex_str, item, 0)
            for match in s_list:
                set_str.add(match)
        return len(set_str)
        
    @staticmethod
    def count_line_matches(regex_str, list_str):
        count = 0
        for item in list_str:
            if re.match(regex_str, item,0):
                count += 1
        return count
    
    @staticmethod
    def all_matches(regex_str, list_str):
        all_matches = []
        for item in list_str:
            s_list = re.findall(regex_str, item, 0)
            all_matches.extend(s_list)
        return all_matches     