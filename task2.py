# Homework Week 1
# Task 2

class Student:

    total_grade = 0
    grade_number = 0

    def __init__(self, name, surname, age, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id
        self.subjects = {}

    def fullname(self):
        return '{} {}'.format(self.name, self.surname)

    def view_student(self):
        return 'Name: {}\nAge: {}\nID: {}'.format(self.fullname(), self.age, self.id)

    def add_subject(self, subject, grade=None):
        self.subjects.update({subject: grade})

    def remove_subjects(self, subject):
        self.subjects.pop(subject)

    def view_subjects(self):
        return 'The student, {}, is taking the following subjects: {}'.format(self.fullname(), self.subjects.keys())

    def view_grades(self):
        return 'The student, {}, grade in the following subjects are: {}'.format(self.fullname(), self.subjects)

    def average_grade(self):

        list_grade = list(self.subjects.values())
        total_grade = self.total_grade
        grade_number = self.grade_number

        for grade in list_grade:
            if grade is not None:
                total_grade += grade
                grade_number += 1

        average_grade = total_grade/grade_number
        avg_grade = round(average_grade, 2)

        return 'Average grade: ' + str(avg_grade)


class CFGStudent(Student):

    def __init__(self, name, surname, age, id, specialisation):
        super().__init__(name, surname, age, id)
        self.specialisation = specialisation

    def view_cfg_student(self):
        return '{}: {}\n{}'.format(self.fullname(), self.specialisation, self.average_grade())


# adding two students in Software and Data Science pathways
student_1 = CFGStudent('Najat', 'Yusuf', 21, 121, 'Software')
student_2 = CFGStudent('Hannah', 'Mitchell', 27, 122, 'Data Science')

# viewing student information
print('Viewing student information: ')
print(student_1.view_student())
print(student_2.view_student())

# adding subjects, only the third subject OOP for student 1 will not have a grade
student_1.add_subject('Python', 82)
student_1.add_subject('SQL', 79)
student_1.add_subject('OOP')

student_2.add_subject('Machine Learning', 86)
student_2.add_subject('Algorithms', 74)

print('\nViewing student 1 and 2 subjects: ')
print(student_1.view_subjects())
print(student_2.view_subjects())


# adding grades to subject OOP for student 1 and viewing average grade
print('\nAdding grades:')
print(student_1.view_grades())
print(student_1.average_grade())
student_1.add_subject('OOP', 59)
print(student_1.view_grades())
print(student_1.average_grade())


# removing subjects SQL
print('\nRemoving subjects:')
student_1.remove_subjects('SQL')
print(student_1.view_subjects())
print(student_1.view_grades())
print(student_1.average_grade())

# viewing the CFG student
print('\nViewing CFG student details:')
print(student_1.view_cfg_student())