
def valid_path():
    starting_point = (0, 0)
    ending_point = (grid - 1, grid - 1)

    current_point = starting_point
    
    paths = [starting_point]
    invalid_path = [(9, 7), (8, 7), (6, 7), (6, 8)]
    

    directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1)]

    while current_point != ending_point:
         