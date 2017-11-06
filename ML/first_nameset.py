#following the o'reilly's guide to ML
import os
os.getcwd()
import pandas as pd
from IPython.display import display

#creating a simple dataset
data = {
    'Name':['John','Jack','Dave','George'],
    'Location':["New York","London","Berlin","Dublin"],
    'Age' : [21,13,41,32]
}

data_pandas = pd.DataFrame(data)

display(data_pandas)    