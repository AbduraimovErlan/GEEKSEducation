""" класс - Человек """

class Person:
    def ___init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    """ information about human """
    def __str__(self, introduce_myself):
        return f"Person name is {self.fullname}, his/her - {self.age}, Family status - {self.is_married}"

""" подкласс студент """
class Student(Person):
    def __init__(self, fullname, age, is_married, marks={}):
        super().__init__(fullname, age, is_married)
        self.marks = marks
    """ средняя оценка """
    def average_marks(self):
        self.average_marks = round(sum(self.marks.values())/len(self.marks.values()), 1)
        return self.average_marks
    """ information about students """
    def __str__(self, introduce_myself):
        return f"Person name is {self.fullname}, his/her age - {self.age}, Family status - {self.is_married}, " \
            f"Lessons - Marks: {self.marks}"

""" подкласс учитель """
class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, experience=0):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        """ information about teacher """
    def __str__(self, introduce_myself):
        return f"Person name is {self.fullname}, his/her age - {self.age}, Family status - {self.is_married}, " \
            f"Exp: {self.experience} years, Salary - {Teacher.salary} som"
    """ method for count of salary """
    def per_salary(self):
        exp = self.experience
        while exp != 0 and exp != 1 and exp !=2:
            exp -= 3
            Teacher.salary = round((Teacher.salary * 0.05) + Teacher.salary, 1)

""" list of students """
def create_students(first_student, second_student, third_student):
    list_of_stu = []
    list_of_stu.append(first_student)
    list_of_stu.append(second_student)
    list_of_stu.append(third_student)
    return list_of_stu

""" Данные студента """
info = create_students(Student('Кубаныч', '17', 'холост', {'Math': 3, 'Bio': 5, "English": 4}),
                                Student('Михаил', '15', 'холост', {'Math': 4, 'Bio': 4, 'English': 4}),
                                Student('Петр', '16', 'холост', {'Math': 4, 'Bio': 4, 'English': 4}))
for obj in info:
    print(obj.__str__(introduce_myself=''))

""" Данные учителя """

alex = Teacher('Алексей', '32', 'женат', 11)
print(alex.per_salary())
print(alex.__str__(introduce_myself=''))





class Figure:
    unit = 'sm'
    def __init__(self):
        self.__peremetr = 0

    @property
    def peremetr(self):
        return self.__peremetr

    @peremetr.setter
    def peremetr(self, value):
        self.__peremetr = value


    def caculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length
        self.__peremetr = self.calculate_perimeter()

    def calculate_perimeter(self):
        return 4 * self.__side_length

    def caculate_area(self):
        return self.__side_length ** 2


    def info(self):
        return f'Square side length: {self.__side_length} {Figure.unit}, '\
               f'perimeter: {self.__peremetr} {Figure.unit}, '\
               f'area: {self.caculate_area()} {Figure.unit}. '


class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__width = width
        self.__length = length
        self.__peremetr = self.calculate_perimeter()


    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def caculate_area(self):
        return self.__width * self.__length

    def info(self):
        return f'Rectangle length: {self.__length} {Figure.unit}, '\
               f'width: {self.__width} {Figure.unit}, '\
               f'perimetr: {self.__peremetr} {Figure.unit}, '\
               f'area: {self.caculate_area()} {Figure.unit}'


figure_list = [Square(3), Square(9), Rectangle(12, 5), Rectangle(6, 7), Rectangle(2, 4)]
for i in figure_list:
    print(i.info())
