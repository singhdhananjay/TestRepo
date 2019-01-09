import random, sys, os, math, json
from Person import Person

try:
  print("Try")
  raise Exception("Error has occure")
except Exception as error:
  print("error")
else:
  print("what the heck is this")
finally:
  print("lol")