import os
import urllib.request
import pandas as pd


def download_dataset(directory, url, file_name):
    # Create the specified directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download the dataset to the specified directory
    file_path = os.path.join(directory, file_name)
    urllib.request.urlretrieve(url, file_path)


def load_dataset(file_name):
    # Load the dataset into a pandas DataFrame
    df = pd.read_csv(file_name, header=None, names=["result", "moves"])
    return df


def split_moves_column(df):
    # Split the moves column into individual moves
    df[["move1", "move2", "move3", "move4", "move5"]
       ] = df["moves"].str.split(" ", expand=True)


def drop_columns_and_rows(df):
    # Drop the original moves column and any rows with missing values
    df = df.drop(columns=["moves"]).dropna()


def create_transactions(df):
    # Create a list of lists, where each inner list represents a transaction
    transactions = df[["move1", "move2", "move3",
                       "move4", "move5"]].values.tolist()
    return transactions


def download_and_prepare_dataset(directory, url, file_name):
    # Download the dataset
    download_dataset(directory, url, file_name)

    file_path = os.path.join(directory, file_name)

    # Load the dataset
    df = load_dataset(file_path)

    # Split the moves column into individual moves
    split_moves_column(df)

    # Drop the original moves column and any rows with missing values
    drop_columns_and_rows(df)

    # Create a list of transactions
    transactions = create_transactions(df)

    return transactions
