import re
def check_count_of_chars():
    input_array = []
    test_input = []
    with open("C:/Users/sh.punyamurthula/Desktop/input.txt") as input_file:
        input_array = input_file.read().split('\n')
    for line in input_array:
        test_input_parts = re.split(' |: |-',line)
        test_input.append(test_input_parts)
    coun_of_trues = 0
    for list in test_input:
        low = int(list[0])
        high = int(list[1])+1
        char_to_search = list[2]
        test_string = list[3]
        count_of_char = 0
        for char in test_string:
            if(char==char_to_search):
                count_of_char += 1
        if count_of_char in range (low,high):
            coun_of_trues += 1
    return coun_of_trues

def check_position_of_chars():
    input_array = []
    test_input = []
    with open("C:/Users/sh.punyamurthula/Desktop/input.txt") as input_file:
        input_array = input_file.read().split('\n')
    for line in input_array:
        test_input_parts = re.split(' |: |-',line)
        test_input.append(test_input_parts)
    count_of_trues = 0
    for list in test_input:
        pos1 = int(list[0])-1
        pos2 = int(list[1])-1
        char_to_search = list[2]
        test_string = list[3]
        count_to_be_1 =0
        if(pos1<len(test_string) and pos2<len(test_string)):
            if (list[3][pos1]==char_to_search):
                count_to_be_1 = 1
            if(list[3][pos2] == char_to_search):
                count_to_be_1 +=1
            if(count_to_be_1 == 1):
                count_of_trues +=1
    return count_of_trues


def main():
    count_of_trues = check_count_of_chars()
    print(count_of_trues)

    count_of_trues_pos = check_position_of_chars()
    print(count_of_trues_pos)

if __name__ == "__main__":
    main()
