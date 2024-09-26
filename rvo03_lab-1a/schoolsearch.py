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

def find_by_StLastName(lastname, students):
    for student in students:
        if student['StLastName'] == lastname:
            print(student['StLastName'], student['StFirstName'], student['Grade'], student['Classroom'], student['TLastName'], student['TFirstName'])

def main():
    if not os.path.exists(STUDENTS_PATH):
        print("students.txt does not exist.")
        exit(1)
    print("students.txt does exist.")
    students = parse_students()
    while (True):
        user_input = input("Please input a search instruction: ")

        instruction = user_input.split()

        if len(instruction) == 1:
            if (instruction[0] == "Q") or (instruction[0] == "Quit"):
                exit(0)

        elif len(instruction) == 2:
            if (instruction[0] == "S") or (instruction[0] == "Student"):
                find_by_StLastName(instruction[1], students)



    

if __name__ == '__main__':
    main()