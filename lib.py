import pandas as pd
import matplotlib.pyplot as plt


def get_mean(df: pd.DataFrame, col: str):
    return df[col].mean()


def get_median(df: pd.DataFrame, col: str):
    return df[col].median()


def get_stddev(df: pd.DataFrame, col: str):
    return df[col].std()


def get_distributino_plot(df: pd.DataFrame, col: str, xlabel: str, title: str):
    plt.hist(df[col], color="lightgreen", ec="black")
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()
