#!/usr/bin/python

def F1():
  print("F1() with zero arguments")

def F2(x):
  print("F2() with one argument")
  print ( type( x ) )
  x = "Hello"
  print ( type( x ) )
  x = 1.99
  print ( type( x ) )

F1()
F2(100)
