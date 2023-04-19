class SchoolMember:
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан Человек: {0})'.format(self.name))
        
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ") # and - новая строка после вызова print

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print('(Создан Учитель: {0})'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary)) # int: {0:d}

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Студент: {0})'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))         
        
t = Teacher('Mrs. Иванова', 40, 30000)
s = Student('Swaroop', 25, 75)

print() # Печатает пустую строку

members = [t, s]  # подклассы, от куда вызывается метод tell
for member in members:
    member.tell() # работает как для преподдавателя, так и для студента

    
    
