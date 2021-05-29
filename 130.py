import pandas as pd
import csv
dataset1 = []
with open("data.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
header = dataset1[0]
print(header)

df = pd.read_csv(r"C:\Users\vedan\Desktop\Data Cleaning\data.csv")
print(df.shape)
del df["hyperlink"]
print(df.shape)
del df["stellar_magnitude"]
print(df.shape)
del df["planet_type"]
print(df.shape)
del df["temp_planet_mass"]
print(df.shape)
del df["temp_planet_date"]
print(df.shape)
del df["eccentricity"]
print(df.shape)
del df["pl_letter"]
print(df.shape)
del df["pl_hostname"]
print(df.shape)
del df["pl_name"]
print(df.shape)
del df["planet_type"]
print(df.shape)
