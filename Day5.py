import string
input = open("input5.txt", "r")

input_content = input.read()

def replace_all(input_content):
    lenght = len(input_content)
    for val in range(2000):
        for i in range(len(string.ascii_lowercase)):
            temp = string.ascii_lowercase[i] + string.ascii_uppercase[i]
            if temp in input_content:
                input_content = input_content.replace(temp,"")

            temp = string.ascii_uppercase[i] +string.ascii_lowercase[i]
            if temp in input_content:
                input_content = input_content.replace(temp,"")

        if(lenght > len(input_content)):
            lenght = len(input_content)
        else:
            return len(input_content)

def part_two(input_content):
    lenghts = []
    for i in range(len(string.ascii_lowercase)):
        temp1 = string.ascii_lowercase[i]
        temp2 = string.ascii_uppercase[i]
        temp_content = input_content.replace(temp1, "")
        temp_content = temp_content.replace(temp2, "")
        lenghts.append(replace_all(temp_content))
    return lenghts    


lenghts = part_two(input_content)
minimal_lenght = min(lenghts)
print(minimal_lenght)

