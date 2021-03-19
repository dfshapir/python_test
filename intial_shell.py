# Adding changes
print("Hello World!")
import numpy as ny
data1 = ny.array([1, 2, 3])
import matplotlib as mat
import matplotlib.pyplot as plt
import pandas as pd

# Testing out creation of dataframes.

dict = {
        "country":["Brazil", "Russia", "India", "China", "South Africa"],
        "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"]}

brics = pd.DataFrame(dict)
brics