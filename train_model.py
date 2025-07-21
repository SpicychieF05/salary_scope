# train_model.py (Final UI Version)
# This script is adapted for the final UI layout and dataset.

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import sys

print("Starting model training process...")

# --- 1. Load Data ---
try:
    df = pd.read_csv('salary-dataset-5000.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'salary-dataset-5000.csv' not found.")
    sys.exit()

# --- 2. Data Preparation ---
df.columns = df.columns.str.strip()
print("Column names cleaned.")

def simplify_education(edu_string):
    s = str(edu_string).lower()
    if 'phd' in s:
        return 'PhD'
    elif any(keyword in s for keyword in ['master', 'mba', 'm.tech', 'm.com', 'm.sc', 'ca', 'cma', 'cs']):
        return 'Masters'
    elif any(keyword in s for keyword in ['bachelor', 'b.tech', 'b.com', 'b.sc', 'b.e.', 'bca', 'b.voc']):
        return 'Bachelors'
    elif '12th' in s or 'diploma' in s:
        return '12th'
    else:
        return '10th'

# Use the new education column
if 'education' in df.columns:
    df['education'] = df['education'].apply(simplify_education)

# Define columns based on the new dataset
TARGET_COL = 'salary_inr_lakhs'
CATEGORICAL_FEATURES = [
    'gender', 'education', 'job_title', 'job_location', 'city', 'nationality', 'marital_status'
]
NUMERICAL_FEATURES = [
    'age', 'years_of_experience', 'education_numeric', 'hours_per_week'
]

# Add missing columns with default values if they don't exist in the CSV
if 'marital_status' not in df.columns:
    df['marital_status'] = 'Married'
if 'education_numeric' not in df.columns:
    edu_map = {'PhD': 20, 'Masters': 18, 'Bachelors': 16, '12th': 12, '10th': 10}
    df['education_numeric'] = df['education'].map(edu_map).fillna(10)
if 'hours_per_week' not in df.columns:
    df['hours_per_week'] = 45

required_cols = CATEGORICAL_FEATURES + NUMERICAL_FEATURES + [TARGET_COL]
for col in required_cols:
    if col not in df.columns:
        print(f"FATAL ERROR: Required column '{col}' not found in the dataset!")
        sys.exit()
df = df[required_cols]

X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL]

print(f"Features for training: {X.columns.tolist()}")

# --- 3. Create a Preprocessing and Modeling Pipeline ---
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), NUMERICAL_FEATURES),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), CATEGORICAL_FEATURES)
    ],
    remainder='passthrough'
)

# Use a more powerful model and tune hyperparameters
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(
        n_estimators=400,
        max_depth=18,
        min_samples_split=3,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    ))
])

# --- 4. Train the Model with Cross-Validation ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

print("Performing cross-validation...")
cv_scores = cross_val_score(model_pipeline, X_train, y_train, cv=5, scoring='r2', n_jobs=-1)
print(f"Cross-validated R-squared (R²): {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

print("Training the regression model on full training set...")
model_pipeline.fit(X_train, y_train)
print("Model training completed.")

# --- 5. Evaluate the Model ---
y_pred = model_pipeline.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\n--- Model Evaluation ---")
print(f"Test R-squared (R²): {r2:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.2f} Lakhs")
print("------------------------\n")

# --- 6. Save the Final Pipeline ---
joblib.dump(model_pipeline, 'model.joblib')
print("Final model pipeline saved successfully as 'model.joblib'")
print("Model training process completed successfully.")
