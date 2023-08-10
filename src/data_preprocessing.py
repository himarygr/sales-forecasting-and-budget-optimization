import pandas as pd

def load_data(file_path):
    """Load the CSV data file."""
    return pd.read_csv(file_path)

def preprocess_train_data(train_data):
    """Preprocess the training data."""
    train_data['date'] = pd.to_datetime(train_data['date'])
    return train_data

def preprocess_test_data(test_data):
    """Preprocess the test data."""
    test_data['date'] = pd.to_datetime(test_data['date'])
    return test_data

def preprocess_sample_submission(sample_submission):
    """Preprocess the sample submission data."""
    sample_submission['sales'] = 0  # Initialize sales as 0 for the sample submission
    return sample_submission
