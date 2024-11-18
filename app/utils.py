import pandas as pd

def read_csv(file):
    return pd.read_csv(file)

def write_csv(data, filename="output.csv"):
    data.to_csv(filename, index=False)
