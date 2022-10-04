# Homework OOP

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __average_rating(self):
        return round(sum([x for y in self.grades.values() for x in y]) / sum(len(x) for x in self.grades.values()), 2)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname} \
                \nСредняя оценка за домашние задания: {self.__average_rating()}' +
                '\nКурсы в процессе обучения: ' + ', '.join(self.courses_in_progress) +
                '\nЗавершенные курсы: ' + ', '.join(self.finished_courses))

    def __lt__(self, other):
        if self.__average_rating() < other.__average_rating():
            return True
        else:
            return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_rating(self):
        return round(sum([x for y in self.grades.values() for x in y]) / sum(len(x) for x in self.grades.values()), 2)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_rating()}'

    def __lt__(self, other):
        if self.__average_rating() < other.__average_rating():
            return True
        else:
            return False


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка') 

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def average_rating(persons, course):
    average_rating = []
    for person in persons:
        if course in person.grades:
            average_rating += person.grades[course]
    return sum(average_rating) / len(average_rating)
    



student1 = Student('Oleg', 'Mongol', 'obscure')
student2 = Student('Nikola', 'Monson', 'men')
lecturer1 = Lecturer('Ivan', 'Ivanov')
lecturer2 = Lecturer('Demis', 'Karenovich')
reviewer1 = Reviewer('Natan', 'Petrosyan')
reviewer2 = Reviewer('Pisos', 'Ogoldelov')

students = [student1, student2]
lecturers = [lecturer1, lecturer2]


student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['JS']
student2.courses_in_progress += ['Python', 'JS']
student2.finished_courses += ['MaxPatrol']

lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['JS', 'Python']

reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['JS', 'Python']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'JS', 7)
reviewer1.rate_hw(student2, 'Python', 4)

student1.rate_hw(lecturer2, 'Python', 8)
student2.rate_hw(lecturer2, 'JS', 5)
student2.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer1, 'Git', 6)

for person in students + lecturers:
    print(person)

print(student1 > student2)
print(lecturer1 < lecturer2)

print(average_rating(students, 'Python'))


