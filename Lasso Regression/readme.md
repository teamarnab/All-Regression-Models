# Lasso Regression on Insurance Dataset

This repository contains the implementation of a regression-based machine learning solution using **Lasso Regression** on an insurance dataset. The goal of this project is to predict insurance charges based on various customer features such as age, BMI, and smoking habits.

## Problem Statement

Insurance companies often rely on predictive models to estimate the costs associated with insuring individuals. This project uses Lasso Regression to:

1. Build a model that predicts insurance charges accurately.
2. Perform feature selection to identify the most significant factors influencing charges.

## Dataset

The dataset used in this project is publicly available and includes the following columns:

- `age`: Age of the individual.
- `sex`: Gender of the individual.
- `bmi`: Body Mass Index, a measure of body fat based on height and weight.
- `children`: Number of children/dependents.
- `smoker`: Smoking status (Yes/No).
- `region`: Region of the individual (e.g., northeast, southwest).
- `charges`: Medical insurance costs (target variable).

## Key Features of the Project

- **Exploratory Data Analysis (EDA):**
  - Statistical summary of the data.
  - Visualization of relationships between features and the target variable.

- **Preprocessing:**
  - Handling missing values (if any).
  - Encoding categorical variables.
  - Scaling numerical features.

- **Model Training and Evaluation:**
  - Implementation of Lasso Regression with cross-validation.
  - Hyperparameter tuning using GridSearchCV.
  - Evaluation using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²).

## Repository Structure

```
├── data - insurance.csv          # Dataset used for training and testing
├── lasso_regression.py
├── README.md
└── requirements.txt           # Required Python packages
```

## Getting Started

### Prerequisites

- Python 3.8+
- Libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/teamarnab/All-Regression-Models/tree/main/Lasso%20Regression
   ```

2. Navigate to the repository:
   ```bash
   cd lasso-regression-insurance
   ```

3. Execute the Lasso Regression notebook for model training and evaluation:
   ```bash
   jupyter notebook notebooks/lasso_regression.py
   ```

## Results

- **Best Model Performance:**
  - Mean Absolute Error (MAE): `<value>`
  - Mean Squared Error (MSE): `<value>`
  - R-squared (R²): `<value>`

- **Feature Selection:**
  Lasso Regression identified the following features as the most significant predictors of insurance charges:
  - `smoker`
  - `age`
  - `bmi`
