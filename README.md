# Time Series Analysis for Budget Optimization

**Project Overview**

The objective of this project is to predict 3 months of item-level sales data at different store locations and optimize budgets and placements to maximize key product metrics. We leverage time series analysis techniques to forecast sales, and then use these forecasts to optimize ad budgets for different placements. This project is a simplified representation of a real-world scenario where data-driven decisions are crucial for advertising campaigns.

**Table of Contents**

1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Data](#data)
4. [Usage](#usage)
5. [Workflow](#workflow)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

### Project Structure <a name="project-structure"></a>

The project repository is structured to facilitate an organized workflow:

```
- data/
  - train.csv
  - test.csv
  - sample_submission.csv
- preprocessed_data/
  - preprocessed_train.csv
  - preprocessed_test.csv
  - preprocessed_sample_submission.csv
- feature_engineered_data/
  - feature_engineered_train.csv
  - feature_engineered_test.csv
- src/
  - data_preprocessing.py
  - feature_engineering.py
  - time_series_model.py
  - budget_optimization.py
  - main.py
- requirements.txt
- README.md
```

### Getting Started <a name="getting-started"></a>

#### Prerequisites <a name="prerequisites"></a>
To run this project, you need:

Python (>=3.6)
Required Python packages (see requirements.txt)

#### Installation <a name="installation"></a>
* Clone the project repository:
```
git clone https://github.com/himarygr/sales-forecasting-and-budget-optimization
cd https://github.com/himarygr/sales-forecasting-and-budget-optimization
```
* Install the required packages:
```
pip install -r requirements.txt
```

### Data <a name="data"></a>
The project uses the following dataset files:

* train.csv: Training data containing historical sales data.
* test.csv: Test data for which you need to predict sales.
* sample_submission.csv: Sample submission file with the correct format for submitting predictions.

### Usage <a name="usage"></a>
To run the complete pipeline, follow these steps:

1. Preprocess the data using the **data_preprocessing.py** script:
```
python src/data_preprocessing.py
```
2. Perform feature engineering using the **feature_engineering.py** script:
```
python src/feature_engineering.py
```
3. Train the time series model using the **time_series_model.py** script:
```
python src/time_series_model.py
```
4. Optimize budgets based on forecasts using the **budget_optimization.py** script:
```
python src/budget_optimization.py
```
5. Orchestrate the entire pipeline using the **main.py** script:
```
python src/main.py
```

### Workflow <a name="workflow"></a>
The project workflow involves the following steps:

* **Data Preprocessing:** The data_preprocessing.py script loads and preprocesses the raw data.
* **Feature Engineering:** The feature_engineering.py script creates time-based features and lag features.
* **Time Series Model:** The time_series_model.py script trains an ARIMA model to forecast sales.
* **Budget Optimization:** The budget_optimization.py script optimizes budgets based on the forecasts.
* **Pipeline Orchestration:** The main.py script orchestrates the entire pipeline, producing forecasted sales and optimized budgets.

### Results <a name="results"></a>
The project generates:

* Forecasted sales based on the trained time series model.
* Optimized budgets for placements based on the forecasted sales.
* 
Results can be found in the console output or saved to files, as specified in the code.

### Contributing <a name="contributing"></a>
Contributions to this project are welcome. Please follow the standard guidelines for contributing.
