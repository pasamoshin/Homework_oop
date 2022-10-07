from peewee import *

db = SqliteDatabase('db/database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    class Meta:
        db_table = 'Students'

    id = PrimaryKeyField(unique=True)
    name = CharField()
    surname = CharField()


class CourseProgressStudent(BaseModel):
    class Meta:
        db_table = 'Courses in progress'

    person = ForeignKeyField(Student, related_name='course_progress')
    course = CharField()


class FinishedCourseStudent(BaseModel):
    class Meta:
        db_table = 'Finished courses'

    person = ForeignKeyField(Student, related_name='finished_courses')
    course = CharField()


class GradeStudent(BaseModel):
    class Meta:
        db_table = 'Grades students'

    person = ForeignKeyField(Student, related_name='grade')
    course = CharField()
    grade = IntegerField()


class Reviewer(BaseModel):
    class Meta:
        db_table = 'Reviewers'

    id = PrimaryKeyField(unique=True)
    name = CharField()
    surname = CharField()


class ReviewerCourse(BaseModel):
    class Meta:
        db_table = 'Reviewers courses'

    person = ForeignKeyField(Reviewer, related_name='reviewer_courses')
    course = CharField()


class Lecturer(BaseModel):
    class Meta:
        db_table = 'Lecturers'

    id = PrimaryKeyField(unique=True)
    name = CharField()
    surname = CharField()


class LecturerCourse(BaseModel):
    class Meta:
        db_table = 'Lecturers courses'

    person = ForeignKeyField(Lecturer, related_name='lecturer_courses')
    course = CharField()


class GradeLecturer(BaseModel):
    class Meta:
        db_table = 'Grades lecturers'

    person = ForeignKeyField(Lecturer, related_name='grade')
    course = CharField()
    grade = IntegerField()


if __name__ == '__main__':
    db.create_tables([Student, CourseProgressStudent, FinishedCourseStudent,
                      GradeStudent, Reviewer, ReviewerCourse, Lecturer,
                      LecturerCourse, GradeLecturer])

    student1 = Student(name='Ivan', surname='Ivanov').save()
    CourseProgressStudent(person=student1, course='Python').save()
    FinishedCourseStudent(person=student1, course='Git').save()
    GradeStudent(person=student1, course='Python', grade=7).save()
    GradeStudent(person=student1, course='Python', grade=5).save()

    reviewer1 = Reviewer(name='Oleg', surname = 'Bystrov').save()
    ReviewerCourse(person=reviewer1, course='Python').save()

    lecturer1 = Lecturer(name='Georg', surname='Zabuzov').save()
    LecturerCourse(person=lecturer1, course='Python').save()
    GradeLecturer(person=lecturer1, course='Python', grade=9).save()


    student2 = Student(name='Alex', surname='Petrov').save()
    CourseProgressStudent(person=student2, course='Git').save()
    FinishedCourseStudent(person=student2, course='JS').save()
    GradeStudent(person=student2, course='Git', grade=10).save()
    GradeStudent(person=student2, course='Git', grade=9).save()
