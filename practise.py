
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



# list in pyton like array in javascript
# first prctise
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
print(list1[0]) #apple
print(list1[1]) #banana
print(list1[2]) #cherry
print (len(list1)) #3

# second question
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) #['apple', 'banana', 'cherry']
# agar aapne list(("e",2)) to ye ek array or list bana ke dega

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']
print(thislist[2:]) #['cherry', 'orange', 'kiwi',
# 2 to 5 index print kar dega and 4 index se pehle ke index print kar dega and 2 index se aage ke index print kar dega

#third quesstion to change the list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist) #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango'] esmai 1 se 3 index ke beech ke items ko replace kar diya hai



# Add list items

# first question
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry'] 2 index pe watermelon add kar diya hai
# insert list mai insert karne ke liye use hota hai

# second question
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange'] append list mai add karne ke liye use hota hai 

# third question
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya'] extend list mai add karne ke liye use hota hai

#remove list items
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry', 'banana', 'kiwi'] remove list mai remove karne ke liye use hota hai

# second question
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry'] pop list mai remove karne ke liye use hota hai pop mai index number dena padta hai aur wo index number ke item ko remove kar deta hai agr index number nahi diya to last item ko remove kar deta hai


# third question
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[] clear list mai remove karne ke liye use hota hai clear list ko empty kar deta hai


# loop lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #apple banana cherry 