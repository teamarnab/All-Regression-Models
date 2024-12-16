# KNN Regression on Insurance Dataset

This repository contains the implementation of a K-Nearest Neighbors (KNN) regression model to solve a machine learning problem using an insurance dataset. The project aims to predict insurance-related metrics based on various features in the dataset.

## Project Overview

- **Algorithm**: K-Nearest Neighbors (KNN) Regressor
- **Dataset**: Insurance data containing features such as age, BMI, region, and charges.
- **Objective**: Predict the insurance charges based on the features provided in the dataset.
- **Tools Used**: Python, Scikit-learn, Pandas, Matplotlib, Seaborn

## Repository Structure

```
├── knn_regression.py       # Main script for KNN Regression implementation
├── insurance_dataset.csv   # Dataset used for the project
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## Dataset Description

The insurance dataset includes the following features:

- **age**: Age of the individual.
- **sex**: Gender of the individual.
- **bmi**: Body Mass Index, a measure of body fat based on height and weight.
- **children**: Number of children/dependents covered by insurance.
- **smoker**: Smoking status (yes/no).
- **region**: Residential region (e.g., northeast, southeast).
- **charges**: Individual medical costs billed by health insurance (target variable).

## Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed along with the necessary libraries. You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/teamarnab/All-Regression-Models/tree/main/KNN%20Regressor
   ```
2. Navigate to the project folder:
   ```bash
   cd knn-insurance-regression
   ```
3. Run the script:
   ```bash
   python knn_regressor.py
   ```
4. Explore the results, including performance and metrics.

## Results

- **Performance Metrics**:
  - R² Score: *value*

## Features

- Implements KNN regression with hyperparameter tuning.
- Data preprocessing steps such as handling categorical data and feature scaling.
- Evaluation of model performance using standard r2_score.
- Insights visualized through plots.