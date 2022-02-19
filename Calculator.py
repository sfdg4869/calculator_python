def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiple(x,y):
    return x * y

def divide(x,y):
    return x / y

def power(x,y):
    return x ** y

def remain(x,y):
    return x % y

Selection = input("연산을 선택하세요 -> 1. 덧셈 , 2. 뺄셈 , 3. 곱셈, 4. 나눗셈, 5. 제곱, 6. 나머지 : ")


x = int(input("숫자를 입력하세요 : "))
y = int(input("숫자를 입력하세요 : "))
if Selection == "1":
   print(x , " + ", y , " = " , plus(x,y))

if Selection == "1":
   print(x , " + ", y , " = " , plus(x,y))

if Selection == "2":
   print(x , " - ", y , " = " , minus(x,y))

if Selection == "3":
   print(x , " * ", y , " = " , multiple(x,y))

if Selection == "4":
   print(x , " / ", y , " = " , divide(x,y))

if Selection == "5":
   print(x , " ** ", y , " = " , power(x,y))

if Selection == "6":
   print(x , " % ", y , " = " , remain(x,y))




