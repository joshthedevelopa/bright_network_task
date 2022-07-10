import random, math;

def random_obstacles(lenght = 20, grid = 10, starting_point = (0, 0), delivery_point = (9, 9)):
    new_obstacles = []

    while len(new_obstacles) <= lenght:
        x = math.floor(random.random() * (grid - 1))
        y = math.floor(random.random() * (grid - 1))
        point = (x, y)

        if point not in new_obstacles and (point != starting_point or point != delivery_point):
            new_obstacles.append((x, y))

    return new_obstacles


def valid_path(grid = 10, starting_point = (0, 0), delivery_point = (9, 9), obstacles = [(9, 7), (8, 7), (6, 7), (6, 8)]):   
    valid_points = [starting_point]
    prev_points = {}

    directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1)]

    for current_point in valid_points:
        if valid_points[-1] == delivery_point:
            break
        
        for direction in directions:
            next_point = (current_point[0] + direction[0], current_point[1] + direction[1])

            if next_point in obstacles or next_point in valid_points:
                continue

            if next_point[0] < 0 or next_point[0] > (grid - 1):
                continue

            if next_point[1] < 0 or next_point[1] > (grid - 1):
                continue

            valid_points.append(next_point)
            prev_points[next_point] = current_point
   
    path = [delivery_point]
    while path[-1] != starting_point:
        path.append(prev_points[path[-1]])

    path.reverse()
    return path


print(valid_path(
    grid= 10, 
    starting_point = (0, 0), 
    delivery_point = (9, 9), 
    obstacles = [(9, 7), (8, 7), (6, 7), (6, 8)] + random_obstacles()
))