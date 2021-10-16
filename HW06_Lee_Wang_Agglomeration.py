import pandas as pd


def max_correlated_index(correlation_df):
    '''
    return the attributes are most strongly cross-correlated with each other
    :param correlation_df:
    :return:
    '''
    max_columnIndex = 0
    max_rowIndex = 0
    max_value = 0
    for rowIndex, row in correlation_df.iterrows():  # iterate over rows
        for columnIndex, value in row.items():
            if (value != 1.00 and value > max_value):
                max_value = value
                max_columnIndex = columnIndex
                max_rowIndex = rowIndex
    return (max_columnIndex, max_rowIndex, max_value)

if __name__ == '__main__':
    data_frame = pd.read_csv('HW_CLUSTERING_SHOPPING_CART_v2211.csv')
    # To remove white space everywhere in the data frame, especially for the name of attributes
    data_frame.columns = data_frame.columns.str.replace(' ', '')
    # Drop the irrelevant "ID" column for calculating correlation.
    df_withoutID = data_frame.drop('ID', 1)

    # Record these values with two digits past the decimal point
    correlation_df = df_withoutID.corr().round(2)
    # Replace all the 1 to 0 on the main diagonal
    df_1_to_0 = correlation_df.replace(1.00, 0.00)
    correlation_df_abs = df_1_to_0.abs()
    #QA.1
    print(max_correlated_index(correlation_df_abs))
    #QA.2
    print(correlation_df_abs['Fish'].nlargest(1))


