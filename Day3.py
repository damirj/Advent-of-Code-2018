from itertools import chain
import numpy as np
input = open("input.txt", "r")

input_content = input.read()
input_list = input_content.split("\n")

def parse_input(input_list):
    new_list = input_list
    for index, value in enumerate(input_list):
        new_list[index] = value.split()
        new_list[index].remove('@')
        new_list[index][0] = new_list[index][0][1:]
        new_list[index][1] = new_list[index][1][:-1]
        new_list[index][1] = new_list[index][1].split(",")
        new_list[index][2] = new_list[index][2].split("x")
        new_list[index][0] = int(new_list[index][0])
        new_list[index][0] = [new_list[index][0]]
        new_list[index] = list(chain.from_iterable(new_list[index]))
        new_list[index] = list(map(int, new_list[index]))
    return new_list

def fill_rectangle(input_list):
    elven_claims = np.zeros((1500, 1500))
    for val in input_list:
        for row in range(0, val[4]):
            for col in range(0, val[3]):
                elven_claims[val[2]+row, val[1]+col] += val[0]
                if elven_claims[val[2]+row, val[1]+col] != val[0]:
                    elven_claims[val[2]+row, val[1]+col] = -9                     
    return elven_claims    

def count_overlaps(elven_claims):
    count = np.count_nonzero(elven_claims == -9)
    return count

def check_intact(elven_claims, input_list):
    for val in input_list:
        if check_intact_single(val, elven_claims):
            return val[0]
    return None
        
def check_intact_single(val, elven_claims):
    for row in range(0, val[4]):
            for col in range(0, val[3]):
                if elven_claims[val[2]+row, val[1]+col] == -9:
                    return False
    return True

input_list = parse_input(input_list)
elven_claims = fill_rectangle(input_list)
square_inch = count_overlaps(elven_claims)
intact_ID = check_intact(elven_claims, input_list)
print('Square inch of wasted fabric: {}'.format(square_inch))
print('ID of the intact elven claim: {}'.format(intact_ID))