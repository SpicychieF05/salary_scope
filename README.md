# Salary Scope: A Data Scientist Salary Predictor

Welcome to **Salary Scope**, a web application that predicts the salary of a data scientist based on key factors like experience, education, and location. This project uses a machine learning model trained on real-world data to provide accurate salary estimates.

---

## ✨ Features
- **Accurate Predictions:** Utilizes a Gradient Boosting Regressor model with **R² = 0.89 (89%)** accuracy.
- **Interactive Web Interface:** User-friendly form to input your details and get instant salary predictions.
- **Data-Driven Insights:** Helps professionals and employers understand salary benchmarks in the industry.
- **Easy Deployment:** Optimized for Render cloud platform.

---

## 🛠️ Tech Stack & Tools
- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn, pandas, numpy
- **Model:** Gradient Boosting Regressor
- **Deployment:** Render (Gunicorn)

---

## 🚀 Getting Started (Local Development)

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd Salary-scope
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Train the model (if needed):**
   ```sh
   python train_model.py
   ```
5. **Run the app locally:**
   ```sh
   python app.py
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000)

---

## ☁️ Deploying on Render

1. **Push your code to GitHub.**
2. **Create a new Web Service on [Render](https://render.com/):**
   - Connect your GitHub repo.
   - Render will auto-detect your Python app.
   - Make sure you have a `Procfile` with:
     ```
     web: gunicorn app:app
     ```
   - All required files (`model.joblib`, `requirements.txt`, etc.) should be in the repo.
3. **Deploy!**
   - Render will build and start your app.
   - Visit your Render URL to use Salary Scope.

---

## 📈 Model Performance

- **Model:** Gradient Boosting Regressor
- **Accuracy Score (R²):** **<span style="color:#2546ff;font-weight:bold;">89%</span>**

---

## 📁 Project Structure

```
Salary-scope/
  app.py
  train_model.py
  requirements.txt
  Procfile
  model.joblib
  static/
  templates/
  README.md
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---

## 📄 License

Distributed under the MIT License.
