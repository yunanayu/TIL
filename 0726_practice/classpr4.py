# class Student():
#     pass
# s1 = Student()
# s1.name = '홍길동'
# print(s1.name) 
# #문법적으론 허용되지만 좋은 코드는 아님


# Student.name = '클래스이름'
# print(s1.name)
# print(Student.name)

class Student():
    sheet = []
    
    def __init__(self, name, age):    
        self.name = name
        self.age = age
        print('호출')
        print('2',self)
        
    def __str__(self):
        return self.name
    
    def __lt__(self, other):
        return self.age < other.age
    
    
    def __len__(self):
        return self.age    
        
    def attendant(self, date):
        print(f'{self.name} {date}에 출석')
        Student.sheet.append((self.name, date))
    
    @classmethod
    def getSheet(cls):
        return cls.sheet  #Student.sheet로 써도 되지만 cls.sheet 사용하기
    
s1 = Student('김씨', 20)

s2 = Student('박씨', 22)
print('1', s1)
print(s1.name, s2.name)
s1.attendant("2023-07-26")
print(Student.sheet)
s2.attendant("2023-07-26")
print(Student.sheet)
print(Student.getSheet())

print(s1)

print(s1<s2)

print(len(s1))