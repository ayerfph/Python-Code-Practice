"""
I write this code to reviewing the basics in data manipulation with pandas library.

"""

import pandas as pd # This is how u import pandas

df = pd.read_csv("file.csv") # This is how u create dataframes

def setup_data_frames():
    df. head() # Showing first 5 columns
    df.info() # Showing information of the data frame
    df.shape # Shows the (columns, row) of data frame.
    df.describe() # Shows the description of the data frame
    df.values # Shows the values of data frames
    df.columns # Shows the column names of the data frame
    df.index # Shows the index of data frames

def sorting():

    # Using sorting_values
    df_sorted = df.sort_values('sort_based_on_column_name')
    df_sorted.head() # Show result

    # Using sorting by descending order
    df_desc = df.sort_values('desc_sort_based_on_column_name', ascending=False)
    df_desc.head() # Show result

    # Sort data by column1, then descending column2 (using multiple columns for sorting values)
    df_sort_two_columns = df.sort_values(["column1", "column2"], ascending=[True, False])
    df_sort_two_columns.head() # Show result

def subsetting_columns():
    # Selecting individual columns
    data = df['column1']
    data.head() # Show result

    # Selecting two columns
    data = df[['column1', 'column2']]
    data.head() # Show result

def subsetting_rows():
    # Filtering rows where individuals is greater than numbers
    data_gt_10k = df[df['column1'] > 10000]
    data_gt_10k.head() # Show result

    # Filtering for rows where column1 is exact data
    column_data = df[df['column1'] == 'exact_data']
    column_data.head() # Show result

    # Filtering rows where column1 is less than 1000 and column2 is exact_data
    specific_data = df[(df['column1'] < 1000) & (df['column2'] == 'exact_data')]
    specific_data.head() # Show result

def subsetting_with_categoria_variables():
    category_columns = ['col1', 'col2', 'col3'] # Category columns
    categ_data = df[df["row_data"].isin(category_columns)] # Filter rows in category_columns
    categ_data.head() # Show result

def add_columns():
    # Add new_col as sum of col1 and col2
    df['new_col'] = df['col1'] + df['col2']
    df.head() # Show Result

    # Manipulating data using sorting rows, subsetting columns, subsetting rows, and adding new columns
    df['new_col'] = 1000 * df['col1'] / df['col2']
    subset_rows = df[df['new_col'] > 20]
    sort_rows = subset_rows.sort_values("new_col", ascending=False)
    subset_columns = sort_rows[["col3", "new_col"]]
    subset_columns.head() # Show result

def summarize_num_data():
    df['col1'].mean() # getting mean
    df['col1'].median() # getting median
    df['col1'].mode() # getting mode
    df['col1'].min() # getting minimum
    df['col1'].max() # getting maximum
    df['col1'].var() # getting variance
    df['col1'].std() # getting standard deviation

    # The .agg(.method)
    def pct30(column):
        return column.quantile(0.3)
    # Apply the method
    df['col1'].agg(pct30)

    # If multiple columns
    df[['col1', 'col2']].agg(pct30)

    # If multiple summaries
    def pct40(column):
            return column.quantile(0.4)

    df['col1'].agg([pct30, pct40])

    # Cumulative Sum
    df['col1'].cumsum()

    # Cumulative Statistics
    df['col1'].cummax()
    df['col1'].cummin()
    df['col1'].cumprod()

def drop_duplicates():
    df.drop_duplicates(subset="col1") # removing one

    df.drop_duplicates(subset=["col1", "col2"]) # removing duplicate pairs


def value_counts():
    df["col1"].value_counts()
    df["col1"].value_counts(sort=True) # sorted
    df["col1"].value_counts(normalize=True) # proportion
