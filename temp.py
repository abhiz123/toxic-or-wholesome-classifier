import pandas as pd

#download it from kaggle and unzip each file and put in the folder named below

df = pd.read_csv("jigsaw-toxic-comment-classification-challenge/train.csv",encoding='latin-1')

del df["id"]

print(df.head())
