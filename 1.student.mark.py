course_id = []
course_name = []

student_name = []
student_id = []
student_mark = []
n2 = int(input("Enter the amount of students: "))
n1 = int(input("Enter the amount of courses: "))


def Input(n1, n2):
    for i in range(0, n1):
        print("--------------------------")
        print("Course" + str(i+1) + ":")
        a = input("Enter the course id: ")
        course_id.append(a)
        b = input("Enter the course name:")
        course_name.append(b)
        print("--------------------------")

        for j in range(0, n2):
            print("Student:")
            x = input("Enter the student name: ")
            student_name.append(x)

            y = input("Enter the student id: ")
            student_id.append(y)

            z = input("Enter the student mark: ")
            student_mark.append(z)
            print("--------------------------")

        print("\n")
        print("--------------------------")
        print("///////////--INFO--///////////")
        print("Course id: " + course_id[i] +"||" + "Course name: " + course_name[i])
        print("Student_id: "+ student_id[i] + "||" + "Student's name: " + student_name[i])
        print("Student_id: "+ student_id[i+1] + "||" + "Student's name: " + student_name[i+1])
        print("students' marks in order: " + str(student_mark))
        print("//////////////////////////////")
        print("--------------------------")
        print("\n")

Input(n1, n2)


