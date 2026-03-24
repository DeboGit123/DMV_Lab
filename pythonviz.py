import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_dataset_no_membership.csv")

# Count missing
missing_count = df.isnull().sum().sum()
print("Total missing values:", missing_count)

# ---- MANUAL FILL ----
for col in df.columns:
    if df[col].isnull().sum() > 0:
        print(f"\nColumn '{col}' has {df[col].isnull().sum()} missing values")
        user_value = input(f"Enter value to fill missing in '{col}': ")
        
        try:
            user_value = float(user_value)
        except:
            pass
        
        df[col] = df[col].fillna(user_value)

# Save cleaned dataset
df.to_csv("cleaned_customer_dataset.csv", index=False)

print("\nMissing values filled!")
print("Remaining missing values:", df.isnull().sum().sum())

# ---- VISUALIZATION FUNCTION ----
def visualize_data(df):
    print("\nChoose visualization type:")
    print("1 → Bar Chart")
    print("2 → Pie Chart")
    print("3 → Stair Chart")

    choice = input("Enter your choice (1/2/3): ")
    col = input("Enter column name to visualize: ")

    if col not in df.columns:
        print("Invalid column!")
        return

    data = df[col].value_counts()

    if choice == "1":
        data.plot(kind='bar')
        plt.title(f"Bar Chart of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.show()

    elif choice == "2":
        data.plot(kind='pie', autopct='%1.1f%%')
        plt.title(f"Pie Chart of {col}")
        plt.ylabel("")
        plt.show()

    elif choice == "3":
        plt.step(range(len(data)), data.values)
        plt.title(f"Stair Chart of {col}")
        plt.xlabel("Index")
        plt.ylabel("Count")
        plt.show()

    else:
        print("Invalid choice!")

# ---- CALL ON CLEANED DATA ----
visualize_data(df)