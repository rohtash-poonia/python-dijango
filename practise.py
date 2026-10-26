
# if else problem practise
a = 200
b = 33
if b > a : print("b is greater than a")
else: print("a is grater than b")  #this is the output

# second question
x = "Hello" #true
y = 15 #true

print(bool(x)) #true
print(bool(y)) #true
print(bool(["apple", "cherry", "banana"])) #true
print(bool(False)) #false
print(bool(None)) #false
print(bool(0)) #false
print(bool("")) #false
print(bool(())) #false
print(bool([])) #false
print(bool({})) #false

# third question
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #false
# One more value, or object in this case, evaluates to False,class with a __len__ function that returns 0 or False


#forth question
x = 200
print(isinstance(x, int)) #True

# artematic oprators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y) # 4 ki power 15 means 4*4 15 times
print(x // y)  # remove the point deciaml value

# Assignment Operators
x = 10
x += 5  
print(x) 
#output will be 15

#terniary operator
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

# comparison operator
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# logical operator

# first question
x = 5
print(not(x > 3 and x < 10))

# second question
x = 5
print(x < 5 or x > 10)

# identity operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# membership operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)



# bitwise operators
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010


# & for both true 
# | for only one true
print(6 & 3)
print(6 | 3)

# Operator Precedence
print(100 + 5 * 3) #115

