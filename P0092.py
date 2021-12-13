'''
Iterator?
반복 가능한 객체, 반복문을 이용하여 데이터를 순회하면서 처리하는 것을 의미
Generator?
Iterator를 생성해주는 함수를 의미
파이썬에서는 함수 안에 yield라는 키워드를 사용해서 만들수 있다.
여기서... 모든 값을 포함하여 변환하는 대신, 호출할 때마다 한 개의 값을 리턴한다...
즉, 호출할 때마다 리턴하기 때문에, 메모리가 충분하지 않은 상황에서도 대용량으,ㅣ 반복 가능한 구조로
순회할 수 있다는...

'''
def number_generator(n) :
    print("Generator 시작")
    while n < 6 :
        print("Yield 전 : ....Function Start")
        yield n
        n += 1
        print("Yield 후 : ....Function End")
    print("Generator 끝")
for i in number_generator(0) :
    print("for 시작 : ....")
    print("Yield 값 : ", i)
    print("for 끝  : .......")

def generator(wordList) :
    wordListLength = 0
    print("Generator Start")
    while(wordListLength < len(wordList)) :
        yield wordList[wordListLength]
        wordListLength += 1
    print("Generator End")

Main_wordList = ["Youngsan", "University","AI","Computer"]
for i in generator(Main_wordList) :
    print(i)
print("done")

'''
사용 이유 두가지...
1) Memory를 효율적으로 사용
list comprehension과 generator expression으로 각각 생성했을 때 메모리 사용 상태를 봅시다.
list의 경우 사이즈가 커질 수록 그만큼 메모리 사용량이 늘어납니다. 
generator의 경우는 사이즈가 커진다해도 차지하는 메모리 사이즈는 동일한 것을 볼 수 있습니다.
list와 generator의 동작 방식의 차이가 있을 뿐입니다.
list는 list 안에 속한 모든 데이터를 메모리에 적재하기 때문에 list의 크기 만큼 
차지하는 메모리 사이즈가 늘어나게 됩니다. 
generator의 경우 데이터 값을 한 번에 메모리에 적재하는 것이 아니라 
next() 함수를 통해 차례로 값에 접근할 때마다 메모리에 적재하는 방식입니다.
'''
import sys

a = [i for i in range(100) if i%2]
print(a)
print(sys.getsizeof(a)) #520

b = [i for i in range(1000) if i%2]
print(b)
print(sys.getsizeof(b)) #4264

c = (i for i in range(100) if i%2)
print(c)
print(sys.getsizeof(c)) #112

d = (i for i in range(1000) if i%2)
print(d)
print(sys.getsizeof(d)) #112

'''
2. Lazy evaluation 즉 계산 결과 값이 필요할 때까지 계산을 늦추는 효과가 있음
list의 경우는 list comprehension을 수행할 때, 
list의 모든 값을 먼저 수행하기 때문에 sleep_function() 함수를 range()만큼 한 번에 수행하게 됩니다.
generator의 경우 생성 시 실제 값을 로딩하지 않고, 
for문이 수행될 때 하나씩 sleep_function()을 수행하며 값을 불러오게 됩니다. 
generator의 특징 중 하나는 "수행 시간이 긴 연산을 필요한 순간까지 늦출 수 있다는 점이 특징"이라고 할 수 있습니다.
간단하게 말하면, list는 실행되고 결과 값을 list에 반환되어 [0,1,2,3,4] 값을 가지고 있게 됩니다.
그러나 generator는 실행되지 않고 object로 선언이 되기 때문에 필요한 때마다 실행시킬 수 있게 된 것입니다.

'''
import time

def sleep_function(x) :
    print("sleep")
    time.sleep(1)
    return x

list = [sleep_function(x) for x in range(5)]
generator = (sleep_function(y) for y in range(5))

for i in list :
    print(i)

print("================")
for j in generator :
    print(j)
    
