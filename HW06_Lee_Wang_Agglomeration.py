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
    # you might need to change the path to run
    data_frame = pd.read_csv('D:\CodeBaby\Python\hw6\hw06_CSCI420\HW_CLUSTERING_SHOPPING_CART_v2211.csv')
    # To remove white space everywhere in the data frame, especially for the name of attributes
    data_frame.columns = data_frame.columns.str.replace(' ', '')
    # Drop the irrelevant "ID" column for calculating correlation.
    df_withoutID = data_frame.drop('ID', 1)

    # Record these values with two digits past the decimal point
    correlation_df = df_withoutID.corr().round(2)
    # Replace all the 1 to 0 on the main diagonal
    df_1_to_0 = correlation_df.replace(1.00, 0.00)
    # get the absolute value of coefficient for easier calculations
    correlation_df_1_to_0_abs = df_1_to_0.abs()
    correlation_df_abs = correlation_df.abs()
    # export the correlation table for better answer the questions from write up
    correlation_df.to_csv("Correlation_table.csv", index=True)


    print("QA.a")
    print("Two attributes are most strongly cross-correlated")
    print(max_correlated_index(correlation_df_abs))
    print("QA.b")
    print('Cross-correlation coefficient of Chips with cereal')
    print((correlation_df_abs['Chips']['Cerel']))
    print("QA.c")
    print('What fish most strongly cross-correlated with')
    print(correlation_df_abs['Fish'].nlargest(1))
    print("QA.d")
    print('What vegges most strongly cross-correlated with')
    print(correlation_df_abs['Vegges'].nlargest(1))
    print("QA.f")
    print('Do people usually buy milk and cereal')
    print((correlation_df['Milk']['Cerel']))
    print("They don't.")
    print("QA.f")
    print('Which two attributes are not strongly cross-correlated with anything')
    print(correlation_df_abs.sum(axis=0).nsmallest(2))


