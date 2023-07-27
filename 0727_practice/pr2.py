class Person:
    def __init__(self,name):
        self.name = name
        
    def greeting(self):
        return f'안녕, {self.name}입니다.'


class Mom(Person):
    gene = 'XX'
    
    def __init__(self,name):
        super().__init__(name)
        
    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'
    
    def __init__(self,name, age):
        super().__init__(name)
        self.age =age
    
    def walk(self):
        return '아빠가 걷기'


class FirstChild(Mom, Dad):
    mom_gene = Dad.gene    #상속구조를 바꾸지 않고 원하는 변수를 불러오기 -> 명시적으로 작성하고 불러오면 됨.
    

    def __init__(self,name, age):
        # super().__init__(name)
        Dad.__init__(self, name, age)
    
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
baby1 = FirstChild('아기')
print(baby1.cry()) #첫째가 응애
print(baby1.swim()) #첫째가 수영
print(baby1.walk()) #아빠가 걷기 #부모클래스에서 walk 메소드를 찾음
print(baby1.gene) #XY  # FirstChild 에는 유전자 정보가 없음.Dad와 Mom 에는 있음.
# 두개가 겹쳤기 때문에 먼저 상속받은 dad class에서 정보 가져옴. -> 상속 순서의 중요성


#생성자함수 생략은 권장하지 않음. def __init__(self, name) super().__init__(name)을 사용하여 생성자 함수 꼭 넣어주기


#상속구조를 바꾸지 않고 원하는 변수를 불러오기

print(FirstChild.mro()) #속성이든 메서드이든 찾아가는 순서대로 