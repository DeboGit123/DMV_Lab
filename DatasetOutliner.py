import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Debopriyo_DMV\customer_dataset_no_membership.csv")

missing_count = df.isnull().sum().sum()
print("Total missing values:", missing_count)

for col in df.columns:
    if df[col].isnull().sum() > 0:
        print(f"\nColumn '{col}' has {df[col].isnull().sum()} missing values")

        user_value = input(f"Enter value to fill missing in '{col}': ")

        try:
            user_value = float(user_value)
        except:
            pass

        df[col] = df[col].fillna(user_value)

df.to_excel("cleaned_customer_dataset.csv", index=False)

print("\nMissing values filled manually!")
print("Remaining missing values:", df.isnull().sum().sum())


plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
df['PreferredCategory'].value_counts().plot(kind='bar')
plt.title("Preferred Category")

# ----- PIE CHART -----
plt.subplot(1,3,2)
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")

# ----- STAIR CHART (STEP PLOT) -----
plt.subplot(1,3,3)

# Sort values for better step visualization
sorted_income = df['AnnualIncome'].sort_values().reset_index(drop=True)

plt.step(range(len(sorted_income)), sorted_income)
plt.title("Stair Chart of Annual Income")
plt.xlabel("Customer Index")
plt.ylabel("Annual Income")

plt.tight_layout()
plt.show()
