#import os

#print("Files in directory:")
#print(os.listdir("/home/ranjeet/Downloads/archive/"))
# Import necessary libraries
import pandas as pd

# Load dataset

print("Loading dataset...")
df = pd.read_csv("/home/ranjeet/Downloads/archive/marketing_campaign.csv", sep='\t')

print("Data loaded. Shape:", df.shape)

# Clean column names
print("Cleaning column names...")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Handle missing values
print("Handling missing values...")
if 'income' in df.columns:
    df['income'] = df['income'].fillna(df['income'].median())

# Remove duplicates
print("Removing duplicates...")
df = df.drop_duplicates()

# Standardize text columns
print("Standardizing text columns...")
if 'marital_status' in df.columns:
    df['marital_status'] = df['marital_status'].str.strip().str.title()

if 'education' in df.columns:
    df['education'] = df['education'].str.strip().str.title()

# Convert date column
print("Converting date columns...")
if 'dt_customer' in df.columns:
    df['dt_customer'] = pd.to_datetime(df['dt_customer'], dayfirst=True)

# Fix data types
print("Fixing data types...")
for col in ['income', 'kidhome', 'teenhome']:
    if col in df.columns:
        df[col] = df[col].astype('int64')

# Save cleaned dataset
print("Saving cleaned dataset...")
df.to_csv("customer_personality_cleaned_1.csv", index=False)

# Summary of changes
print("Generating summary of changes...")
summary = {
    "Missing Income Filled": df["income"].isnull().sum() == 0,
    "Duplicates Removed": True,
    "Text Standardized": True,
    "Date Format Fixed": True,
    "Column Names Cleaned": True,
    "Data Types Fixed": True
}

print("✅ Cleaning Complete. Summary:")
for k, v in summary.items():
    print(f"- {k}: {'Yes' if v else 'No'}")
