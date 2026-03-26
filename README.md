# Student-performanc-predictor
This project demonstrates a basic machine learning classification model built using Python. It generates a synthetic dataset with random values for marks, attendance, and study hours, then trains a Logistic Regression model to predict the performance outcome.
A python script which is used to check if a student is pass or fail in a subject or not. Student Performance Predictor

A simple AI/ML project that predicts whether a student will Pass or Fail based on their marks, attendance, and average study hours per day using Logistic Regression in Python.

Overview: This project demonstrates a basic machine learning classification model built using Python. It generates a synthetic dataset with random values for marks, attendance, and study hours, then trains a Logistic Regression model to predict the performance outcome.

Features:

Predicts Pass/Fail for students

Uses Logistic Regression (binary classification)

Automatically generates dataset (no external files needed)

Displays accuracy and classification report

Simple console input for predictions

Libraries Used:

pandas – Data handling and storage

scikit-learn – Model training and evaluation

random – Random dataset generation

Methodology:

Dataset Generation – Create 500 random student records (marks, attendance, study hours).

Preprocessing – Split dataset into training (80%) and testing (20%) sets.

Model Training – Train Logistic Regression model from scikit-learn.

Evaluation – Calculate accuracy and classification metrics.

Prediction – Accept user inputs and predict Pass/Fail with probability.

Model Evaluation: Test Samples: 300 Accuracy: 0.8667

Classification Report: Class | Precision | Recall | F1-Score | Support 0 (Fail) | 0.4000 | 0.0513 | 0.0909 | 39 1 (Pass) | 0.8746 | 0.9885 | 0.9281 | 261 Accuracy: 0.8667 (300 samples) Macro Avg: 0.6373 | 0.5199 | 0.5095 Weighted Avg: 0.8129 | 0.8667 | 0.8192

Result: The model achieved 86.67% accuracy and performs consistently in predicting whether a student will pass or fail. It’s a solid beginner-level AI/ML implementation using only basic Python libraries.

Future Enhancements:

Add visualizations using matplotlib

Build a simple UI with Streamlit

Store results in a CSV or database

Improve predictions with balanced data

Project Structure: student-performance-predictor/ │ ├── main.py – Main program ├── requirements.txt – Dependencies ├── README.md – Project documentation ├── report.pdf – Project report └── .gitignore – Ignore unnecessary files

How to Run:

Install dependencies: pip install -r requirements.txt

Run the program: python main.py

Author: Name: Uchit Jain Register No: 25BAI10798 University: VIT Bhopal University
