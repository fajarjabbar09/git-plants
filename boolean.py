print (10 > 9)
a = 222
b = 49
if b > a:
 print("b is greater than a ")
else:
 print("a is greater than b")
print(bool("Hello"))
print(bool(44))
x = "JASMINE"
Y = "FLOWER"
print(bool(x))
print(bool(Y))
bool("abc")
bool(["apple","banana","cherry"])
class myclass():
  def __len__(self):
   return 0
myobj = myclass()
print(bool(myobj))
def myfunction():
 return True
if myfunction():
  print("yess")
else:
 print("no")
# used to determine if a function is of a certain datatype
u = 300
print(isinstance(u,int))