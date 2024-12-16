# Insurance Dataset Regression Analysis

This repository contains a machine learning project that utilizes the **Random Forest Regressor** to solve a regression problem based on an insurance dataset. The project demonstrates data preprocessing, feature engineering, model training, and evaluation of regression performance.

## Project Overview

The goal of this project is to predict insurance costs based on various features such as age, gender, BMI, number of children, smoking habits, and region. The **Random Forest Regressor** is chosen for its ability to handle non-linear relationships and provide robust predictions.

## Dataset

The dataset used in this project contains the following features:

- `age`: Age of the individual.
- `sex`: Gender of the individual.
- `bmi`: Body mass index, a measure of body fat based on height and weight.
- `children`: Number of children/dependents covered by health insurance.
- `smoker`: Smoking status of the individual.
- `region`: Region of residence (e.g., northeast, southeast, etc.).
- `charges`: Final medical charges billed to the insurance company (target variable).

## Project Structure

```
├── data - insurance.csv        # Insurance dataset
├── notebooks - random_forest_regressor.py   # Jupyter Notebook with detailed implementation
├── README.md
└── requirements.txt
```

## Key Steps

1. **Data Preprocessing**
   - Handled missing values (if any).
   - Encoded categorical variables (`sex`, `smoker`, `region`) using one-hot encoding.
   - Standardized numerical features (`age`, `bmi`, `children`).

2. **Exploratory Data Analysis (EDA)**
   - Visualized distributions of features.
   - Examined correlations between features and the target variable.

3. **Model Training**
   - Split the dataset into training and testing sets.
   - Tuned hyperparameters using cross-validation.

4. **Evaluation**
   - Evaluated the model using metrics like R² score.

## Results

- **R² Score**: _e.g., 0.86_

The Random Forest Regressor demonstrated strong predictive performance and highlighted the most significant features impacting insurance costs.

## Getting Started

### Prerequisites

- Python 3.8+
- Libraries: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/teamarnab/All-Regression-Models/tree/main/Random%20Forest
   ```
2. Navigate to the project directory:
   ```bash
   cd insurance-rf-analysis
   ```
3. Run the Jupyter Notebook or Python scripts.

## Insights

- Smoking significantly increases insurance costs.
- BMI and age also play key roles in determining charges.
- The Random Forest model can identify and rank important predictors effectively.

