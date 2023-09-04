person = {
    'name' : 'Alice',
    'age' : '25'
}

# print(my_dict['name'])
# print(my_dict.get('name'))

# #찾고자하는 키가 없을 때
# print(my_dict['age']) #keyError
# print(my_dict.get('age')) #None, error 가 아닌 none값을 반환 받았기 때문에 코드 진행 가능
# print(my_dict.get('age', 'Unknown')) #찾는값이 없으면 unknown 반환

print(person.keys())
for key in person.keys():
    print(key)

print(person.values())
for value in person.values():
    print(value)

print(person.items())
for key,value in person.items():
    print(key, value)

print(person.pop('age'))
# print(person.pop('coy'))
print(person.pop('coy', 'coyx'))