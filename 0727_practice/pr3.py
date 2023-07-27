try:
    num = int(input('100 으로 나눌 값을 입력하세요 '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하세요')
except ZeroDivisionError:
    print('0입력x')
except:
    print('error')
    
    
try:
    num = int(input('100 으로 나눌 값을 입력하세요 '))
    print(100 / num)
except BaseException:
    print('숫자를 입력하세요')
except ZeroDivisionError:
    print('0입력x')  #zero division  이 BaseException 의 하위 클래스 이기 때문에 비활성화
except:
    print('error')