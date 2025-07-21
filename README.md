<!-- Banner Image -->
<p align="center">
  <img src="assets/banner.jpg.jpg" alt="Salary Scope Banner" style="width:100%;max-width:900px;border-radius:16px;box-shadow:0 4px 24px #2546ff44;">
</p>

<h1 align="center" style="color:#2546ff;font-size:2.8rem;font-weight:800;letter-spacing:2px;">Salary Scope: A Data Scientist Salary Predictor</h1>

<p align="center" style="color:#5fa8f6;font-size:1.2rem;font-weight:500;">
  <strong>Predict your salary with confidence using AI-powered insights.</strong>
</p>

<p align="center">
  <a href="https://salary-scope-spycychief.streamlit.app/" style="font-size:1.1rem;font-weight:600;color:#2546ff;">🌐 Live Demo: salary-scope-spycychief.streamlit.app</a>
</p>

---

## <span style="color:#2546ff;">✨ Features</span>
- <span style="color:#5fa8f6;">Accurate Predictions:</span> Utilizes a Gradient Boosting Regressor model with <strong style="color:#2546ff;">R² = 0.89 (89%)</strong> accuracy.
- <span style="color:#5fa8f6;">Interactive Web Interface:</span> User-friendly form to input your details and get instant salary predictions.
- <span style="color:#5fa8f6;">Data-Driven Insights:</span> Helps professionals and employers understand salary benchmarks in the industry.
- <span style="color:#5fa8f6;">Easy Deployment:</span> Optimized for Streamlit Cloud platform.

---

## <span style="color:#2546ff;">🛠️ Tech Stack & Tools</span>
- <span style="color:#5fa8f6;">Frontend & Backend:</span> Python, Streamlit
- <span style="color:#5fa8f6;">Machine Learning:</span> scikit-learn, pandas, numpy
- <span style="color:#5fa8f6;">Model:</span> Gradient Boosting Regressor
- <span style="color:#5fa8f6;">Deployment:</span> Streamlit Cloud

---

## <span style="color:#2546ff;">🚀 Getting Started (Local Development)</span>

```sh
# 1. Clone the repository
   git clone <your-repo-url>
   cd Salary-scope

# 2. Create a virtual environment
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
   pip install -r requirements.txt

# 4. Train the model (if needed)
   python train_model.py

# 5. Run the app locally
   streamlit run app_streamlit.py
```
The app will be available at [http://localhost:8501](http://localhost:8501)

---

## <span style="color:#2546ff;">☁️ Deploying on Streamlit Cloud</span>

1. <span style="color:#5fa8f6;">Push your code to GitHub.</span>
2. <span style="color:#5fa8f6;">Go to <a href="https://streamlit.io/cloud" style="color:#2546ff;">Streamlit Cloud</a> and sign in.</span>
3. <span style="color:#5fa8f6;">Click "New app" and connect your GitHub repo.</span>
4. <span style="color:#5fa8f6;">Set the main file to <code>app_streamlit.py</code>.</span>
5. <span style="color:#5fa8f6;">Deploy!</span>
   - Streamlit Cloud will build and start your app.
   - Visit your Streamlit Cloud URL to use Salary Scope.
   - <strong>Live App:</strong> <a href="https://salary-scope-spycychief.streamlit.app/">https://salary-scope-spycychief.streamlit.app/</a>

---

## <span style="color:#2546ff;">📈 Model Performance</span>

- <span style="color:#5fa8f6;">Model:</span> Gradient Boosting Regressor
- <span style="color:#5fa8f6;font-weight:bold;">Accuracy Score (R²):</span> <strong style="color:#2546ff;font-size:1.3em;">89%</strong>

---

## <span style="color:#2546ff;">📁 Project Structure</span>

```text
Salary-scope/
  app_streamlit.py
  train_model.py
  requirements.txt
  model.joblib
  label_encoder.joblib
  static/
  assets/
  README.md
  indian_salary_data_500.csv
```

---

## <span style="color:#2546ff;">🤝 Contributing</span>

Contributions are welcome! Please fork the repo and submit a pull request.

---

## <span style="color:#2546ff;">📄 License</span>

Distributed under the MIT License.
