input = open("Day2/Input.txt", "r")

input_content = input.read()
input_list = input_content.split()

def FindCorrectBoxes(input_list):
    string_size = len(input_list[0])
    correct_box_value = []
    
    for ind, value in enumerate(input_list):
        for value_next in input_list[ind+1:]:
            count_letters = 0
            not_match = []
            for index in range(string_size):
                if value[index] == value_next[index]:
                    count_letters += 1
                else:
                    not_match.append(index)
                    if len(not_match) > 1:
                        continue

            if count_letters == (string_size-1):
                    correct_box_value.append(value[:not_match[0]] + value[not_match[0]+1:])
                    
            if ind == len(input_list)-2:
                return correct_box_value   

print(FindCorrectBoxes(input_list))


            
