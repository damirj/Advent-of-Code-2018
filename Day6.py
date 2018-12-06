import re
import numpy as np

input = open("Day6/Input6.txt", "r")

input_content = input.readlines()
list_of_coordinates = [list(map(int, re.findall(r'\d+', value))) for value in input_content]

class coordinates_unit:

    def __init__(self, id, x, y):
        self.id = id
        self.X = x
        self.Y = y
        self.area_size = 0
        self.man_distance = 0

    def area(self,coordinates_table):
        self.area_size = np.count_nonzero(coordinates_table == self.id)


def initialize_coordinates(list_of_coordinates):
    coordinates_unit_list = []
    for id, value in enumerate(list_of_coordinates, 1):
        coordinates_unit_list.append(coordinates_unit(id, value[0], value[1]))
    return coordinates_unit_list

def fill_coordinate_table(coordinates_unit_list):
    coordinates_table = np.empty((500,500))
    for coordinates, value in np.ndenumerate(coordinates_table):
        coordinates_table[coordinates[0], coordinates[1]] = get_smallest_manhattan_distance(coordinates,coordinates_unit_list)
    return coordinates_table

def get_smallest_manhattan_distance(coordinates, coordinates_unit_list):
    smallest_distance = 99999
    distance_list = []
    smallest_distance_id = 0
    for unit in coordinates_unit_list:
        unit.man_distance = calculate_manhattan_distance(coordinates[0], coordinates[1], unit.X, unit.Y)
        distance_list.append(unit.man_distance)
        if smallest_distance > unit.man_distance:
            smallest_distance = unit.man_distance
            smallest_distance_id = unit.id
    if distance_list.count(smallest_distance) > 1:
        return 0
    else:
        return smallest_distance_id

def calculate_manhattan_distance(table_x, table_y, id_x, id_y):
    x = abs(table_x - id_x)
    y = abs(table_y - id_y)
    manhattan_distance = x + y
    return manhattan_distance

def remove_infinite_id(coordinates_table):
    infinite_id1 = np.unique(coordinates_table[0, :])
    infinite_id2 = np.unique(coordinates_table[-1, :])
    infinite_id3 = np.unique(coordinates_table[:, 0])
    infinite_id4 = np.unique(coordinates_table[:, -1])
    all_infinite_id = np.concatenate([infinite_id1, infinite_id2, infinite_id3, infinite_id4])
    all_infinite_id = np.unique(all_infinite_id)
    all_id = np.unique(coordinates_table)
    finite_id = []
    for id in all_id:
        if id not in all_infinite_id:
            finite_id.append(id)
    return finite_id
    
def calculate_area(coordinates_table, coordinates_unit_list, finite_id):
    areas = []
    for unit in coordinates_unit_list:
        if unit.id in finite_id:
            unit.area(coordinates_table)
            areas.append(unit.area_size)
    return max(areas)

def sum_of_distances_at_point(coordinates, coordinates_unit_list):
    sum_of_distances = 0
    for unit in coordinates_unit_list:
        unit.man_distance = calculate_manhattan_distance(coordinates[0], coordinates[1], unit.X, unit.Y)
        sum_of_distances += unit.man_distance
    if sum_of_distances < 10000:
        return True      
    else:
        return False

def sum_of_distances(coordinates_table, coordinates_unit_list):
    area_size = 0
    for coordinates, value in np.ndenumerate(coordinates_table):
        if sum_of_distances_at_point(coordinates, coordinates_unit_list):
            area_size += 1
    return area_size


coordinates_unit_list = initialize_coordinates(list_of_coordinates)
coordinates_table = fill_coordinate_table(coordinates_unit_list)
finite_id = remove_infinite_id(coordinates_table)
max_area = calculate_area(coordinates_table, coordinates_unit_list, finite_id)
print(max_area)

area_size_of_under_10000 = sum_of_distances(coordinates_table, coordinates_unit_list)
print(area_size_of_under_10000)


    

