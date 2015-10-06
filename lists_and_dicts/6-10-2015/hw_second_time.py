'''
http://pastebin.com/u8ntNmxd

Members DC Labels Homework DescriptionEdit Create an console application
in python that keeps the evidence of students.
Each student has the following information:
First name
Last name
Courses he attends
Grades for each courses
A way to maintain the list of the student Features:
add students
add courses
add grades for courses
find student
list students
give students with mean of all courses higher then a given grade
give students that are failing at at least one course
All these have to implemented using lists and dictionaries.
There will be a pretty menu from where you can do all of this (for reading from the console, see raw_input() function).
For any other questions, this should answer just about everything about the language.
List documentation Dictionary documentation From those links you can also find sets and tuples.
V1: http://pastebin.com/u8ntNmxd

'''


students = {}

def add_student(first_name, last_name, cnp):
    if students.get(cnp) is None:
        students[cnp] = {
            'first_name': first_name,
            'last_name': last_name,
            'courses': {}
        }
        return True
    else:
        return False


def add_course(cnp, course):
    if students[cnp]['courses'].get(course) is None:
        students[cnp]['courses'][course] = []
        return True
    else:
        return False


def add_grade(cnp, course, grade):
    student = students.get(cnp)
    if student is not None:
        if student['courses'].get(course) is None:
            return False
        else:
            student['courses'][course].append(grade)
            return True


def print_student(student, not_found_text=None):
    if student is None:
        if not_found_text is not None:
            print not_found_text
        return

    print 'First name: ', student['first_name']
    print 'Last name: ', student['last_name']
    print 'Courses: ', student['courses']
    print 10 * '-'


def find_student_by_cnp(cnp):
    return students.get(cnp)


def find_student_by_fname(fname):
    return filter(lambda student: student['first_name'] == fname, students.values())


def list_students():
    if not students:
        return
    for student in students.values():
        print_student(student)


def del_student_by_cnp(student_cnp):
    if students.get(student_cnp) is None:
        return False
    else:
        del students[student_cnp]
        return True


def del_student_by_fname(fname):
    if not students:
        return False

    is_deleted = False
    for student, atributes in students.items():
        if atributes['first_name'] == fname:
            del students[student]
            is_deleted = True

    return is_deleted


def del_student_by_lname(lname):
    if not students:
        return False

    is_deleted = False
    for student, atributes in students.items():
        if atributes['last_name'] == lname:
            del students[student]
            is_deleted = True

    return is_deleted


def courses_mean(student):
    courses = student['courses']
    return {
        course: float(sum(note)) / len(note)
        for course, note in courses.items()
    }


def grade_mean(student_cnp):
    student = students.get(student_cnp)
    if student is None:
        return False
    mediile = courses_mean(student).values()
    return float(sum(mediile)) / len(mediile)


def student_with_mean_higher_than(grade):
    return filter(
        lambda student_cnp: grade_mean(student_cnp) >= grade, students.keys())


def students_failing_at_at_least_one_course():
    studenti_failing = []
    for student in students.values():
        mediile = courses_mean(student).values()

        for medie in mediile:
            if medie < 5:
                studenti_failing.append(student)
                break

    return studenti_failing


def run():
    add_student('Andrei', 'Nasosu', 1)
    add_student('Andrei', 'Slabu', 5)
    add_student('Florin', 'Strunga', 2)
    add_student('Dumitru', 'Candale', 3)
    add_student('Ionut', 'Popescu', 4)

    for student in find_student_by_fname('bla'):
        print_student(student)


    add_course(1, 'Mate')
    add_course(1, 'Romana')
    add_course(2, 'Geogra')
    add_course(3, 'Bio')

    add_grade(1, 'Mate', 8)
    add_grade(1, 'Romana', 10)
    add_grade(2, 'Geogra', 7)
    add_grade(3, 'Bio', 6)

    print_student(find_student_by_cnp(1), not_found_text="Nu s-a gasit")
    print_student(find_student_by_cnp(2))
    print_student(find_student_by_cnp(3))

    list_students()

    del_student_by_fname('Andrei')

    list_students()

    del_student_by_cnp(2)

    list_students()

    del_student_by_lname('Candale')

    list_students()

    # grade_mean(1)

run()
