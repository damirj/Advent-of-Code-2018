import re
import datetime
import numpy as np

input = open("input4.txt", "r")

input_content = input.readlines()

def parse(input_content):
    true_input = input_content
    for index, val in enumerate(input_content):
        true_input[index] = val.split('] ')
        true_input[index][0] = true_input[index][0][1:]
        true_input[index][1] = true_input[index][1].replace("\n", "")
    return true_input
   
def sort_input(true_input):
    true_input = sorted(true_input, key=lambda l:l[0])
    return true_input

def number_of_guards(true_input):
    guard_num = [int(re.findall(r'\d+', val[1])[0]) for val in true_input if val[1][0] == 'G']
    return len(guard_num)

def guards_sleep(true_input, guard_num):
    sleep_guards = np.zeros((guard_num, 2), dtype=object)
    fall_asleep = 0
    wake_up = 0
    working = 1
    guards_count = 0
    for index, value in enumerate(true_input):
        if value[1][0] == 'G':
            guard_id = re.findall(r'\d+',value[1])
            sleep_guards[guards_count, 0] = int(guard_id[0])
            if index != 0:
                sleep_guards[guards_count-1, 1] = sleep_time  
            guards_count += 1
            sleep_time = np.zeros(60)
            continue
        
        if working:
            fall_asleep = int(value[0][-2:])
            working = 0
        else:
            wake_up = int(value[0][-2:])
            working = 1
        
        if working:
            sleep_time[(fall_asleep):(wake_up)] = 1
    
    return sleep_guards

def unique_guard_ID(guards_sleep):
    unique_id = set()
    for val in guards_sleep:
        unique_id.add(val[0])
    return unique_id

def most_sleep_guard_REAL(guards_sleep, unique):
    num_of_unique_guards = len(unique)
    sum_of_sleep = np.zeros((num_of_unique_guards,2))
    for index,val in enumerate(unique):
        sum_of_sleep[index, 0] = val
        for val_guard in guards_sleep:
            if val == val_guard[0]:
                sum_of_sleep[index, 1] += np.count_nonzero(val_guard[1] == 1)
    
    return sum_of_sleep

def most_slept_minute(sleep_guards, best_guard): 
    most_sleep_guard = np.where(sleep_guards[:,0] == best_guard)[0]
    overlap_sleep = np.zeros(60)
    for val in range(len(most_sleep_guard)):
        overlap_sleep += sleep_guards[most_sleep_guard[val],1]

    return overlap_sleep

def all_slept_minute(sleep_guards, all_guards): 
    overlap_sleep_all = np.zeros((len(all_guards), 2), dtype=object)

    for index,val in enumerate(all_guards):
        overlap_sleep_all[index, 0] = val
        for val_guard in sleep_guards:
            if val == val_guard[0]:
                overlap_sleep_all[index][1] += val_guard[1]

    return overlap_sleep_all

def fetch_biggest_min(minutes):
    big = 0
    winner = 0
    for minut in minutes:
        if big < minut[1]:
            big = minut[1]
            winner = minut[0]
    return winner

def guard_with_most_sleep_in_same_minute(all_sleep):
    rjesenje = np.zeros(3)
    for guard in all_sleep:  
        for i in range(60):
            if rjesenje[2] < guard[1][i]:
                rjesenje[2] = guard[1][i]
                rjesenje[0] = guard[0]
                rjesenje[1] = i
    return rjesenje

parsiran = parse(input_content)
sortiran = sort_input(parsiran)
broj = number_of_guards(sortiran)
zaspali = guards_sleep(sortiran, broj)
unique = unique_guard_ID(zaspali)
lista_minuta_jedinstvenih_cuvara = most_sleep_guard_REAL(zaspali, unique)
spavalica = fetch_biggest_min(lista_minuta_jedinstvenih_cuvara)
most_slept_minute_array = most_slept_minute(zaspali, spavalica)
all_sleep = all_slept_minute(zaspali,unique)
rjesenje = guard_with_most_sleep_in_same_minute(all_sleep)
print(rjesenje)