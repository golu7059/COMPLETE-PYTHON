import numpy as np 
import pandas as pd

data = {
  "GOLU": [90, 95, 100],
  "ISHANT": [50, 40, 45]
}

df = pd.DataFrame(data,index=(["MATHS","JAVA","PYTHON"]))

print(df)
print(df.shape)
print(df.head(2))  # by default value of head and tail is 8

