from Model.StudentClass import Student
from Model.CourseClass import Course

class Database:
    def __init__(self):
        self.students = []
        self.courses = []

    def nextStudentID(self):
        return len(self.students) + 1

    def nextCourseID(self):
        return len(self.students) + 1

    def addStudent(self,name,age):
        self.students.append(Student(self.nextStudentID(),name,age))

    def addCourse(self,name,credit,instructor):
        self.courses.append(Course(self.nextCourseID(),name,credit,instructor))
