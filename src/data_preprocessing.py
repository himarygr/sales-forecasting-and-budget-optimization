import pandas as pd


def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)


def preprocess_data(train_data, test_data, sample_submission):
    """Preprocess the dataset."""
    train_data['date'] = pd.to_datetime(train_data['date'])
    preprocessed_train = train_data
    test_data['date'] = pd.to_datetime(test_data['date'])
    preprocessed_test = test_data
    sample_submission['sales'] = 0  # Initialize sales as 0 for the sample submission
    preprocessed_sample_submission = sample_submission
    
    return preprocessed_train, preprocessed_test, preprocessed_sample_submission
