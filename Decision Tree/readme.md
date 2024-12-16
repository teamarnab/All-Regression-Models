# Insurance Dataset - Decision Tree Regressor

This repository contains a solution to a regression problem using the Decision Tree Regressor on an insurance dataset. The primary objective of this project is to predict insurance charges based on various features, such as age, BMI, smoking habits, and more.

## Problem Statement

The goal is to build a regression model that accurately predicts the insurance charges for individuals based on their demographic and health information. The dataset consists of features such as:

- Age
- Gender
- BMI (Body Mass Index)
- Number of Children
- Smoking Status
- Region

## Dataset

The insurance dataset used in this project is publicly available and contains the following columns:

- `age`: Age of the individual
- `sex`: Gender of the individual
- `bmi`: Body mass index
- `children`: Number of children/dependents
- `smoker`: Smoking status (yes/no)
- `region`: Residential area (northeast, northwest, southeast, southwest)
- `charges`: Medical insurance charges (target variable)

## Implementation Details

### Steps Followed:
1. **Data Preprocessing**:
   - Handled missing values (if any).
   - Encoded categorical variables (e.g., `sex`, `smoker`, `region`) using one-hot encoding.
   - Normalized/Standardized numerical features where necessary.

2. **Exploratory Data Analysis (EDA)**:
   - Visualized relationships between features and target variable (`charges`).
   - Checked for correlations among features.

3. **Model Building**:
   - Used `DecisionTreeRegressor` from the `scikit-learn` library.

4. **Model Evaluation**:
   - Evaluated performance using R-squared (R²) score

5. **Results**:
    - `Score with trining model is: 0.9982060600117458`
    - `Score with test model is: 0.9982060600117458`
    - `Score with full model is: 0.9377165109430143`

## Repository Structure

```
├── Decision Tree
│   ├── decision_tree_regressor.py  # Python script containing the solution
│   ├── insurance.csv                # Dataset
│   └── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- Libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/teamarnab/All-Regression-Models/tree/main/Decision%20Tree
   ```

2. Navigate to the project folder:
   ```bash
   cd insurance_decision_tree_regressor
   ```

3. Run the Python script:
   ```bash
   python decision_tree_regressor.py
   ```


## Features

- End-to-end regression solution using the Decision Tree Regressor.
- Clear explanations of the preprocessing and modeling steps.
- Visualizations to understand feature relationships and model performance.


