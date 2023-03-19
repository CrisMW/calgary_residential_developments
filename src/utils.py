import pandas as pd
import matplotlib.pyplot as plt

def get_absolute_and_relative_counts(
    df: pd.DataFrame,
    col_label: str,
) -> pd.DataFrame:
    """Combines relative and absolute value counts in one dataframe. Includes missing values."""

    relative = df[col_label].value_counts(dropna=False, normalize=True)
    absolute = df[col_label].value_counts(dropna=False)

    return pd.concat(
        [relative, absolute],
        keys=['relative', 'absolute'],
        axis=1,
    )

def simplify(axis: plt.Axes):
    """Removes unnecessary spines, and ticks from axis object"""
    axis.tick_params(bottom=False, top=False, left=False, right=False)
    for spine in ['right', 'left', 'top', 'bottom']:
        axis.spines[spine].set_visible(False)

    return axis
