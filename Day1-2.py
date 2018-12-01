import timeit
input = open("Day1/Input1.txt", "r")

input_content = input.read()
input_list = input_content.split()
input_list = [int(i) for i in input_list]

def duplicate_frequency(input_list):
    frequency = 0
    resulting_frequency = [0]
  
    while True:
        for value in input_list:
            frequency += value
            resulting_frequency.append(frequency)

            if frequency in resulting_frequency[:-1]:
                return frequency

            
def duplicate_frequency_set(input_list):
    frequency = 0
    resulting_frequency = {0}

    while True:
        for value in input_list:
            frequency += value

            if frequency in resulting_frequency:
                return frequency

            resulting_frequency.add(frequency)


SETUP_CODE = '''
input = open("Day1/Input1.txt", "r")

input_content = input.read()
input_list = input_content.split()
input_list = [int(i) for i in input_list]
def duplicate_frequency(input_list):
    frequency = 0
    resulting_frequency = [0]
  
    while True:
        for value in input_list:
            frequency += value
            resulting_frequency.append(frequency)

            if frequency in resulting_frequency[:-1]:
                return frequency

def duplicate_frequency_set(input_list):
    frequency = 0
    resulting_frequency = {0}

    while True:
        for value in input_list:
            frequency += value

            if frequency in resulting_frequency:
                return frequency

            resulting_frequency.add(frequency)                
'''

TEST_CODE_LIST = '''
print(duplicate_frequency(input_list))
'''

TEST_CODE_SET = '''
print(duplicate_frequency_set(input_list))
'''

time_list = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE_LIST, number=1)
time_set = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE_SET, number=1)

print('List time: {}'.format(time_list))
print('Set time: {}'.format(time_set))

