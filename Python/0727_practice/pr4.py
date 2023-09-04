class Person:
    number_of_people = 0
    def __init__(self, name, age): #self = s1
        self.name = name
        self.age = age
        Person.number_of_people += 1  #클래스 변수 이므로 클래스 속성 사용하기

    def __str__(self):
        return self.name
    
    @classmethod
    def getNumber(cls):
        return cls.number_of_people
    
class Professor(Person):
    # a = super()
    def __init__(self, name, age): #self = s1 #def __init__(self, name, age) ->  Person. __init__(self, name, age)
        super().__init__(name, age) # class Professor(Person): > super().__init__(name, age) (self없어도 됨)
# professor에 init 이 없으면 상위 클래스에서 찾는다.

class Student(Person):
    def __init__(self, name, age, no): #self = s1
        Person. __init__(self, name, age)
        self.no = no
        
        def __str__(self):
            return f'{self.no}_{self.name}'

s1 = Student('김씨', 29, 's1000')  #self = s1
s2 = Student('이씨', 22, 's1001')  #self =s2

p1 = Professor('박씨', 40)

print(s1, s2, p1)

print(Student.getNumber())  #student 에 number_of_people이 존재하지 않으므로 상위클래스 Person에서 가져온다.
print(s1.getNumber()) #인스턴스는 클래스에서 찾고 클래스에 없으면 상위 클래스로 올라간다. 