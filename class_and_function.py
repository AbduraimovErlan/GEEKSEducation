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


class Figures:
    unit = 'mm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def ingo(self):
        pass

class Circle(Figures):
    pi = 'π'
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    def calculate_area(self):
        return self.__radius ** 2

    def ingo(self):
        return f'Circle radius: {self.__radius} {Figures.unit}, ' \
               f'area: {self.calculate_area()}{Circle.pi} {Figure.unit}'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def caculate_area(self):
        return round((self.__side_a * self.__side_b) / 2, 1)

    def info(self):
        return f'RightTriangle side a: {self.__side_a}{Figures.unit}, ' \
               f'side b: {self.__side_b}{Figures.unit}, ' \
               f'area: {self.caculate_area()}{Figures.unit}'


figure2_list = [Circle(4), Circle(6), RightTriangle(2, 4), RightTriangle(6, 7), RightTriangle(5, 7)]
for j in figure2_list:
    print(j.ingo())









class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value


    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


    def make_computations(self):
        return self.__memory * self.__cpu


    def __str__(self):
        return f'Оператативная память: {self.memory}, Тактовая частота: {self.cpu}'


    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory < other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory



class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list


    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value



    def call(self, sim_card_number, call_to_number):
        print(f"'Идет звонок на номер {call_to_number}' с сим-карты-{sim_card_number} - "
              f"{self.__sim_cards_list[sim_card_number-1]}")


    def __str__(self):
        return f'Список сим-кард: {self.sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)


    @staticmethod
    def use_gps(location):
        print(f"Маршрут до {location} построен!")

    def __str__(self):
        return f'Список сим-кард: {self.sim_cards_list}, ' \
               f'Оперативная память: {self.memory}, Тактовая частота: {self.cpu}'


nokia_phone = Phone(['O!', 'Beeline'])
simple_computer = Computer('5.8 GHz', 32)
simple2_computer = Computer('6 GHz', 64)
redmi_smartphone = SmartPhone('4.4 GHz', 32, ['Megafon', 'MTS'])
samsung_smartphone = SmartPhone('4.5 GHz', 68, ['MTZ', 'TeLe2'])
redmi_smartphone.call(1, '+7(812)336-42-42')
nokia_phone.call(2, '+99677701-23-60')
redmi_smartphone.use_gps('Ош базар')


print(simple2_computer > samsung_smartphone)
print(simple2_computer == simple_computer)
print(redmi_smartphone != samsung_smartphone)
print(redmi_smartphone <= samsung_smartphone)


items_list = [simple_computer, nokia_phone, redmi_smartphone, samsung_smartphone]
for items in items_list:
    print(items)