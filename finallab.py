import pandas as pd
import matplotlib.pyplot as plt
import re

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("company_dataset.csv")

# Rename columns (adjust if needed)
df.columns = ['index','Company','Ratings','Review_Count','Type','Years','HQ','Employees']

# -----------------------------
# DATA CLEANING
# -----------------------------

# Extract numeric rating
df['Rating'] = df['Ratings'].astype(str).str.extract(r'(\d+\.\d+)').astype(float)

# Convert reviews (k → *1000)
def convert_reviews(x):
    x = str(x)
    match = re.search(r'(\d+\.?\d*)k', x)
    if match:
        return float(match.group(1)) * 1000
    match = re.search(r'(\d+\.?\d*)', x)
    if match:
        return float(match.group(1))
    return 0

df['Reviews'] = df['Review_Count'].apply(convert_reviews)

# Extract years (numeric)
df['Year_Num'] = df['Years'].str.extract(r'(\d+)').astype(float)

# Convert employee count (approx)
def convert_employees(x):
    x = str(x)
    if 'Lakh' in x:
        return 100000
    elif '50k' in x:
        return 50000
    elif '10k' in x:
        return 10000
    elif '1k' in x:
        return 1000
    else:
        return 0

df['Emp_Count'] = df['Employees'].apply(convert_employees)

# -----------------------------
# RANDOM SAMPLING
# -----------------------------
df10 = df.sample(n=10, random_state=42)
df_remaining = df.drop(df10.index)
df5 = df_remaining.sample(n=5, random_state=1)

# -----------------------------
# 1. Headquarters (ONLY these 10)
# -----------------------------
print("\nHeadquarters of Selected 10 Companies:\n")
print(df10[['Company', 'HQ']])

# -----------------------------
# 2. Bar Chart (Rating wise)
# -----------------------------
plt.figure()
plt.bar(df10['Company'], df10['Rating'])
plt.title("Company Rating Comparison (Random 10)")
plt.xlabel("Company")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Funnel Chart (Reviews wise)
# -----------------------------
df_sorted = df10.sort_values(by='Reviews', ascending=False)

plt.figure()
plt.barh(df_sorted['Company'], df_sorted['Reviews'])
plt.title("Funnel Chart - Reviews (Random 10)")
plt.xlabel("Reviews")
plt.ylabel("Company")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Line Chart (Employee count)
# -----------------------------
plt.figure()
plt.plot(df10['Company'], df10['Emp_Count'], marker='o')
plt.title("Employee Count Comparison (Random 10)")
plt.xlabel("Company")
plt.ylabel("Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Pie Chart (5 Company years)
# -----------------------------
plt.figure()
plt.pie(df5['Year_Num'], labels=df5['Company'], autopct='%1.1f%%')
plt.title("Company Age Distribution (Random 5)")
plt.tight_layout()
plt.show()