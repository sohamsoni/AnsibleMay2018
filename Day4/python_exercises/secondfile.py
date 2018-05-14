
class MyClass:
  
 def __init__(self):
   print ("MyClass constructor")
   self.x = 10
   self.y = 20

 def secondFunction(self):
   print ("This is second function")
   print ( __name__ )
   print ("X = ", self.x)
   print ("Y = " + str(self.y) )

if __name__ == "__main__":
    print ("This will not be executed")
