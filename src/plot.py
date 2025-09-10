import pandas as pd
import matplotlib.pyplot as plt

def plot_baseline_vs_optimized(baseline: pd.Series,
                               optimized: pd.Series,
                               title: str = "Baseline vs Optimized (weekly hours)",
                               save_path: str | None = None) -> None:
    """
    Draw side-by-side bar chart for Baseline vs Optimized.
    """
    # Align both baseline and optimized series by activity labels
    labels = sorted(set(baseline.index) | set(optimized.index))
    b = baseline.reindex(labels).fillna(0)
    o = optimized.reindex(labels).fillna(0)

    # Plot side-by-side bars
    x = range(len(labels))
    plt.figure(figsize=(10, 4))
    plt.bar(x, b.values, label="Baseline")
    plt.bar([i+0.4 for i in x], o.values, label="Optimized")

    # Formatting the x-axis labels
    plt.xticks([i+0.2 for i in x], labels, rotation=45, ha="right")
    plt.ylabel("Hours per week")
    plt.title(title)
    plt.legend()
    plt.tight_layout()

    # Optionally save to file
    if save_path:
        plt.savefig(save_path, dpi=200)
    plt.show()
