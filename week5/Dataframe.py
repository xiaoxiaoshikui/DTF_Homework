

# import the packages
import numpy as np
import pandas as pd


# create a non-empty dataframe with 1e06 rows and 5 columns
df = np.random.randint(0, 100, (1000000, 5))
df = pd.DataFrame(df)
print(df.shape)
print(df.head(5))

df[:, 0] = df[:, 1]
print(df.head(5))

