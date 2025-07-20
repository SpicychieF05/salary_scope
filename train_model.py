# train_model.py (Final UI Version)
# This script is adapted for the final UI layout and dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib
import sys

print("Starting model training process...")

# --- 1. Load Data ---
try:
    df = pd.read_csv('indian_salary_data_500.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'indian_salary_data_500.csv' not found.")
    sys.exit()

# --- 2. Data Preparation ---
df.columns = df.columns.str.strip()
print("Column names cleaned.")

# --- Simplify Education Categories to match the UI ---


def simplify_education(edu_string):
    if 'phd' in str(edu_string).lower():
        return 'PhD'
    elif any(keyword in str(edu_string).lower() for keyword in ['master', 'mba', 'm.tech', 'm.com', 'm.sc', 'ca', 'cma', 'cs']):
        return 'Masters'
    elif any(keyword in str(edu_string).lower() for keyword in ['bachelor', 'b.tech', 'b.com', 'b.sc']):
        return 'Bachelors'
    elif '12th' in str(edu_string).lower() or 'diploma' in str(edu_string).lower():
        return '12th'
    else:
        return '10th'


df['education'] = df['education'].apply(simplify_education)
print("Simplified education categories.")


# Define columns based on the final UI layout
TARGET_COL = 'salary_inr_lakhs'
CATEGORICAL_FEATURES = ['gender', 'education', 'job_title',
                        'job_location', 'city', 'nationality', 'marital_status']
NUMERICAL_FEATURES = ['age', 'years_of_experience',
                      'education_num', 'hours_per_week']

# Add missing columns with default values if they don't exist in the CSV
if 'marital_status' not in df.columns:
    df['marital_status'] = 'Married'
if 'education_num' not in df.columns:
    edu_map = {'PhD': 20, 'Masters': 18,
               'Bachelors': 16, '12th': 12, '10th': 10}
    df['education_num'] = df['education'].map(edu_map).fillna(10)
if 'hours_per_week' not in df.columns:
    df['hours_per_week'] = 45

# Select only the columns we need for the model
required_cols = CATEGORICAL_FEATURES + NUMERICAL_FEATURES + [TARGET_COL]
# Ensure all required columns exist before trying to select them
for col in required_cols:
    if col not in df.columns:
        print(
            f"FATAL ERROR: Required column '{col}' not found in the dataset!")
        sys.exit()
df = df[required_cols]

X = df.drop(columns=[TARGET_COL])
y = df[TARGET_COL]

print(f"Features for training: {X.columns.tolist()}")

# --- 3. Create a Preprocessing and Modeling Pipeline ---
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), NUMERICAL_FEATURES),
        ('cat', OneHotEncoder(handle_unknown='ignore',
         sparse_output=False), CATEGORICAL_FEATURES)
    ],
    remainder='passthrough'
)

model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(n_estimators=300,
     learning_rate=0.1, max_depth=5, random_state=42, subsample=0.8))
])

# --- 4. Train the Model ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

print("Training the regression model...")
model_pipeline.fit(X_train, y_train)
print("Model training completed.")

# --- 5. Evaluate the Model ---
print("\n--- Model Evaluation ---")
y_pred = model_pipeline.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R-squared (R²): {r2:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f} Lakhs")
print("------------------------\n")

# --- 6. Save the Final Pipeline ---
joblib.dump(model_pipeline, 'model.joblib')
print("Final model pipeline saved successfully as 'model.joblib'")
print("Model training process completed successfully.")
# End of train_model.py
