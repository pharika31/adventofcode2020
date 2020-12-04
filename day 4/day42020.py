import re
def check_passport_data_validity(filename):
    with open(filename) as f:
        input_array = f.read().split('\n\n')
    cleaned_input_array_without_new_lines = []
    for line in input_array:
       modified_input_line = line.replace("\n", " ")
       cleaned_input_array_without_new_lines.append(modified_input_line)
    test_input_final = []
    for line in cleaned_input_array_without_new_lines:
        line_converted_to_dict = dict((k.strip(), v.strip()) for k,v in
              (item.split(':') for item in line.split(' ')))
        test_input_final.append(line_converted_to_dict)
    count_of_valid_passports = 0
    for item in test_input_final:
        if ('byr' in item and
            'eyr'in item and
            'hgt' in item and
            'pid' in item and
            'hcl'in item and
            'iyr'in item and
            'ecl'in item and
            'cid' in item ):
            count_of_valid_passports += 1
        elif('byr' in item and
            'eyr'in item and
            'hgt' in item and
            'pid' in item and
            'hcl'in item and
            'iyr'in item and
            'ecl'in item):
            count_of_valid_passports +=1
    print (count_of_valid_passports)

def check_passport_data_validity_values(filename):
    with open(filename) as f:
        input_array = f.read().split('\n\n')
    cleaned_input_array_without_new_lines = []
    for line in input_array:
       modified_input_line = line.replace("\n", " ")
       cleaned_input_array_without_new_lines.append(modified_input_line)
    test_input_final = []
    for line in cleaned_input_array_without_new_lines:
        line_converted_to_dict = dict((k.strip(), v.strip()) for k,v in
              (item.split(':') for item in line.split(' ')))
        test_input_final.append(line_converted_to_dict)
    count_of_valid_passports = 0
    pattern = re.compile('^(([1][5][0-9]|[1][6-8][0-9]|[1][9][0-3])cm)$|([5][9]|[6-7][0-6]in)$')
    hcl_pattern = re.compile('^#([0-9a-f]){6}$')
    for item in test_input_final:
        if ('byr' in item and
            'eyr'in item and
            'hgt' in item and
            'pid' in item and
            'hcl'in item and
            'iyr'in item and
            'ecl'in item and
                ('cid' in item or 'cid' not in item) ):
            #regex for each condition
            try:
                byr =int(item['byr'])
            except:
                continue
            try:
                iyr = int(item['iyr'])
            except:
                continue
            try:
                eyr = int(item['eyr'])
            except:
                continue
            try:
                pid = int(item['pid'])
            except:
                continue
            pattern_match = pattern.match(item['hgt'])
            pattern_match_hcl = hcl_pattern.match(item['hcl'])
            if(byr in range(1920,2003) and
                iyr in range(2010,2021) and
                eyr in range(2020,2031) and
                pattern_match is not None and
                pattern_match_hcl is not None and
                item['ecl'] in({'amb','blu','brn','gry','grn','hzl','oth'}) and
                pid in range (000000000, 1000000000)):
                count_of_valid_passports += 1
    print (count_of_valid_passports)





def main():
    check_passport_data_validity('C:/Users/harik/Documents/Python Scripts/advent_of_code/day 4/input.txt')
    check_passport_data_validity_values('C:/Users/harik/Documents/Python Scripts/advent_of_code/day 4/input.txt')


if __name__ == "__main__":
    main()
