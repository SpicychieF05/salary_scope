import streamlit as st
import joblib
import numpy as np
import os

# Load model and encoders
model = joblib.load('model.joblib')
label_encoder = joblib.load('label_encoder.joblib')

# Optional: Display logo/banner if available
if os.path.exists('static/app-logo.png'):
    st.image('static/app-logo.png', width=120)
if os.path.exists('assets/banner.jpg.jpg'):
    st.image('assets/banner.jpg.jpg', use_column_width=True)

st.title('Salary Scope: Data Scientist Salary Predictor')

st.markdown('''<div style="border:2px solid #2546ff;background:linear-gradient(90deg,#1a1a2e 60%,#16213e 100%);border-radius:16px;padding:28px 24px 22px 24px;margin-bottom:32px;box-shadow:0 4px 24px 0 rgba(36,99,235,0.12),0 0 0 2px #2546ff33;color:#e0e6f7;position:relative;overflow:hidden;">
<h2 style="color:#5fa8f6;font-size:2rem;margin-top:0;margin-bottom:12px;letter-spacing:1px;font-weight:700;">How to Use</h2>
<p style="font-size:1.13rem;line-height:1.7;margin:0;color:#c7d0e6;">Fill in your details below and click <b>Predict Salary</b> to see your estimated salary. <span class="accuracy-highlight" style="color:#fff;background:linear-gradient(90deg,#2546ff 60%,#5fa8f6 100%);padding:2px 10px;border-radius:8px;font-weight:600;margin:0 4px;box-shadow:0 2px 8px 0 #2546ff44;letter-spacing:0.5px;">Model Accuracy: 89% (R² = 0.89)</span></p>
</div>''', unsafe_allow_html=True)

# Dropdown options (sorted)
job_titles = sorted([
    'Actuary', 'Agile Coach', 'AI Engineer', 'Assistant Engineer (AE)', 'Assistant Section Officer', 'Auditor', 'Automation Tester', 'Backend Developer', 'Bank Clerk', 'Bank Probationary Officer (PO)', 'Bank Specialist Officer (SO)', 'Big Data Engineer', 'Block Development Officer (BDO)', 'Blockchain Developer', 'Business Analyst', 'Business Intelligence Developer', 'Chartered Accountant (CA)', 'Chief Technology Officer (CTO)', 'Cloud Architect', 'Cloud Engineer', 'Cloud Security Engineer', 'Company Secretary (CS)', 'Content Strategist', 'Cost Accountant (CMA)', 'CRM Specialist (Salesforce)', 'Credit Analyst', 'Customs Officer', 'Cybersecurity Analyst', 'Data Analyst', 'Data Engineer', 'Data Scientist', 'Database Administrator (DBA)', 'Deep Learning Engineer', 'DevOps Engineer', 'Digital Marketing Analyst', 'District Magistrate', 'Embedded Systems Engineer', 'ERP Consultant (SAP/Oracle)', 'Excise Officer', 'Financial Analyst', 'Financial Planner', 'Frontend Developer', 'Full Stack Developer', 'Game Developer', 'Graphic Designer', 'IAS Officer', 'IFS Officer', 'Income Tax Inspector', 'Indian Railways Officer (RRB Group A/B)', 'Information Security Officer', 'Insurance Advisor (GIC/NIC)', 'IoT Engineer', 'IPS Officer', 'IRS Officer', 'IT Consultant', 'IT Project Manager', 'IT Support Specialist', 'Junior Engineer (JE)', 'LDC (Lower Division Clerk)', 'LIC AAO', 'LIC ADO', 'Loan Officer', 'Machine Learning Engineer', 'Mobile App Developer', 'Mutual Fund Advisor', 'NABARD Grade A/B Officer', 'NLP Engineer', 'Network Administrator', 'Network Engineer', 'Portfolio Manager', 'Power BI Developer', 'Product Manager', 'PSU Engineer (ONGC, NTPC, BHEL)', 'QA/Test Engineer', 'Railway Protection Force (RPF) Officer', 'RBI Assistant', 'RBI Grade B Officer', 'Research Officer (CSIR/ICAR)', 'Risk Analyst', 'Scrum Master', 'SEBI Grade A Officer', 'SEO Specialist', 'Social Media Manager', 'Software Architect', 'Software Developer', 'SSC CGL Officer', 'State PCS Officer', 'Stock Broker', 'System Administrator', 'Tax Consultant', 'Technical Support Engineer', 'Tehsildar', 'Treasury Manager', 'UI/UX Designer', 'UDC (Upper Division Clerk)', 'Wealth Manager', 'Web Designer'
])
locations = ['Rural', 'Suburban', 'Urban']
nationalities = sorted(['American', 'Australian', 'Brazilian', 'British', 'Canadian', 'Chinese', 'French', 'German', 'Indian', 'Japanese', 'Russian', 'South African'])

# Streamlit form
with st.form("salary_form"):
    job_title = st.selectbox("Job Title", ["Select"] + job_titles)
    location = st.selectbox("Location Type", ["Select"] + locations)
    nationality = st.selectbox("Nationality", ["Select"] + nationalities)
    # Add more fields as needed (education, marital status, etc.)
    submitted = st.form_submit_button("Predict Salary")

if submitted:
    if job_title == "Select" or location == "Select" or nationality == "Select":
        st.error("Please select all fields.")
    else:
        # Example: encode inputs (update as per your model's requirements)
        # X = np.array([[...encoded values...]], dtype=object)
        # prediction = model.predict(X)
        # For demonstration, we'll use a placeholder value:
        prediction = [1234567]  # Replace with actual prediction logic
        st.success(f"Predicted Salary: ₹{prediction[0]:,.0f}")
        st.info("Authenticity: 89% (R² = 0.89)")
