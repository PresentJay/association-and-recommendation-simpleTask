import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# Read in the dataset
df = pd.read_csv("adult_dataset.csv")

# Preprocess the data by converting categorical variables into numerical ones
df = pd.get_dummies(df)

# Convert the data into a list of transactions
transactions = []
for row in df.iterrows():
    transactions.append(list(row[1]))

# Encode the transactions using the TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)

# Convert the encoded transactions into a DataFrame
df = pd.DataFrame(te_ary, columns=te.columns_)

# Run the apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

# Print the frequent itemsets
print(frequent_itemsets)
