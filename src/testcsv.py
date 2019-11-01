#import pandas as pd
#import numpy as nm
import unittest



"""
df = pd.read_csv("uadd.csv")

print (df)

    df = pd.head()

    print(df)
    
    
    
    """
"""
with open('uadd.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)


    """


""""    def add_csv(self):
        for var in range(len(your_list)):
            for i in range(0, 1):
                a = your_list[var][0]
                b = your_list[var][1]
                c = your_list[var][2]
                test_addition2(self,a,b,c)
                """

import csv
with open('uadd.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)




  for var in range(len(your_list)):
      for i in range(0,1):
             a=your_list[var][0]
             b=your_list[var][1]
             c=your_list[var][2]

             print(a,b,c)










"""
y= your_list[2][1]
print(y)

x=len(your_list)
print(x)
"""










""""
j=len(your_list)

for i in xrange(j):
    print(i)
df = pd.read_csv('uadd.csv', delimiter=',')

# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
dicts = df.to_dict().values()

print(dicts)
"""


def read_csv(self):
    self.result = math.sqrt(a)
    self.result = 0

    with open('Unit Test Subtraction.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        your_list = list(reader)

        for var in range(len(your_list)):
            a[var] = int(your_list[var][0])
            b[var] = int(your_list[var][1])
            c[var] = int(your_list[var][2]

    return self.result



 def test_read_csv_sub(self):
        with open('Unit Test Subtraction.csv', 'r') as f:
            next(f)
            reader = csv.reader(f)
            your_list = list(reader)

            for var in range(len(your_list)):
                a = int(your_list[var][0])
                b = int(your_list[var][1])
                c = int(your_list[var][2])

                c= -1 * c
                # print(c)
                self.calculator.__sub__(a, b)
                # print(x)
                # print(self.calculator.result)
                self.assertEqual(self.calculator.result, c)
                # print(a,b,c)
