import pandas as pd

data = {
    'TransactionID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Timestamp': ['2022-01-01 10:00:00', '2022-01-02 14:30:00', '2022-01-03 09:45:00', '2022-01-04 12:15:00',
                  '2022-01-05 11:30:00', '2022-01-06 15:00:00', '2022-01-07 13:20:00', '2022-01-08 10:45:00'],
    'StockSymbol': ['AAPL', 'GOOGL', 'MSFT', 'AAPL', 'GOOGL', 'MSFT', 'AAPL', 'GOOGL'],
    'TransactionType': ['BUY', 'SELL', 'REC', 'BUY', 'SELL', 'CMD', 'BUY', 'SELL'],
    'Quantity': [10, 5, 20, 8, 15, 1, 12, 7],
    'Price': [150.50, 2500.75, None, 160.20, 2550.30, None, 155.80, 2480.90]
}

df = pd.DataFrame(data)

json_key = [
    {"StockSymbol": "AAPL", "TransactionType": "BUY"},
    {"StockSymbol": "GOOGL", "TransactionType": "SELL"}
]

json_key2 = [
    {"StockSymbol": "AAPL", "TransactionType": "SELL"},
    {"StockSymbol": "GOOGL", "TransactionType": "BUY"}
]

json_key3 = [
    {"TransactionType": "CMD"},
    {"TransactionType": "REC"}
]


def split_df(df, json_key=None):
    if json_key is None:
        json_key = []

    res_df = []

    for q in json_key:
        query = " and ".join([f"{k} == '{v}'".format(k=k, v=v) for k, v in q.items()])
        print(query)

        res_df.append(df.query(query))
    return pd.concat(res_df)


print(split_df(df, json_key))

print(split_df(df, json_key2))

print(split_df(df, json_key3))
