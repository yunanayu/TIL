# 클래스 정의
class person:
    #속성(변수)  #클래스변수 - 클래스 내부에 선언된 변수, 클래스로 생성 된 모든 인스턴스들이 공유하는 변수
    blood_color = 'red'
    
    
    #메서드  인스턴스 만들기 위해 생성자(name)가 있어야함// 개발자가 직접호출 x
    
    def __init__(self, name) -> None:
        self.name = name    #self는 인스턴스 변수 . 인스턴스 마다 독립적인 값을 갖고 인스턴스 생성될 때 마다 초기화 됨
        
    def singing (self): #인스턴스가 호출하는 메섣, 
        return f'{self.name} 가 노래합니다.'
    
    # 인스턴스 생성 name
    #인스턴스 생성 주소가 둘 다 다르기 때문에 name에 각각 저장 가능(공유하지 않음). 클래스와 인스턴스 모두 다른 공간에///공유하는것은 blood_color 뿐임.
singer1 = person('iu')
singer2 = person('BTS')    
print(singer1.singing())

#메서드 호출
print(singer1.singing())
print(singer2.singing())
#인스턴스가 가지고 있는 변수들이 독립적


#속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)