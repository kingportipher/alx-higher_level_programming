#!/usr/bin/python3

def magic_calculation(a, b):
   """Replicates the behavior of the provided Python bytecode."""

   result = 0
   for i in range(1, 3):
       try:
           if i > a:
               raise Exception("Too far")
           result += b
       except Exception:
           pass
   return result
