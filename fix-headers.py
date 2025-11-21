# Importing libs
import pandas as pd
import os

# Getting data
df = pd.read_csv("Datasets/original-hospital-general-information.csv")
df2 = pd.read_csv("Datasets/original-hospital-readmission-program.csv")

# Used "-" to replace spaces for better readbility
# Also applied lowercase for better readability
df.columns = (
    df.columns
    .str.replace(" ", "-", regex=False)
    .str.replace("/", "-", regex=False)
    .str.lower()
)

df2.columns = (
    df2.columns
    .str.replace(" ", "-", regex=False)
    .str.replace("/", "-", regex=False)
    .str.lower()
    )

# Saves as fixed files
df.to_csv("fixed-hospital-general-information.csv", index=False)
df2.to_csv("fixed-hospital-readmission-program.csv", index=False)