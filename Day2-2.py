input = open("Day2/Input.txt", "r")

input_content = input.read()
input_list = input_content.split()

def find_correct_boxes(input_list):    
    for ind, value in enumerate(input_list):
        for value_next in input_list[ind+1:]:
            differing_char_index = string_comparison(value, value_next)
            if differing_char_index:
                return remove_differing_char(value, differing_char_index)
                    
        if ind == len(input_list)-2:
            return None

def string_comparison(first, second):
    differing_char_index = []
    for index in range(len(first)):
        if first[index] != second[index]:
            differing_char_index.append(index)
            if len(differing_char_index) > 1:
                return None

    return differing_char_index[0]

def remove_differing_char(correct_box_ID, index):
    common_letters_correct_box = correct_box_ID[:index] + correct_box_ID[index + 1:]
    return common_letters_correct_box
    
print(find_correct_boxes(input_list))
