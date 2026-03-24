import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("cleaned_customer_dataset.csv")

# Select columns
age = df["Age"]
income = df["AnnualIncome"]   # change column name if different

# Create scatter plot
plt.scatter(age, income)

# Add labels and title
plt.xlabel("Age")
plt.ylabel("AnnualIncome")
plt.title("Age vs Annual Income")

# Show plot
plt.show()