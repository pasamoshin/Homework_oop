from models import *


class WorkPerson():

    def average_grade(self, person):
        grades = 0
        for grade in person.grade:
            grades += grade.grade
        try:
            res = round(grades/person.grade.count(), 2)
        except ZeroDivisionError:
            res = 0
        finally:
            return res


class WorkStudent(WorkPerson):
    def __init__(self, person_id):
        self.person = Student.get(Student.id == person_id)

    def __str__(self):
        return (f'{self.person.name} {self.person.surname}' + '\nКурсы в процессе обучения: ' +
                ', '.join(course.course for course in self.person.course_progress) + '\nЗавершенные курсы: ' +
                ', '.join(course.course for course in self.person.finished_courses) +
                '\nСредний бал за домашние задания: ' + str(self.average_grade(self.person)))

    def rate_grade_lecturer(self, lecturer_id, course, grade):
        lecturer = Lecturer.get_or_none(Lecturer.id == lecturer_id)
        if lecturer == None:
            print('Лектора нет в базе.')
            return 'Ошибка'
        course_lecturer = LecturerCourse.get_or_none(
            LecturerCourse.person_id == lecturer_id, LecturerCourse.course == course)

        if course_lecturer == None:
            print('Курс не закрелпен за лектором.')
            return 'Ошибка'

        course_student = CourseProgressStudent.get_or_none(
            CourseProgressStudent.person_id == self, CourseProgressStudent.course == course)
        if course_student == None:
            print('Вы не проходите указаннных курс.')
            return 'Ошибка'

        GradeLecturer(person=lecturer, course=course, grade=grade).save()

    def add_course_progress(self, course):
        if CourseProgressStudent.get_or_none(person=self, course=course) == None:
            CourseProgressStudent(person=self, course=course).save()
            print('Курс добавлен')
            return 'Курс добавлен'
        else:
            print('Студент уже проходит указанный курс')
            return 'Ошибка'

    def __str__(self):
        return (f'\nСтудент: {self.person.name} {self.person.surname}' + '\nКурсы в процессе обучения: ' +
                ', '.join(course.course for course in self.person.course_progress) + '\nЗавершенные курсы: ' +
                ', '.join(course.course for course in self.person.finished_courses) +
                '\nСредний бал за домашние задания: ' + str(self.average_grade(self.person)))

    def __lt__(self, other):
        grade_person1 = self.average_grade(self.person)
        grade_person2 = self.average_grade(other.person)
        if grade_person1 > grade_person2:
            return f'{self.person.name} {self.person.surname} успешнее {other.person.name} {other.person.surname}.'
        elif grade_person1 == grade_person2:
            return f'{self.person.name} {self.person.surname} = {other.person.name} {other.person.surname}.'
        else:
            return f'{other.person.name} {other.person.surname} успешнее {self.person.name} {self.person.surname}.'


class WorkLecturer(WorkPerson):
    def __init__(self, person_id):
        self.person = Lecturer.get(Lecturer.id == person_id)


    def add_course(self, course):
        if LecturerCourse.get_or_none(person=self, course=course) == None:
            LecturerCourse(person=self, course=course).save()
            print('Курс добавлен')
            return 'Курс добавлен'
        else:
            print('За указанным лектором уже закреплен указанный курс')
            return 'Ошибка'

    def __str__(self):
        return (f'\nЛектор: {self.person.name} {self.person.surname}' + '\nЗакрепленные курсы: ' +
                ', '.join(course.course for course in self.person.lecturer_courses) +
                '\nСредний бал за лекции: ' + str(self.average_grade(self.person)))

    def __lt__(self, other):
        grade_person1 = self.average_grade(self.person)
        grade_person2 = self.average_grade(other.person)
        if grade_person1 > grade_person2:
            return f'{self.person.name} {self.person.surname} успешнее {other.person.name} {other.person.surname}.'
        elif grade_person1 == grade_person2:
            return f'{self.person.name} {self.person.surname} = {other.person.name} {other.person.surname}.'
        else:
            return f'{other.person.name} {other.person.surname} успешнее {self.person.name} {self.person.surname}.'


class WorkReviewer(WorkPerson):
    def __init__(self, person_id):
        self.person = Reviewer.get(Reviewer.id == person_id)

    def rate_grade_student(self, student_id, course, grade):
        student = Student.get_or_none(Student.id == student_id)
        if student == None:
            print('Студента нет в базе.')
            return 'Ошибка'

        course_student = CourseProgressStudent.get_or_none(
            CourseProgressStudent.person_id == student_id, CourseProgressStudent.course == course)
        if course_student == None:
            print('Студент не проходит указанный курс.')
            return 'Ошибка'

        course_reviewer = ReviewerCourse.get_or_none(
            ReviewerCourse.person_id == self, ReviewerCourse.course == course)
        if course_reviewer == None:
            print('Вы не закреплены за указаннным курсом.')
            return 'Ошибка'

        GradeStudent(person=student, course=course, grade=grade).save()


    def add_course(self, course):
        if ReviewerCourse.get_or_none(person=self, course=course) == None:
            ReviewerCourse(person=self, course=course).save()
            print('Курс добавлен')
            return 'Курс добавлен'
        else:
            print('За указанным практиком уже закреплен указанный курс')
            return 'Ошибка'

    def __str__(self):
        return (f'\nПрактик: {self.person.name} {self.person.surname}' +
                '\nЗакрепленные курсы: ' + ', '.join(course.course for course in self.person.reviewer_courses))


print(WorkStudent(1))
print(WorkLecturer(1))
# WorkStudent.rate_grade_lecturer(1, 1, 'Python', 8)
WorkReviewer.rate_grade_student(2, 1, 'Python', 8)
WorkStudent.add_course_progress(2, 'Git')
print(WorkStudent(2))

WorkLecturer.add_course(1, 'JS')
# print(WorkStudent(1) > WorkStudent(2))
