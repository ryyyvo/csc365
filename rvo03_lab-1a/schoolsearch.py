import os 

STUDENTS_PATH = 'rvo03_lab-1a/students.txt' # change path if needed

def parse_students():
    students = []

    with open(STUDENTS_PATH, 'r') as file:
        for line in file:
            fields = line.strip().split(',')

            if len(fields) != 8:
                print("Incorrect number of columns in a line in students.txt")
                exit(1)

            student = {
                "StLastName": fields[0],
                "StFirstName": fields[1],
                "Grade": int(fields[2]),
                "Classroom": int(fields[3]),
                "Bus": int(fields[4]),
                "GPA": fields[5],
                "TLastName": fields[6],
                "TFirstName": fields[7]
            }
            students.append(student)


    return students

def find_by_StLastName(lastname, students): #R4
    for student in students:
        if student['StLastName'] == lastname:
            print(student['StLastName'], student['StFirstName'], student['Grade'], student['Classroom'], student['TLastName'], student['TFirstName'])

def find_by_StLastName_bus(lastname, students): #R5
    for student in students: 
        if student['StLastName'] == lastname:
            print(student['StLastName'], student['StFirstName'], student['Bus'])

def find_by_TLastName(lastname, students): #R6
    for student in students:
        if student['TLastName'] == lastname:
            print(student['StLastName'], student['StFirstName'])

def find_by_grade(grade, students): #R7
    for student in students:
        if student['Grade'] == grade:
            print(student['StLastName'], student['StFirstName'])

def find_by_bus(route, students): #R8
    for student in students:
        if student['Bus'] == route:
            print(student['StLastName'], student['StFirstName'], student['Grade'], student['Classroom'])

def find_by_grade_high_low(grade, lowhigh, students): #R9
    temp = False
    tempGPA = False
    for student in students:
        if student['Grade'] == grade:
            if lowhigh == "HIGH" or lowhigh == "H":
                if not tempGPA:
                    tempGPA = 0 
                if float(student['GPA']) >= tempGPA:
                    tempGPA = float(student['GPA'])
                    temp = student
            elif lowhigh == "LOW" or lowhigh == "L":
                if not tempGPA:
                    tempGPA = 5
                if float(student['GPA']) <= tempGPA:
                    tempGPA = float(student['GPA'])
                    temp = student
    if not temp:
        return
    print(temp['StLastName'], temp['StFirstName'], temp['GPA'], temp['TLastName'], temp['TFirstName'], temp['Bus'])
                    

def find_by_average(grade, students): #R10
    totalGP = 0
    numberOfStudents = 0
    for student in students:
        if student['Grade'] == grade:
            totalGP += float(student['GPA'])
            numberOfStudents += 1
    if numberOfStudents == 0:
        return
    gradeLevelGPA = round(totalGP/numberOfStudents, 2)
    print(grade, gradeLevelGPA)

def info(students): #R11
    totalStudentsPerGrade = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    for student in students:
        totalStudentsPerGrade[str(student['Grade'])] += 1
    print('0: ' + str(totalStudentsPerGrade['0']) + ", " \
          '1: ' + str(totalStudentsPerGrade['1']) + ", " \
          '2: ' + str(totalStudentsPerGrade['2']) + ", " \
          '3: ' + str(totalStudentsPerGrade['3']) + ", " \
          '4: ' + str(totalStudentsPerGrade['4']) + ", " \
          '5: ' + str(totalStudentsPerGrade['5']) + ", " \
          '6: ' + str(totalStudentsPerGrade['6'])
          )

def main():
    if not os.path.exists(STUDENTS_PATH):
        print("students.txt does not exist.")
        exit(1)
    students = parse_students()
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