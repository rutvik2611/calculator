import math
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


        a = []
        b = []
        c = []
        for var in range(len(data)):
            a.append(data[var][0])
            b.append(data[var][1])
            c.append(data[var][2])
        z = [a, b,c]

        return z




