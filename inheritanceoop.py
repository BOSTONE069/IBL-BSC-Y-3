# The class "Firstname" initializes an object with a name attribute and raises a value error if no
# name is specified.
class Firstname:
    def __init__(self, name):
        if not name:
            raise ValueError("No name specified")
        self.name = name

# The class `Student` takes in a name and course and returns a string stating the name is studying the
# course.
class Student(Firstname):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def __str__(self):
        return f"{self.name} is studying {self.course}"

# The class "Teacher" takes in a name and units and returns a string indicating the teacher's name and
# what they are teaching.
class Teacher(Firstname):
    def __init__(self, name, units):
        super().__init__(name)
        self.units =units

    def __str__(self):
        return f"{self.name} is is teaching {self.units}"

def main():
    student = Student("Bostone", "Information Science")
    teacher = Teacher("Ochieng", "Python Programming")
    print(student)
    print(teacher)

if __name__ == "__main__":
    main()
