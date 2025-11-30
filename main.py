import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import missingno as msno

heart_failure_list = []

df = pd.read_csv("csv/heart.csv")

new_columns = ["age", "sex", "cp", "trtbps", "chol", "fbs", "rest_ecg", "thalach", "exang", "old_peak", "slope", "ca", "thal", "target"]

df.columns = new_columns

# df.head() to return first 5 rows
# df.shape to get dimensions of dataset (rows, columns)
# df.info() to get a summary of the dataset comes useful to null values or data types
# df.isnull().sum() checks if there are any missing values
# df.describe() returns description of the data in the DataFrame
"""
    count - The number of not-empty values.
    mean - The average (mean) value.
    std - The standard deviation.
    min - the minimum value.
    25% - The 25% percentile*.
    50% - The 50% percentile*.
    75% - The 75% percentile*.
    max - the maximum value.
"""

# checks for null values
isnull_number = []
for i in df.columns:
    x = df[i].isnull().sum()
    isnull_number.append(x)

is_missing_df = pd.DataFrame(isnull_number, index = df.columns, columns = ["Total Missing Values"])
# msno.bar(df, color="b")
# plt.show()

# checks for unique values
is_unique_list = []
for i in df.columns:
    x = df[i].value_counts().count()
    is_unique_list.append(x)

is_unique_df = pd.DataFrame(is_unique_list, index = df.columns, columns = ["Total Unique Values"])

# Numeric:
# Categoric: 

numeric_var = ["age", "trtbps", "chol", "thalach", "old_peak"]
categoric_var = ["sex", "cp", "fbs", "rest_ecg", "exang", "slope", "ca", "thal", "target"]

"""
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="age", linewidth=1, edgecolor="k", alpha=0.7)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="trtbps", linewidth=1, edgecolor="k", bins=20)

sns.displot(data=df, x="chol", kind='kde')

sns.displot(data=df, x="thalach", kind='kde')
plt.show()
"""
numeric_axis_name = ["Age of the Patient", "Resting Blood Pressure", "Cholesterol", "ST Depression"]
title_font = {"family": "arial", "color": "darkred", "weight": "bold", "size": 15}
axis_font = {"family": "arial", "color": "darkblue", "weight": "bold", "size": 13}

for i, z in list(zip(numeric_var, numeric_axis_name)):
    plt.figure(figsize=(8,6), dpi=80)
    
    # Replace distplot with histplot
    sns.histplot(df[i], kde=True, linewidth=1, edgecolor="k", bins=20)
    
    plt.title(i, fontdict=title_font)
    plt.xlabel(z, fontdict=axis_font)
    plt.ylabel("Density", fontdict=axis_font)
    
    plt.tight_layout()
    plt.show()