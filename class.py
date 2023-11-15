class Parents:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def content(self):
        print(f'이름은 {self.name}이고, 나이는 {self.age}살 이다.')

user1 = Parents("윤종혁", 19)
user2 = Parents("윤종혁", 29)

print(user1.content())
print(user2.content())
#class 상속
class Parents:
    #생성자, 첫번째 인자로 self를 가짐 (인스턴스 메소드)
    def __init__(self, speed, angle, dict):
        self.dict = dict
        self.speed = speed
        self.angle = angle

    def add(self):
        print(f'모터가 {self.dict}방향으로 회전하며, {self.speed}RPM의 속도로 {self.angle}도 만큼 움직인다.')

class Child(Parents):
    def __init__(self, speed, angle, dict):
        self.dict = dict
        self.speed = speed
        self.angle = angle
    
instance = Child("right",200, 90)
instance.add()

#--------------------------------------------------------------------------------------------------------------

#정적 메소드(staticmethod)
#: 정적 메소드를 사용하면 인스턴스에 접근을 할수 가 없다.
#: 그래서 인스턴스를 사용하지 못할거면 왜 이 메소드를 사용하는지 모르겠다. (그냥 class말고 그 밖에 함수 만들어서 쓰는거랑 뭐가 다른건가...)
class StaticMethod:
    @staticmethod
    def content(이름, 나이):
        print(f'저의 이름은 {이름}이고, 나이는 {나이}살 입니다.')

StaticMethod.content("윤종혁", 19)

#--------------------------------------------------------------------------------------------------------------

#property 메소드
# : 함수를 변수처럼 사용하고 싶을 떄 쓴다.
# 
class Property:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def Test(self):
        print("test success!")
        
instance = Property(3, 4)
instance.Test

#----------------------------------------------------------

from contextlib import contextmanager
import time

@contextmanager
def test():
    start_time = time.time()
    yield
    finish_time = time.time()
    print(f"시간 {finish_time - start_time}만큼 경과!")

with test():
    time.sleep(1)


#==-------------------------------------------------
# super() 사용하기
# static 클래스 변수나 함수를 다른 클래스에 사용할 수 있도록 할 수 있음
class Person:
    def __init__(self):
        self.name = "yun"

    def content(self):
        print(f'my name is {self.name}')

class Child(Person):
    def __init__(self):
        super().__init__()

    def content2(self):
        super().content()
        print(f'내 이름은 {self.name}')
        
a = Person()
b = Child()

a.content()
b.content2()

#----------------------------------------------
# try 사용
try:
    x = int(input())
    y = 10/x
    print(y)
except:
    print("error")

import time

it = [1,2,3].__iter__()

print(it.__next__())
time.sleep(1)
print(it.__next__())
time.sleep(1)
print(it.__next__())
time.sleep(1)


#----------------------------------------------

class Parents:
    def a(self):
        self.name = "yun"

    def b(self):
        self.a()  # 부모 클래스의 메서드 호출
        print(self.name)

test = Parents()
test.b()  # "yun"을 출력합니다.