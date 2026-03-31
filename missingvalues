import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Aman', 'Ravi', 'Sita', 'Jhon', 'Mira', None],
    'Age': [23, np.nan, 29, 35, np.nan, 40],
    'Salary': [50000, 60000, np.nan, 80000, 75000, np.nan],
    'City': ['Mumbai', 'Delhi', None, 'Chennai', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

print("\nMissing Values (True = Missing):\n", df.isnull())
print("\nCount of missing values:\n", df.isnull().sum())

plt.figure()
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Data Heatmap")
plt.show()

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

df['Name'] = df['Name'].fillna(df['Name'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])

print("\nAfter Filling Missing Values:\n", df)

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

print("\nMissing Values After Cleaning:\n", df.isnull().sum())

plt.figure()
plt.hist(df['Age'])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df['Age'], df['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

plt.figure()
sns.countplot(x='City', data=df)
plt.title("City Distribution")
plt.show()
