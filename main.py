import time
import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from prepare import download_and_prepare_dataset


def main():
    # Download and prepare the dataset
    transactions = download_and_prepare_dataset(
        "datasets/chess", "http://archive.ics.uci.edu/ml/machine-learning-databases/chess/king-rook-vs-king-pawn/kr-vs-kp.data", "krkp.data")

    # Encode the transactions as a boolean matrix
    te = TransactionEncoder()
    matrix = te.fit_transform(transactions)

    # Create a Pandas DataFrame from the encoded matrix
    df = pd.DataFrame(matrix, columns=te.columns_)

    # Create a table showing the frequency of each item
    item_counts = df.sum().sort_values(ascending=False)
    print(item_counts)

    # Create a bar plot showing the frequency of the top 10 items
    item_counts[:10].plot.bar()
    plt.xlabel("Item")
    plt.ylabel("Frequency")
    plt.title("Frequency of Top 10 Items")
    plt.show()


if __name__ == "__main__":
    main()
