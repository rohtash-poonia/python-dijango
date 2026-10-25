
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