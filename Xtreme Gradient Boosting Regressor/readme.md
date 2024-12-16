# XGBoost Regressor on Insurance Dataset

This repository contains a regression machine learning solution developed using the XGBoost Regressor. The problem is based on an insurance dataset, where the goal is to predict a target variable using multiple features.

## Project Overview

- **Dataset**: Insurance dataset with features like age, sex, BMI, children, smoker, region, etc.
- **Algorithm**: XGBoost Regressor
- **Goal**: To predict the target variable (e.g., insurance charges) with high accuracy.

## Repository Structure

```
├── insurance_xgb_regressor.py
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.8+
- Libraries: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `xgboost`

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/insurance-xgb-regressor.git
   ```
2. Navigate to the repository:
   ```bash
   cd insurance-xgb-regressor
   ```
3. Run the Python script:
   ```bash
   python insurance_xgb_regressor.py
   ```

## Features

- **Data Preprocessing**:
  - Handles missing values and outliers.
  - Encodes categorical variables.
  - Scales numerical features.

- **Model Training**:
  - Uses XGBoost Regressor with hyperparameter tuning.
  - Evaluates the model using metrics like MAE, RMSE, and R^2.

- **Visualization**:
  - Provides insights into feature importance and residual analysis.

## Results

- Achieved high accuracy with an R^2 score.
    - `Model's score with training data is: 0.9946677283017997`
    - `Model's score with test data is: 0.8332089403827523`
    - `Model's score with full data is: 0.9532208315190347`

## Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or additional features.