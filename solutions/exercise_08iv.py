def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return int(mark * 2 + 0.5) / 2


def has_passed(mark):
    return mark >= 4


def main():
    max_points = input("Enter maximum score: ")

    grade_dict = {}

    while True:
        name = input("Enter the name or type exit to quit: ")
        if name == "exit":
            break
        points = input("Enter points: ")
        grade_dict[name] = calculate_mark(points, max_points)

    total = 0
    best_name = None
    best_grade = None
    worst_name = None
    worst_grade = None
    for name, grade in grade_dict.items():
        total = total + grade
        if has_passed(grade):
            print(f"{name} has passed with {grade}")
        else:
            print(f"{name} has failed with {grade}")
        if best_grade is None or grade > best_grade:
            best_name = name
            best_grade = grade
        if worst_grade is None or grade < worst_grade:
            worst_name = name
            worst_grade = grade

    # Without this check the division would crash when nothing was entered
    if len(grade_dict) > 0:
        print(f"Average: {total / len(grade_dict):.2f}")
        print(f"Best: {best_name} with {best_grade}")
        print(f"Worst: {worst_name} with {worst_grade}")


main()
