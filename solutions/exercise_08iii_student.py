def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return int(mark * 2 + 0.5) / 2


class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name

    def __str__(self):
        return f"id: {self.id} \t name: {self.name}"


def main():
    student_id = 0
    max_points = input("Enter maximum score: ")

    grade_dict = {}

    while True:
        name = input("Enter the name or type exit to quit: ")
        if name == "exit":
            break
        student = Student(student_id, name)
        student_id += 1
        points = input("Enter points: ")
        grade_dict[student] = calculate_mark(points, max_points)

    for student, grade in grade_dict.items():
        print(f"{student} has grade: {grade}")


main()
