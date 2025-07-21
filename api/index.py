import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, render_template
import joblib
import pandas as pd

# --- Create absolute paths for files ---
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
model_path = os.path.join(basedir, 'model.joblib')
template_dir = os.path.join(basedir, 'templates')
static_dir = os.path.join(basedir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

model = joblib.load(model_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = 'Predicted Salary'
    form_data_dict = {}

    if request.method == 'POST':
        try:
            form_data_dict = request.form.to_dict()
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
            full_model_input = model_input_data.copy()
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
            final_expected_columns = model.named_steps['preprocessor'].transformers_[0][2] + model.named_steps['preprocessor'].transformers_[1][2]
            input_df = input_df[final_expected_columns]
            predicted_salary_lakhs = model.predict(input_df)[0]
            prediction_text = f'₹ {predicted_salary_lakhs:,.2f} Lakhs per year'
        except Exception as e:
            print(f"An error occurred: {e}")
            prediction_text = 'Error: Please check input fields.'
    return render_template('index.html', prediction_text=prediction_text, form_data=form_data_dict)

# Vercel will use this file as the entrypoint, so no need for __main__ block. 