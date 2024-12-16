# Insurance Cost Prediction using Multiple Linear Regression

This repository contains a solution to a regression problem, where we predict insurance costs based on various features such as age, BMI, smoking status, and more. The dataset and model implementation leverage Multiple Linear Regression to understand and predict the relationship between the input features and insurance costs.

## Dataset

The dataset used in this project contains the following columns:
- `age`: Age of the individual.
- `sex`: Gender of the individual.
- `bmi`: Body Mass Index (BMI).
- `children`: Number of children covered by health insurance.
- `smoker`: Smoking status of the individual (yes/no).
- `region`: Region of residence (northeast, northwest, southeast, southwest).
- `charges`: Insurance cost (target variable).

The dataset is included in the repository.

## Project Structure

```
├── dataset - insurance.csv
├── linear_regression.py
├── README.md
├── requirements.txt
```

## Implementation

The project uses Multiple Linear Regression to:
1. Preprocess the data:
   - Handle categorical variables (e.g., one-hot encoding for `sex`, `smoker`, and `region`).
   - Normalize numerical variables for better model performance.
2. Split the data into training and testing sets.
3. Train the Multiple Linear Regression model.
4. Evaluate the model using R-squared (R²).

### Key Libraries Used
- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

## Results

The model's performance metrics:
    - `Training data score is: 0.7383287003518029`
    - `Test data score is: 0.7727987396309755`
    - `Full data score is: 0.7472604953135835`


## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/teamarnab/All-Regression-Models/tree/main/Linear%20Regression
   ```
2. Navigate to the `src` directory:
   ```bash
   cd src
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python linear_regression.py
   ```

## Visualization

The script includes visualization of:
- Correlation heatmap between features.
- Distribution of insurance charges.


