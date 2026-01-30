import numpy as np
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df = df.drop(columns=["index", "Unnamed: 0"], errors="ignore")
    return df

def window_features(df, sensor_cols, label_col, window=128, step=64):
    X, y = [], []
    data = df[sensor_cols].values
    labels = df[label_col].values

    for i in range(0, len(df) - window, step):
        w = data[i:i+window]
        X.append(np.hstack([
            w.mean(axis=0),
            w.std(axis=0)
        ]))
        y.append(labels[i])

    return np.array(X), np.array(y)
