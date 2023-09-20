import pandas as pd
import matplotlib.pyplot as plt
import os


def get_mean(df: pd.DataFrame, col: str):
    return df[col].mean()


def get_median(df: pd.DataFrame, col: str):
    return df[col].median()


def get_stddev(df: pd.DataFrame, col: str):
    return df[col].std()


def get_distributino_plot(
    df: pd.DataFrame, col: str, xlabel: str, title: str, out_dir: str
):
    plt.hist(df[col], color="lightgreen", ec="black")
    plt.xlabel(xlabel)
    plt.title(title)
    fig_path = os.path.join(out_dir, xlabel + "_distribution.png")
    plt.savefig(fig_path, dpi=300)
    plt.show()
    plt.close()
