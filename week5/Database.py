# import the packages
import pandas as pd
import numpy as np
import time
import h5py
import pyarrow.feather as feather
import pyarrow.parquet as pq
import pyarrow as pa

# dataframe
df = np.random.randint(0, 100, (1000000, 5))
df = pd.DataFrame(df)
print(df.head(5))
df.iloc[:, 0] = df.iloc[:, 1]  # copy the second column to the first column
print(df.head(5))   # testing the output

# time list
time_list = []

# HDF
start_time_h = time.time()
d_hdf = h5py.File("Data_HDF.h5", 'w')
d_hdf.create_dataset("data", data=df)
d_hdf.close()
end_time_h = time.time()
hdf_time = end_time_h-start_time_h
print(hdf_time)
time_list.append(hdf_time)

# Feather
start_time_f = time.time()
feather.write_feather(df, 'Data_feather.feather')
end_time_f = time.time()
feather_time = end_time_f - start_time_f
print(feather_time)
time_list.append(feather_time)

# Parquet
start_time_p = time.time()
table = pa.Table.from_pandas(df)
pq.write_table(table, 'Data_parquet.parquet')
end_time_p = time.time()
parquet_time = end_time_p - start_time_p
print(parquet_time)
time_list.append(parquet_time)

# write the time in the txt file
df1 = pd.DataFrame([time_list])
df1.columns = ['hdf_time', 'feather_time', 'parquet_time']
print(df1)
df1.to_csv(r'time.txt', header=True, index=None, sep='\t', mode='w')

