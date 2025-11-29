import numpy as np # linear algebra
import pandas as pd # data processing, CS
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

heart_failure_list = []

df = pd.read_csv("csv/heart.csv")

print(df.head())
