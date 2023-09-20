import pandas as pd
from lib import get_mean, get_median, get_stddev, get_distributino_plot
import os
import matplotlib.pyplot as plt


def generate_stats(df: pd.DataFrame, col: str):
    res = {}
    res["mean"] = get_mean(df, col)
    res["median"] = get_median(df, col)
    res["std"] = get_stddev(df, col)
    return res


def generate_dist_plots(df: pd.DataFrame, out_dir):
    for c in df.columns:
        get_distributino_plot(df, c, c, f"{c} Distribution")
        fig_path = os.path.join(out_dir, c + "_distribution.png")
        plt.savefig(fig_path, dpi=300)
        plt.close()


def main():
    df = pd.read_csv("diabetes.csv")

    with open("./output/stats.md", "w") as f:
        f.write("## Descriptive Statistics Results\n\n")
        for c in df.columns:
            res = generate_stats(df, c)
            f.write("### " + c + "\n")
            f.write(f'Mean: {res["mean"]} <br> \n ')
            f.write(f'Median: {res["median"]} <br> \n')
            f.write(f'Std: {res["std"]} <br> \n')
            f.write("\n\n")

    generate_dist_plots(df, "./output")


if __name__ == "__main__":
    main()
