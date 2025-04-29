import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#Lendo o arquivo e trasnformando o mesmo em um dataframe 
df_startups = pd.read_csv("c:\\Users\\Dell\\OneDrive\\Desktop\\Portfolio Python\\archive (6)\\unicorns till sep 2022.csv")

#Visualiza a primeiras 5 linhas do dataframe
print(df_startups.head())