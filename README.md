# 📱 Google Play Store App Rating Prediction

This project aims to predict the **rating of apps** listed on the Google Play Store using machine learning and deep learning models. It explores how different app features (like size, installs, category, etc.) influence user ratings.

---

##  Project Objective

To build a model that can accurately predict an app's **user rating (from 1.0 to 5.0)** based on its features, helping developers and marketers understand what makes an app successful.

---

##  Dataset

The dataset contains information about apps from the Google Play Store, including:

- App Name
- Category
- Rating (Target Variable)
- Reviews
- Size
- Installs
- Type (Free/Paid)
- Price
- Content Rating
- Genres
- Last Updated
- Android Version

> **Note:** All features were preprocessed into a **fully numeric** dataset for training.

---

## 🛠 Technologies Used

- Python
- NumPy, Pandas
- Matplotlib, Seaborn (for EDA & Visualization)
- Scikit-learn (for preprocessing and model training)
- TensorFlow / Keras (for deep learning model)
- Jupyter Notebook

---

##  Machine Learning & Deep Learning Models

- **Linear Regression**
- **Random Forest Regressor**
- **Support Vector Regressor (SVR)**
- **Neural Network (Keras Sequential model)**

The best model was chosen based on **RMSE (Root Mean Squared Error)** and **R² Score**.

---

##  Evaluation Metrics

- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

---

## Results

The final selected model achieved:
- High accuracy in predicting app ratings
- Generalization on test data without overfitting

> The model was saved as `model.pkl` for deployment or reuse.

---


