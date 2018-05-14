#!/usr/bin/python

from secondfile import MyClass;

def printFunction():
	print("Hello Python!")
        print ( __name__ )


if __name__ == "__main__":
   printFunction()
   obj = MyClass()
   obj.secondFunction()
