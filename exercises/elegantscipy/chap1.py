#!/usr/bin/env python
"""
Example code and exercises from Chapter 1 of Elegant Scipy
"""
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('style/elegant.mplstyle')


def read_data(file: str) -> pd.DataFrame:
    """
    Read clean data {file} and return a pandas table with the data.
    """
    with open(file, 'r', encoding="utf-8") as f:
        data = pd.read_csv(f, index_col=0)

    return data


def matched_indexes(df1: pd.DataFrame, df2: pd.DataFrame) -> np.ndarray:
    """
    Takes two DataFrames and returns an NumPy array of the indexes that match
    between the two DataFrames.
    """
    matched_index = pd.Index.intersection(df1.index, df2.index)
    return np.array(matched_index)


def match_index(df1: pd.DataFrame,
                df2: pd.DataFrame,
                column_name: str = '') -> np.ndarray:
    """
    Takes two DataFrames and returns a NumPy array containing only the {df1}
    data of the indexes that match between the two DataFrames.

    Optionally you can supply a {column_name} of the data from {df1} that
    should be returned.
    """
    matched_index = pd.Index.intersection(df1.index, df2.index)
    if column_name != '':
        return np.asarray(df1.loc[matched_index][column_name], dtype=int)

    return np.asarray(df1.loc[matched_index], dtype=int)


def plot_countdensity(counts: np.ndarray) -> None:
    """
    Plot the total count density for each total count per individual.
    """
    total_counts = np.sum(counts, axis=0)
    density = stats.kde.gaussian_kde(total_counts)
    x = np.arange(min(total_counts), max(total_counts), 10000)

    _, ax = plt.subplots()
    ax.plot(x, density(x))
    ax.set_xlabel("Total counts per individual")
    ax.set_ylabel("Density")

    print(
        f"Count statistics:\n"
        f"  min: {np.min(total_counts)}\n"
        f"  mean: {np.mean(total_counts)}\n"
        f"  max: {np.max(total_counts)}"
    )


def get_subset(counts: np.ndarray) -> np.ndarray:
    """
    Randomly selects and returns a subset of input ndarray.
    """
    np.random.seed(seed=7)

    sample_index = np.random.choice(range(counts.shape[1]), size=70,
                                    replace=False)
    return counts[:, sample_index]


def reduce_xaxis_labels(ax, factor: int) -> None:
    """
    Only show every {factor}th x-axis label.
    """
    for i, l in enumerate(ax.xaxis.get_ticklabels()):
        if i % factor != factor-1:
            l.set_visible(False)


def plot_boxplot(counts: np.ndarray) -> None:
    """
    Plots a boxplot of input data.
    """
    _, ax = plt.subplots(figsize=(5, 2))

    with plt.style.context('style/thinner.mplstyle'):
        ax.boxplot(np.log(counts + 1))
        ax.set_xlabel("Individuals")
        ax.set_ylabel("Log gene expression counts")
        reduce_xaxis_labels(ax, 5)


def norm_libsize(counts: np.ndarray) -> np.ndarray:
    """
    Normalize counts to library size and return new ndarray.
    """
    total_counts = np.sum(counts, axis=0)
    return counts / total_counts * 1000000


if __name__ == "__main__":
    counts_raw = read_data('counts.txt')
    samples = list(counts_raw.columns)  # a list of the column names
    gene_metadata = read_data('genes.csv')

    print(counts_raw.iloc[:5, :5])
    print(gene_metadata.iloc[:5, :])

    gene_names: np.ndarray = matched_indexes(counts_raw, gene_metadata)
    gene_lengths: np.ndarray = match_index(
        gene_metadata, counts_raw, 'GeneLength')
    counts: np.ndarray = match_index(counts_raw, gene_metadata)

    print(
        f"{counts.shape[0]} genes measured in {counts.shape[1]} individuals.")

    print(counts.shape)
    print(gene_lengths.shape)

    plot_countdensity(counts)

    counts_subset = get_subset(counts)
    plot_boxplot(counts_subset)

    counts_lib_norm = norm_libsize(counts)
    counts_subset_lib_norm = get_subset(counts_lib_norm)
    plot_boxplot(counts_subset_lib_norm)

    plt.show()
