![Salary Scope Banner](./assets/banner.jpg.jpg)

# 📊 Salary Scope: A Data Scientist Salary Predictor

Welcome to **Salary Scope**, a web application that predicts the salary of a data scientist based on key factors like experience level, employment type, and location. This project leverages a machine learning model trained on a comprehensive dataset to provide insightful salary estimates.

The live application is deployed on Vercel. You can access it here: **[Link to your deployed Vercel app]**

---

## ✨ Features

* **Accurate Predictions**: Utilizes a Random Forest Regressor model with **89% accuracy**.
* **Interactive Web Interface**: A clean and user-friendly interface built with Flask to input data and receive salary predictions.
* **Data-Driven Insights**: Helps aspiring data scientists and employers understand salary benchmarks in the industry.
* **Scalable Deployment**: Deployed on Vercel for fast, reliable, and scalable performance.

---

## 🛠️ Tech Stack & Tools

This project was built using a modern stack for machine learning and web development:

* **Backend**: Python, Flask
* **Machine Learning**: Scikit-learn, Pandas, NumPy
* **Model**: Random Forest Regressor
* **Deployment**: Vercel
* **Code Management**: Git & GitHub

---

## 🚀 Getting Started

Follow these instructions to get a local copy up and running for development and testing purposes.

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/SpicychieF05/Salary-Scope.git](https://github.com/SpicychieF05/Salary-Scope.git)
    cd Salary-Scope
    ```

2.  **Create a virtual environment:**
    This isolates the project dependencies from your system's Python installation.
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    The `requirements.txt` file contains all the necessary Python libraries.
    ```sh
    pip install -r requirements.txt
    ```

4.  **(Optional) Train the model:**
    The repository already includes pre-trained model files (`.joblib`). However, if you want to retrain the model on new data, run the training script:
    ```sh
    python train_model.py
    ```

5.  **Run the Flask application:**
    This will start a local development server.
    ```sh
    python api/index.py
    ```
    Your application should now be running locally at `http://127.0.0.1:5000`.

---

## ☁️ Deployment

This project is configured for easy deployment on **Vercel**. The `vercel.json` file handles the configuration for Python serverless functions. To deploy your own version:

1.  Push your code to your GitHub repository.
2.  Go to [Vercel](https://vercel.com) and sign up with your GitHub account.
3.  Click "Add New... > Project" and import your GitHub repository.
4.  Vercel will automatically detect the settings in `vercel.json` and deploy the application.

---

## 📁 Project Structure

Here is an overview of the project's file structure:


.
├── api/
│   └── index.py         # Main Flask application file for local and Vercel execution
├── assets/              # Contains static images like the banner
│   └── banner.jpg
├── static/              # Contains static assets (CSS, JS, images)
├── templates/           # Contains HTML templates for the web interface
├── .gitignore           # Specifies files for Git to ignore
├── label_encoder.joblib # Saved label encoder for categorical features
├── model.joblib         # The trained Random Forest Regressor model
├── model_performance.joblib # (Optional) Saved model performance metrics
├── requirements.txt     # A list of all Python dependencies
├── train_model.py       # Python script to train the ML model
└── vercel.json          # Configuration file for Vercel deployment


---

## 📈 Model Performance

The machine learning model was trained and evaluated, achieving the following performance:

* **Model**: Random Forest Regressor
* **Accuracy Score (R²)**: **89%**

The `train_model.py` script contains the complete workflow, from data preprocessing and feature engineering to model training and evaluation.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
