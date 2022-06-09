from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, student_data):
        new_student = Student(student_data['name'],student_data['age'],student_data['password'],student_data['role'],student_data['school_id'])
        self.students.append(new_student)
        return self.list_students()

    def delete_student(self,student_id):
        for i,student in enumerate(self.students):
            if student.school_id == student_id:
                self.students.remove(self.students[i])
                return self.list_students()
                
    
# name, age, password, role, school_id