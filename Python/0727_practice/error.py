class UserInfo:
    def __init__(self):
        self.user_data = {}
        
    def get_user_info(self):
        while True:
            try:
                name = input('이름입력')
                age = input('나이 입력')
                self.user_data = {'name' : name, 'age' : age}
                break
            except ValueError:
                print('나이는 숫자로')
                
    def display_info(self):
        try:
            name = self.user_data['name']
            age = self.user_data['age']
            print(f'사용자정보 : \n ..{name} \n.. {age}')
        except KeyError:
            print('사용자 정보가 입력되지 않았습니다.')
        except:
            print('오류')
            
user1 = UserInfo()