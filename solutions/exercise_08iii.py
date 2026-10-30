def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return int(mark * 2 + 0.5) / 2


def main():
    max_points = input("Enter maximum score: ")

    grade_dict = {}

    while True:
        name = input("Enter the name or type exit to quit: ")
        if name == "exit":
            break
        points = input("Enter points: ")
        grade_dict[name] = calculate_mark(points, max_points)

    for name, grade in grade_dict.items():
        print(f"{name} has grade: {grade}")


main()
