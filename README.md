# Heart Attack Prediction Using Machine Learning

A machine learning project that analyzes cardiovascular health parameters and compares multiple machine learning approaches for predicting heart attack outcomes.

## 📌 Project Overview

This project uses patient health data to explore whether cardiovascular and biochemical parameters can be used to predict heart attack outcomes.

The project compares multiple machine learning approaches, including regression, classification, dimensionality reduction, and a neural network.

## 📊 Dataset

The dataset contains 1,319 patient records with the following features:

- Age
- Gender
- Heart rate
- Systolic blood pressure
- Diastolic blood pressure
- Blood sugar
- CK-MB
- Troponin
- Result

The target variable is `Result`, which contains positive and negative outcomes.

## 🤖 Machine Learning Models

The following approaches were implemented and compared:

- Logistic Regression
- Ridge Regression
- Lasso Regression
- Gaussian Naive Bayes
- Support Vector Machine
- Random Forest
- PCA + Gaussian Naive Bayes
- Neural Network

## 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

Cross-validation was also performed for the Ridge and Lasso regression models.

## 🏆 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 79.92% | 82.63% | 85.19% | 83.89% |
| Ridge Regression | 70.45% | 71.43% | 86.42% | 78.21% |
| Lasso Regression | 71.21% | 71.29% | 88.89% | 79.12% |
| Gaussian Naive Bayes | 69.70% | 98.81% | 51.23% | 67.48% |
| Support Vector Machine | 81.06% | 86.36% | 82.10% | 84.18% |
| Random Forest | 98.48% | 98.77% | 98.77% | 98.77% |
| Gaussian Naive Bayes + PCA | 61.74% | 63.56% | 88.27% | 73.90% |
| Neural Network | 74.24% | 76.40% | 83.95% | 80.00% |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow
- Jupyter Notebook

## 📁 Project Structure

```text
heart-attack-prediction/
│
├── data/
│   └── Medicaldataset.csv
│
├── notebooks/
│   └── heart_attack_prediction.ipynb
│
├── images/
│
├── model_comparison_results.csv
├── requirements.txt
├── .gitignore
└── README.md
```
## ⚠️ Disclaimer

This project is intended for educational and experimental purposes only. It is not a medical diagnostic system and should not be used for clinical decision-making.