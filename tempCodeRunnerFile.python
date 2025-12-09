# ======================================
# INTELLIGENT DATA CLEANING FRAMEWORK
# VS CODE / LOCAL SYSTEM VERSION
# ======================================

# STEP 1: IMPORT REQUIRED LIBRARIES
import pandas as pd
import numpy as np
import re
from rapidfuzz import fuzz, process
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# ======================================
# READ DATASET (TAB SEPARATED FILE)
# ======================================
file_path = "C:/Users/vivek/Downloads/marketing_campaign.csv"   # keep file in same folder

print("📂 Loading dataset...")
df = pd.read_csv(file_path, sep='\t')
print("✅ Dataset Loaded Successfully!\n")

print(df.head())


# ======================================
# 🔹 DATA QUALITY SUMMARY
# ======================================
def data_quality_summary(df):
    summary = pd.DataFrame({
        "Data Type": df.dtypes,
        "Missing Values": df.isnull().sum(),
        "Missing %": df.isnull().mean() * 100,
        "Unique Values": df.nunique()
    })
    return summary


# ======================================
# 🔹 REGEX CLEANING FOR TEXT COLUMNS
# ======================================
def regex_corrections(df):
    df = df.copy()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)
        df[col] = df[col].apply(lambda x: re.sub(r'\s+', ' ', x).strip())
        df[col] = df[col].str.lower()
    return df


# ======================================
# 🔹 OUTLIER DETECTION (IQR + Isolation Forest)
# ======================================
def detect_outliers(df):
    df = df.copy()

    # Convert numeric-looking strings
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

    num_cols = df.select_dtypes(include=[np.number]).columns

    outlier_mask = pd.Series(False, index=df.index)

    # IQR-based outlier detection
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outlier_mask |= (df[col] < lower) | (df[col] > upper)

    # Isolation Forest
    try:
        scaler = StandardScaler()
        X = scaler.fit_transform(df[num_cols].fillna(0))
        model = IsolationForest(contamination=0.02, random_state=42)
        iso_pred = model.fit_predict(X)
        outlier_mask |= (iso_pred == -1)
    except:
        print("⚠ Isolation Forest skipped due to numeric issues.")

    df["_is_outlier"] = outlier_mask
    return df


# ======================================
# 🔹 FUZZY MATCHING (Only if name column exists)
# ======================================
def fuzzy_deduplication(df, column, threshold=90):
    df = df.copy()
    values = df[column].astype(str).tolist()
    map_values = {}

    for val in values:
        match = process.extractOne(val, values, scorer=fuzz.token_sort_ratio)
        if match and match[1] >= threshold:
            map_values[val] = match[0]
        else:
            map_values[val] = val

    df[column + "_fuzzy"] = df[column].map(map_values)
    return df


# ======================================
# 🔹 MISSING VALUE IMPUTATION
# ======================================
def impute_missing_values(df):
    df = df.copy()

    num_cols = df.select_dtypes(include=[np.number]).columns
    cat_cols = df.select_dtypes(exclude=[np.number]).columns

    if len(num_cols) > 0:
        df[num_cols] = SimpleImputer(strategy='median').fit_transform(df[num_cols])

    if len(cat_cols) > 0:
        df[cat_cols] = SimpleImputer(strategy='most_frequent').fit_transform(df[cat_cols])

    return df


# ======================================
# 🔹 FULL CLEANING PIPELINE
# ======================================
def full_cleaning_pipeline(df):

    print("\n🔍 DATA QUALITY BEFORE CLEANING\n")
    print(data_quality_summary(df))

    df = regex_corrections(df)
    df = detect_outliers(df)

    # If dataset contains names
    if "Customer_Name" in df.columns:
        df = fuzzy_deduplication(df, "Customer_Name")

    df = impute_missing_values(df)

    print("\n✨ DATA QUALITY AFTER CLEANING\n")
    print(data_quality_summary(df))

    return df


# ======================================
# RUN CLEANING PIPELINE
# ======================================
cleaned_df = full_cleaning_pipeline(df)

# SAVE CLEANED FILE
cleaned_file = "cleaned_marketing_campaign.csv"
cleaned_df.to_csv(cleaned_file, index=False)

print(f"\n💾 Cleaned file saved as: {cleaned_file}")
print("🎉 Data Cleaning Completed Successfully!")
