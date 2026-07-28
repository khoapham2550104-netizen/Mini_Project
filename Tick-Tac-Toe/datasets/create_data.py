import pandas as pd
from itertools import product

values = (0, 1, -1)
df  = pd.DataFrame(product(values, repeat= 9))
df.columns = [f"{i}" for i in range(9)]
df.to_csv("all_combination.csv", index= False)