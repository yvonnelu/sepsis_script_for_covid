import matplotlib.pyplot as plt
import seaborn as sns


def missing_values_barplot(df, missing=True, return_vals=False):
    """ Takes a dataframe and plots the percentage of missing values (or not missing if set False) """
    # Sorted percentage of missing (or contained) values
    s_amount = 100 * df.isna().sum() / df.shape[0]
    if missing == False:
        s_amount = 100 - s_amount
    s_amount.sort_values(ascending=False, inplace=True)

    # Barplot it
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.barplot(s_amount.index, s_amount.values, ax=ax, palette="Blues_d")

    # Some niceties
    ax.set_title('% {} values'.format('Missing' if missing else 'Contained'), weight='bold', fontsize=16)
    plt.xticks(rotation=45)

    if return_vals:
        return s_amount

