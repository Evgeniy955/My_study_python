course1_students = {"Alice", "Bob", "Charlie", "David"}
course2_students = {"Charlie", "David", "Edward", "Fiona"}


def task_11():
    one_course = course1_students.difference(course2_students)
    students_both_courses = [student for student in course1_students if student in course2_students]
    print("one_course: ", one_course)
    print("students_both_courses: ", students_both_courses)


if __name__ == '__main__':
    task_11()