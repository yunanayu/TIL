class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'안녕, {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        # self.name = name
        # self.age = age
        # Person.__init__(self,name,age) 
        # #유연하지 않는 코드/ 클래스 이름이 바뀔때 / 다중상속시 상위클래스를 작성한 순서대로 찾아나감. 메서드등 중복이 될 때 상속 순서를 생각해야함.
        super().__init__(name, age) #self 안적어도 됨 / 상속이 많아지고 부모 class가 많아지면 유연하게 작성이 어려워지기 때문에 super 사용
        self.department = department
        
class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        # self.name =name
        # self.age = age
        self.gpa =gpa
        
p1 = Professor('박교수', 49, '컴공')
s1 = Student('김학생', 20, 3.5)

p1.talk()
s1.talk()
