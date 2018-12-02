from iteration_utilities import duplicates

input = open("Day2/Input.txt", "r")

input_content = input.read()
input_list = input_content.split()
check_list = [0, 0]

def FindDuplicates(input_value, check_list):
    duplicates_list = list(duplicates(input_value))
    
    triplicate_list = list(duplicates(duplicates_list))
    duplicates_list = [value for value in duplicates_list + triplicate_list if value not in duplicates_list or value not in triplicate_list]

    if duplicates_list:
        check_list[0] += 1

    return check_list

def FindTriplicate(input_value, check_list):
    duplicates_list = list(duplicates(input_value))    
    triplicate_list = list(duplicates(duplicates_list))
    if triplicate_list:
        check_list[1] += 1

    return check_list


for value in input_list:
    check_list = FindDuplicates(value, check_list)
    check_list = FindTriplicate(value, check_list)


checksum = check_list[0] * check_list[1]
print(checksum)