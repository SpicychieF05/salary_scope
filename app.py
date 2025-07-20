# api/index.py
# This version is adapted for the final UI layout.

from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')

# --- Load the Trained Model ---
model_path = os.path.join(os.path.dirname(__file__), '..', 'model.joblib')

try:
    model = joblib.load(model_path)
    print("Regression model loaded successfully.")
except FileNotFoundError:
    print("Error: 'model.joblib' not found.")
    model = None

# --- Define Application Routes ---


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = 'Predicted Salary'
    form_data_dict = {}  # Dictionary to hold the form data

    if request.method == 'POST':
        if model is None:
            prediction_text = 'Error: Model not loaded.'
            return render_template('index.html', prediction_text=prediction_text, form_data=form_data_dict)

        try:
            # --- Get Data From the Form and store it for re-rendering ---
            form_data_dict = request.form.to_dict()

            # Create a dictionary for the model input
            model_input_data = {
                'age': [int(form_data_dict['age'])],
                'gender': [form_data_dict['gender']],
                'marital_status': [form_data_dict['marital_status']],
                'job_title': [form_data_dict['job_title']],
                'years_of_experience': [int(form_data_dict['years_of_experience'])],
                'education': [form_data_dict['education']],
                'education_num': [int(form_data_dict['education_num'])],
                'hours_per_week': [int(form_data_dict['hours_per_week'])],
                'city': [form_data_dict['city']],
                'job_location': [form_data_dict['job_location']],
                'nationality': [form_data_dict['nationality']]
            }

            # --- Create a DataFrame for Prediction ---
            # Define all columns the model was trained on
            expected_columns = [
                'age', 'gender', 'education', 'job_title', 'job_location',
                'city', 'nationality', 'marital_status', 'years_of_experience',
                'education_num', 'hours_per_week'
            ]

            # Add any missing columns from the dataset that are not in the form
            # For example, 'workclass', 'relationship', 'race', etc.
            # This ensures the model gets all the features it was trained on.
            full_model_input = model_input_data.copy()

            # These are columns the model expects but are not in the simplified UI.
            # We provide default values for them.
            if 'workclass' not in full_model_input:
                full_model_input['workclass'] = ['Private']
            if 'relationship' not in full_model_input:
                full_model_input['relationship'] = ['Not-in-family']
            if 'race' not in full_model_input:
                full_model_input['race'] = ['Other']
            if 'capital_gain' not in full_model_input:
                full_model_input['capital_gain'] = [0]
            if 'capital_loss' not in full_model_input:
                full_model_input['capital_loss'] = [0]

            input_df = pd.DataFrame(full_model_input)

            # Ensure the column order is exactly what the model expects
            final_expected_columns = model.named_steps['preprocessor'].transformers_[
                0][2] + model.named_steps['preprocessor'].transformers_[1][2]
            input_df = input_df[final_expected_columns]

            print(f"Input data for prediction:\n{input_df.to_string()}")

            # --- Make Prediction ---
            predicted_salary_lakhs = model.predict(input_df)[0]

            # Format the result for display
            prediction_text = f'₹ {predicted_salary_lakhs:,.2f} Lakhs per year'
            print(f"Prediction successful: {prediction_text}")

        except Exception as e:
            print(f"An error occurred: {e}")
            prediction_text = 'Error: Please check input fields.'

    # Pass the form data back to the template to repopulate the fields
    return render_template('index.html', prediction_text=prediction_text, form_data=form_data_dict)


# --- Block to run the server locally ---
if __name__ == '__main__':
    app.run(debug=True)
