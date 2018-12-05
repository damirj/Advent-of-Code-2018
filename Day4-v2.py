import numpy as np
import re

input = open("Day4/Input4.txt", "r")

input_content = input.readlines()

class guard:
    def __init__(self, id):
        self.id = id
        self.sleep_cycle = np.zeros(60)
        self.all_shifts = []
        self.minutes_of_sleep = 0
        self.times_slept_on_minute = 0
        self.most_slept_on_minute = -1
        self.fall_asleep = 0
        self.wakes_up = 0
        self.sleep_cycle_shift = np.zeros(60)

    def sleep_wake_cycle(self):
        self.sleep_cycle[int(self.fall_asleep):int(self.wakes_up)] += 1
        self.sleep_cycle_shift[int(self.fall_asleep):int(self.wakes_up)] = 1

    def add_work_shift(self):
        self.all_shifts.append(self.sleep_cycle_shift)
        
    def calculate_minutes_of_sleep(self):
        self.minutes_of_sleep = np.sum(self.sleep_cycle)

    def calculate_most_slept_on_minute(self):
        self.most_slept_on_minute = np.argmax(self.sleep_cycle)
        self.times_slept_on_minute = np.amax(self.sleep_cycle)


def parse(input_content):
    parsed_input = input_content
    for index, val in enumerate(input_content):
        parsed_input[index] = val.split('] ')
        parsed_input[index][0] = parsed_input[index][0][1:]
        parsed_input[index][1] = parsed_input[index][1].replace("\n", "")
    return parsed_input
   
def sort_input(parsed_input):
    parsed_input = sorted(parsed_input, key=lambda l:l[0])
    return parsed_input

def guards_sleep_record(parsed_input):
    list_of_guards = []
    index = 0
    for time, action in parsed_input:
        if "begins shift" in action:
            if index != 0:
                list_of_guards[index].add_work_shift()
            guard_id = int(re.findall(r'\d+', action)[0])
            IDs = [guard.id for guard in list_of_guards]
            if guard_id not in IDs:
                list_of_guards.append(guard(guard_id))
                index = len(list_of_guards)-1
                continue
            else:
                index = IDs.index(guard_id)
                continue

        if "falls asleep" in action:
            list_of_guards[index].fall_asleep = time[-2:]
        if "wakes up" in action:
            list_of_guards[index].wakes_up = time[-2:]
            list_of_guards[index].sleep_wake_cycle()

    return list_of_guards

def get_results(list_of_guards):
    for guard in list_of_guards:
        guard.calculate_minutes_of_sleep()
        guard.calculate_most_slept_on_minute()

    times_slept_on_minute = 0
    minute = 0
    minutes_of_sleep = 0
    guard_id_1 = 0
    guard_id_2 = 0
    minute2 = 0
    for guard in list_of_guards:
        if times_slept_on_minute < guard.times_slept_on_minute:
            times_slept_on_minute = guard.times_slept_on_minute
            minute = guard.most_slept_on_minute
            guard_id_2 = guard.id
        for shift in guard.all_shifts:
            if minutes_of_sleep < guard.minutes_of_sleep:
                minutes_of_sleep = guard.minutes_of_sleep
                guard_id_1 = guard.id
                minute2 = np.argmax(guard.sleep_cycle)

    print(guard_id_1*minute2)
    print(guard_id_2*minute)


parsed_input = parse(input_content)
sorted_input = sorted(parsed_input)
list_of_guards = guards_sleep_record(sorted_input)
get_results(list_of_guards)