import numpy as np
import pandas as pd

s1 = pd.Series([1,2,3,4,5], index=["a","b","c","d","e"])
s2 = pd.Series([10,20,30,40,50], index=["a1","b1","c1","d1","e1"])

# Corrected dictionary creation using curly braces
dic = {"Series1": s1, "Series2": s2}

s1 = pd.Series([1,2,3,4,5],index)
print(s1)

# data frame to create 2-d tables 
student = {"marks":[1,2,3,34,45],"Sports":["Hockey","Golf","cricket"]}
