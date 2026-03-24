import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_csv("cleaned_customer_dataset.csv")

# Select the column which has the values
data = df["Age"]     # change column name if different

# Draw boxplot
plt.boxplot(data)

plt.title("Boxplot of Dataset")
plt.show()