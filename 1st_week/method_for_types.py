# 타입별 메서드

# 문자열 메서드
# count: 문자열 내에서 특정 문자가 몇 개나 있는 지 세는 메서드
text = "hello, sparta!"
count = text.count('a')
print(count)

# find: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드 (없을 경우 -1 return)
text = "hello, sparta!"
position = text.find('sparta')
position2 = text.find('world')
print(position)
print(position2)

# index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드 (없을 경우 ValueError)
text = "hello, sparta!"
position = text.index('sparta')
print(position)
try:
    position2 = text.index('world')
    print(position2)
except Exception as e:
    print(e)

# join: 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드
fruits = ['apple', 'banana', 'cherry']
joined_fruit = ', '.join(fruits)
print(joined_fruit)

# upper: 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드
# lower: 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드
text = "Hello, Sparta!"
uppercase_text = text.upper()
print(uppercase_text)
lowercase_text = text.lower()
print(lowercase_text)

# replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
text = "Hello, Sparta!"
replaced_text = text.replace('Hello', 'Hi')
print(replaced_text)

# split: 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환)
text = 'apple,banana,cherry'
fruits = text.split(',')
print(fruits)

# 리스트 메서드
# len: 리스트의 길이를 반환하는 내장 함수
numbers = [1, 2, 3, 4, 5]
print(len(numbers))

# del: 리스트에서 특정 요소를 삭제하는 연산자
numbers = [1, 2, 3, 4, 5]
del numbers[1]
print(numbers)

# append: 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# sort: 리스트를 오름차순으로 정렬하는 메서드
numbers = [4, 5, 2, 1, 3]
numbers.sort()
print(numbers)
numbers = [4, 5, 2, 1, 3]
numbers.sort(reverse=True)
print(numbers)

# reverse: 리스트의 요소 순서를 반대로 뒤집는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

# index: 리스트에서 특정 요소의 인덱스를 반환하는 메서드
numbers = [1, 2, 3, 4, 5]
print(numbers.index(3))

# insert: 리스트의 특정 위치에 요소를 삽입하는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.insert(3, 2)
print(numbers)

# remove: 리스트에서 특정 요소를 제거하는 메서드
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)

# pop: 리스트에서 마지막 요소를 빼닌 뒤, 그 요소를 삭제하는 메서드
numbers = [1, 2, 3, 4, 5]
number = numbers.pop()
print(numbers)
print(number)

numbers = [1, 2, 3, 4, 5]
number = numbers.pop(3)  # 인덱스 값을 받는 구나
print(numbers)
print(number)

# count: 리스트에서 특정 요소의 개수를 세는 메서드
numbers = [1, 2, 2, 3, 4, 5, 2]
print(numbers.count(2))

# extend: 리스트를 확장하여 새로운 요소를 추가하는 메서드
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)

# += 연산자를 사용해서 구현할 수도
numbers = [1, 2, 3]
numbers += [4, 5, 6]
print(numbers)

# 딕셔너리 메서드
# 딕셔너리 초기화
empty_dict = {}
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(my_dict)
my_dict = {}
print(my_dict)

# 딕셔너리 쌍 추가
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
my_dict['orange'] = 4
print(my_dict)

# del: 딕셔너리에서 특정 요소를 삭제
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
del my_dict['apple']
print(my_dict)

# 딕셔너리에서 특정 Key에 해당되는 Value를 얻는 방법(딕셔너리에 Key가 없는 경우, KeyError)
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(my_dict['apple'])
try:
    print(my_dict['grape'])
except Exception as e:
    print(e)

# keys: 딕셔너리에서 모든 Key를 리스트로 만들기
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
key_list = list(my_dict.keys())
print(key_list)

# values: 딕셔너리에서 모든 Value를 리스트로 만들기
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
value_list = list(my_dict.values())
print(value_list)

# items: 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(my_dict.items())

# clear: 딕셔너리의 모든 요소를 삭제
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
my_dict.clear()
print(my_dict)

# get: 딕셔너리에 지정한 키에 대응하는 값을 반환 (딕셔너리에 Key가 없는 경우, None 반환)
person = {'name': 'John', 'age': 30, 'gender': 'male'}
name = person.get('name')
print(name)
email = person.get('email')
print(email)
# 기본값을 설정할 수 있음
email = person.get('email', 'unknown')
print(email)

# request.POST['key’] vs request.POST.get('key')

# in: 해당 키가 딕셔너리 안에 있는 지 확인
person = {'name': 'John', 'age': 30, 'gender': 'male'}
print('name' in person)
print('email' in person)
print('John' in person)
