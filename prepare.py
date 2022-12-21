import os
import urllib.request
import pandas as pd


def download_dataset(directory, url, file_path):
    # Create the specified directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    urllib.request.urlretrieve(url, file_path)


def load_dataset(file_path, names=None):
    # Load the dataset into a pandas DataFrame
    df = pd.read_csv(file_path, header=None, index_col=False, names=names)
    return df


def drop_columns_and_rows(df, columns):
    # Drop the original moves column and any rows with missing values
    df = df.drop(columns=columns).dropna()
    return df
