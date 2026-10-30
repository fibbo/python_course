def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return int(mark * 2 + 0.5) / 2


max_points = input("Enter maximum score: ")

while True:
    points = input("Enter points or type exit to quit: ")
    if points == "exit":
        break
    print(calculate_mark(points, max_points))
