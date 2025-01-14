class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return False
        self.students[student_id] = Student(student_id, name, age, major)
        print("Student created successfully.")
        return True

    def read_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student)
            return student 
        else:
            print("Student not found.")
            return None

    def read_all_students(self):
        if not self.students:
            print("No students registered.")
            return []
        for student in self.students.values():
            print(student)
        return list(self.students.values())

    def update_student(self, student_id, name=None, age=None, major=None):
        student = self.students.get(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print("Student updated successfully.")
            return True
        else:
            print("Student not found.")
            return False

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
            return True
        else:
            print("Student not found.")
            return False
