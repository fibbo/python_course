def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    # Round to the nearest 0.5: multiply by 2, round, divide by 2 again
    return int(mark * 2 + 0.5) / 2


print(calculate_mark("18", "40"))
print(calculate_mark("34", "40"))
