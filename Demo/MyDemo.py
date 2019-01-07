import random, sys, os, math, json
from Person import Person

try:
  print("Try")
  raise Exception("Error has occure")
except Exception as error:
  pass
else:
  print("what the heck is this")