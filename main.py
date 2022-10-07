from models import *


def average_grade(person):
    grades = 0
    for grade in person.grade:
        grades += grade.grade

    try:
        res = str(round(grades/person.grade.count(), 2))
    except ZeroDivisionError:
        res = ' -'
    finally:
        return res


def out_students():
    for person in Student.select():
        print(f'{person.name} {person.surname}' + 'Курсы в процессе обучения: ' +
              ', '.join(course.course for course in person.course_progress) +
              'Завершенные курсы: ' + ', '.join(course.course for course in person.finished_courses) +
              'Средний бал за домашние задания' + average_grade(person))


def out_lecturers():
    for person in Lecturer.select():
        print(f'{person.name} {person.surname}' + 'Закрепленные курсы: ' +
              ', '.join(course.course for course in person.lecturer_courses) +
              'Средний бал за лекции' + average_grade(person))

def out_reviewers():
    for person in Reviewer.select():
        print(f'{person.name} {person.surname}' + 'Закрепленные курсы: ' +
              ', '.join(course.course for course in person.reviewer_courses))

out_students()
out_lecturers()
out_reviewers()

