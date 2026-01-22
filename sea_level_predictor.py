import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # 1. Load data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Line of best fit (all data)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    x_pred = range(1880, 2051)
    y_pred = res.intercept + res.slope * x_pred

    plt.plot(x_pred, y_pred, "r")

    # 4. Line of best fit (from 2000)
    df_2000 = df[df["Year"] >= 2000]

    res2 = linregress(
        df_2000["Year"],
        df_2000["CSIRO Adjusted Sea Level"]
    )

    x_pred2 = range(2000, 2051)
    y_pred2 = res2.intercept + res2.slope * x_pred2

    plt.plot(x_pred2, y_pred2, "green")

    # 5. Labels & title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save
    plt.savefig("sea_level_plot.png")

    return plt.gca()
