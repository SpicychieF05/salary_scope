<!-- Banner Image -->
<p align="center">
  <img src="assets/banner.jpg.jpg" alt="Salary Scope Banner" style="width:100%;max-width:900px;border-radius:16px;box-shadow:0 4px 24px #2546ff44;">
</p>

<h1 align="center" style="color:#2546ff;font-size:2.8rem;font-weight:800;letter-spacing:2px;">Salary Scope</h1>

<p align="center" style="color:#5fa8f6;font-size:1.2rem;font-weight:500;">
  <strong>AI-powered, mobile-optimized salary prediction app with a modern, glowing UI.</strong>
</p>

<div align="center">
  <h3>🌐 Live Demo</h3>
  <a href="https://salaryscope.streamlit.app/" style="font-size:1.1rem;font-weight:600;color:#2546ff;">
    SalaryScope.streamlit.app
  </a>
</div>

---

## ✨ Features
- **Modern, Responsive UI:** Beautiful dark theme, glowing blue accents, and perfect alignment on all devices (desktop, tablet, mobile).
- **Custom Header:** Logo, app name, and social icons (GitHub, LinkedIn, Twitter, Discord) with real links.
- **Glowing Accuracy Badge:** Eye-catching, pill-shaped badge with a checkmark and blue gradient.
- **Interactive Form:** User-friendly, grouped fields for salary prediction.
- **AI-Powered:** Uses a Gradient Boosting Regressor model with **R² = 0.96 (96%)** accuracy.
- **Easy Deployment:** Optimized for Streamlit Community Cloud.

---

## 🖼️ Screenshots

<div align="center">
  <!-- Default View -->
  <div style="margin-bottom:30px;">
    <img src="assets/default.png" alt="Default App View" style="width:100%;max-width:900px;border-radius:16px;box-shadow:0 4px 24px #2546ff44;">
    <p style="color:#5fa8f6;font-size:1.1rem;margin-top:10px;">
      Default view of the app showing the prediction form with input fields and custom styling
    </p>
  </div>

  <!-- Output View -->
  <div style="margin-bottom:30px;">
    <img src="assets/output.png" alt="Prediction Output" style="width:100%;max-width:900px;border-radius:16px;box-shadow:0 4px 24px #2546ff44;">
    <p style="color:#5fa8f6;font-size:1.1rem;margin-top:10px;">
      Results view showing the predicted salary based on user inputs with confidence score
    </p>
  </div>
</div>

---

## 🛠️ Tech Stack & Tools
- **Frontend & Backend:** Python, Streamlit
- **Machine Learning:** scikit-learn, pandas, numpy
- **Model:** Gradient Boosting Regressor
- **Deployment:** Streamlit Community Cloud

---

## 🚀 Getting Started (Local Development)

```sh
# 1. Clone the repository
   git clone <https://github.com/SpicychieF05/salary_scope>
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

## ☁️ Deploying on Streamlit Community Cloud

1. **Push your code to GitHub.**
2. **Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.**
3. **Click "New app" and connect your GitHub repo.**
4. **Set the main file to `app_streamlit.py`.**
5. **Deploy!**
   - Streamlit Cloud will build and start your app.
   - Visit your Streamlit Cloud URL to use Salary Scope.
   - **Live App:** [SalaryScope.streamlit.app](https://salaryscope.streamlit.app/)

---

## 📊 Model Performance
- **Model:** Gradient Boosting Regressor
- **Accuracy Score (R²):** **96%**

---

## 📁 Project Structure
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
```

---

## 🌐 Social & Credits
- **GitHub:** [SpicychieF05](https://github.com/SpicychieF05)
- **LinkedIn:** [Chirantan Mallick](https://www.linkedin.com/in/chirantan-mallick)
- **Twitter (X):** [@Chirantan2965](https://x.com/Chirantan2965)
- **Discord:** [Join Server](https://discord.gg/mc2jRBuV)
- **Developer:** [Chirantan Mallick](https://linktr.ee/chirantan_mallick)

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
