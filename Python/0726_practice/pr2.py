#person정의
class Person:
    name = 'unknown'
    #인스턴스 메서드  (사용하는 주체가 인스턴스라 인스턴스 메서드)
    def talk(self):
        print(self.name)


p1 = Person()
p1.talk() #unknown
# 인스턴스 변수 없음. 본인의 인스턴스 변수가 존재하지 않으면 본인을 만든 클래스에서 변수를 찾음


# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown 
# 인스턴스 변수 없음. 본인의 인스턴스 변수가 존재하지 않으면 본인을 만든 클래스에서 변수를 찾음

p2.name = 'Kim' #p2에 인스턴스 변수가 있기때문에 클래스에서 찾아쓰지 않음.
p2.talk()  # Kim
#인스턴스는 독립적이기 때문에 p2에만 변수가 들어가고 p1에는 들어가지 앟ㄴ음
# p1 과 p2는 서로 영향을 주지 않고 독립적임.

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim


#클래스가 만든 것은 클래스가 관리
#인스턴스가 관리하는것은 본인들의 변수