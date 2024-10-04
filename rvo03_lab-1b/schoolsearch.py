'''
• Requirement NR1. Given a classroom number, list all students assigned to it.

• Requirement NR2. Given a classroom number, find the teacher (or teachers) teaching

in it (In our test file, there in one teacher per classroom. 
However, your search algorithm cannot assume that it will
always be the case. If a classroom has multiple teachers 
they should be considered co-teachers. All co-teachers of
a classroom should be included wherever teacher information is printed.)

• Requirement NR3. Given a grade, find all teachers who teach it.

• Requirement NR4. Report the enrollments broken down by classroom 
(i.e., output a
list of classrooms ordered by classroom number, 
with a total number of students in each
of the classrooms).

Requirement NR5. Add to your program the commands that allow a data analyst to extract
appropriate data to be able to analyze whether student GPAs are affected by the student’s
grades, student’s teachers or the bus routes the students are on.

'''

import os 

STUDENTS_PATH = 'rvo03_lab-1b/list.txt' # change path if needed
TEACHERS_PATH = 'rvo03_lab-1b/teachers.txt' # change path if needed


def parse_students():
    students = []

    with open(STUDENTS_PATH, 'r') as file:
        for line in file:
            fields = line.strip().split(',')

            if len(fields) != 6:
                print("Incorrect number of columns in a line in students.txt")
                exit(1)

            student = {
                "StLastName": fields[0],
                "StFirstName": fields[1],
                "Grade": int(fields[2]),
                "Classroom": int(fields[3]),
                "Bus": int(fields[4]),
                "GPA": fields[5]
            }
            students.append(student)


    return students

def parse_teachers():
    teachers = []

    with open(TEACHERS_PATH, 'r') as file:
        for line in file:
            fields = line.strip().split(',')

            if len(fields) != 3:
                print("Incorrect number of columns in a line in students.txt")
                exit(1)

            teacher = {
                "TLastName": fields[0],
                "TFirstName": fields[1],
                "Classroom": int(fields[2])
            }

            teachers.append(teacher)


    return teachers

def parse_classrooms(students, teachers):
    classrooms = {}

    for teacher in teachers:
        if teacher["Classroom"] not in classrooms:
            classroom = {
                        "TLastName": [teacher["TLastName"]],
                        "TFirstName": [teacher["TFirstName"]],
                        "StLastName": [],
                        "StFirstName": [],
                        "TotalStudents": 0
                        }
            classrooms[teacher["Classroom"]] = classroom
        else:
            classrooms[teacher["Classroom"]]["TLastName"].append(teacher["TLastName"])
            classrooms[teacher["Classroom"]]["TFirstName"].append(teacher["TFirstName"])


    for student in students:

        
    return classrooms


def main():
    if not os.path.exists(STUDENTS_PATH):
        print("list.txt does not exist.")
        exit(1)
    if not os.path.exists(TEACHERS_PATH):
        print("teachers.txt does not exist.")
        exit(1)
    students = parse_students()
    teachers = parse_teachers()
    classrooms = parse_classrooms(students, teachers)
    while (True):
        user_input = input("Please input a search instruction: ")

        instruction = (user_input.upper()).split()

        if len(instruction) == 1:
            if (instruction[0] == "Q") or (instruction[0] == "QUIT"): #R12
                exit(0)
            elif (instruction[0] == "I") or (instruction[0] == "INFO"): #R11
                info(students)

        elif len(instruction) == 2:
            if (instruction[0] == "S") or (instruction[0] == "STUDENT"): #R4
                find_by_StLastName(instruction[1], students)
            elif (instruction[0] == "T") or (instruction[0] == "TEACHER"): #R6
                find_by_TLastName(instruction[1], students)
            elif (instruction[0] == "G") or (instruction[0] == "GRADE"): #R7
                find_by_grade(int(instruction[1]), students)
            elif (instruction[0] == "B") or (instruction[0] == "BUS"): #R8
                find_by_bus(int(instruction[1]), students)
            elif (instruction[0] == "A") or (instruction[0] == "AVERAGE"): #R10
                find_by_average(int(instruction[1]), students)

        elif len(instruction) == 3:
            if (instruction[0] == "S" or instruction[0] == "STUDENT") and (instruction[2] == "B" or instruction[2] == "BUS"): #R5
                find_by_StLastName_bus(instruction[1], students)
            if (instruction[0] == "G") or (instruction[0] == "GRADE"): #R9
                find_by_grade_high_low(int(instruction[1]), instruction[2], students)

if __name__ == '__main__':
    main()