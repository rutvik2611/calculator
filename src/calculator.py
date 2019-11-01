import math
import csv
import pandas as pd


def addition(a,b):
    c = a + b
    return c

def subtraction(a,b):
    c = a - b
    return c

def multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    c = a / b
    return c

def square(a):
    c = a * a
    return c

def squareRoot(a):
    math.sqrt(a)
    return c

print("fsefefsf")

class calculator:
    result = 0


    def __init__(self):
        pass

    def __add__(self, a, b):
        self.result = addition(a, b)
        return  self.result

    def __sub__(self, a, b):
        self.result = subtraction(a, b)
        return  self.result

    def __mul__(self, a, b):
        self.result = multiplication(a, b)
        return  self.result

    def __div__(self, a, b):
        self.result = division(a, b)
        return self.result

    def __square__(self, a):
        self.result =square(a)
        return self.result

    def __squareRoot__(self, a):
        self.result = math.sqrt(a)
        return self.result

    def read_csv(self,obj):

        data = pd.read_csv(obj)
        data = data.values


<<<<<<< HEAD
    def __select__(self):
        print("""
        0.Add
        1.Sub
        2.Mul
        3.Div
        4.Squ
        5.Sqrt
        6.ReDO
        7.Exit
        
        """)
        x=input()

    def week(x):
        switcher = {
            0: __add__(a,b),
            1: __sub__(a,b),
            2: __mul__(a,b),
            3: __div__(a,b),
            4: __square__(a),
            5: __squareRoot__(a),
            6: __select__(self)
        }
        return switcher.get(i, "Invalid day of week")
=======
        return data



>>>>>>> c612f66905fbe7d2e2262d222b613a111a857daf
