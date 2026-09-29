'''
from abc import ABC, abstractmethod


class Course:

    def __init__(self, course_id, course_name, schedule):
        self.course_id = course_id
        self.course_name = course_name
        self.schedule = schedule
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print("\nStudents enrolled in", self.course_name)

        for student in self.students:
            print(student.get_name())


class Student(ABC):

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.__name = name
        self.__courses = []
        self.__grades = {}

    def get_name(self):
        return self.__name

    @abstractmethod
    def view_schedule(self):
        pass

    def enroll(self, course):

        if course not in self.__courses:
            self.__courses.append(course)
            course.add_student(self)

            print(
                self.__name,
                "enrolled in",
                course.course_name
            )

        else:
            print("Already enrolled in this course.")

    def add_grade(self, course, grade):

        if course in self.__courses:
            self.__grades[course.course_name] = grade

        else:
            print("Student is not enrolled in this course.")

    def view_grades(self):

        print("\nGrades of", self.__name)

        if not self.__grades:
            print("No grades available.")
            return

        for course, grade in self.__grades.items():
            print(course, ":", grade)


class UndergraduateStudent(Student):

    def view_schedule(self):

        print("\nUndergraduate Schedule -", self.get_name())

        for course in self._Student__courses:
            print(
                course.course_name,
                "-",
                course.schedule
            )


class GraduateStudent(Student):

    def view_schedule(self):

        print("\nGraduate Schedule -", self.get_name())

        for course in self._Student__courses:

            if course.course_name == "Python Programming":
                print(
                    course.course_name,
                    "- Monday 2 PM"
                )

            elif course.course_name == "Database Management":
                print(
                    course.course_name,
                    "- Wednesday 3 PM"
                )


class Faculty:

    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.__name = name
        self.__courses = []

    def get_name(self):
        return self.__name

    def assign_course(self, course):

        self.__courses.append(course)

        print(
            course.course_name,
            "assigned to",
            self.__name
        )

    def view_courses(self):

        print(
            "\nCourses assigned to",
            self.__name
        )

        for course in self.__courses:
            print(course.course_name)

    def view_student_roster(self):

        print(
            "\nStudent Roster -",
            self.__name
        )

        for course in self.__courses:

            print("\nCourse:", course.course_name)

            for student in course.students:
                print(student.get_name())


class University:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        self.faculty = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def show_details(self):

        print("\n===== UNIVERSITY =====")
        print("University:", self.name)

        print("\nStudents:")

        for student in self.students:
            print(
                student.student_id,
                "-",
                student.get_name()
            )

        print("\nCourses:")

        for course in self.courses:
            print(
                course.course_id,
                "-",
                course.course_name
            )

        print("\nFaculty:")

        for faculty in self.faculty:
            print(
                faculty.faculty_id,
                "-",
                faculty.get_name()
            )


class Department(University):

    def __init__(self, university_name, department_name):
        super().__init__(university_name)
        self.department_name = department_name

    def show_department(self):

        print("\nDepartment:", self.department_name)
        print("University:", self.name)


university = University("Parul University")


python = Course(
    "C101",
    "Python Programming",
    "Monday 10 AM"
)

database = Course(
    "C102",
    "Database Management",
    "Tuesday 11 AM"
)


student1 = UndergraduateStudent(
    "S101",
    "Jaswanth"
)

student2 = GraduateStudent(
    "S102",
    "Yaswanth"
)

student3 = UndergraduateStudent(
    "S103",
    "Jahnavi"
)


faculty1 = Faculty(
    "F101",
    "Dr. Saketh"
)

faculty2 = Faculty(
    "F102",
    "Dr. Anjali"
)


university.add_student(student1)
university.add_student(student2)
university.add_student(student3)

university.add_course(python)
university.add_course(database)

university.add_faculty(faculty1)
university.add_faculty(faculty2)


student1.enroll(python)
student1.enroll(database)

student2.enroll(python)
student2.enroll(database)

student3.enroll(python)
student3.enroll(database)


faculty1.assign_course(python)
faculty2.assign_course(database)


student1.add_grade(python, "A")
student1.add_grade(database, "B+")

student2.add_grade(python, "A+")
student2.add_grade(database, "A")

student3.add_grade(python, "A")
student3.add_grade(database, "A+")


student1.view_schedule()
student2.view_schedule()
student3.view_schedule()


student1.view_grades()
student2.view_grades()
student3.view_grades()


faculty1.view_courses()
faculty1.view_student_roster()

faculty2.view_courses()
faculty2.view_student_roster()


university.show_details()


department = Department(
    "Parul University",
    "Computer Science and Engineering"
)

department.show_department()
'''
#First we will define the function to take eligible

def eligible(attendence):
    """Eligible checker"""
    return attendence >=75

#to take marks of students we will create a list
+

students= []
for i in range(5):
    name= input(f'enter the student name: {i+1}')
    while True:
        #Exception handling to check all cases of +ve,-ve
        try:
            attendence= float(input(f'enter the attendence for {name}\ in 0-100'))
            #if attendence >= 0 and attendence <=100:
            if 0<= attendence <= 100: #chain comparision operation
                break
            print("Enter the value only 0-100")
        except ValueError:
            print("Enter only +ve values and make sure its in given range")
    students.append(attendence)
    print(students)
