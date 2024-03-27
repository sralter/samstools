def nullish(df,ordered=True):
    '''
    Creates a summary dataframe showing the amount of null
    values in each column along with the percent of nulls
    compared to the total rows in the dataframe
    
    Inputs:
    - df
    a dataframe
    
    Outputs:
    a new dataframe with the summary of nulls and percentages
    '''
    
#     Define columns in new nullish dataframe

    # number of non-nulls in each original column
    list_nonnulls=[df[col].notna().sum() for col in df.columns]

    # number of nulls in each original column
    list_nulls=[df[col].isna().sum() for col in df.columns]

    
#    Create new dataframe

    df_nullish=pd.DataFrame({'col_name':df.columns,
                            'num_nulls':list_nulls,
                            'num_non_nulls':list_nonnulls})

    
#    Add new column with percent null

    df_nullish['percent_null'] = round((df_nullish['num_nulls'] / (df.shape[0]))*100,2)
    
    if not ordered:
        return df_nullish
    else: 
        df_nullish.sort_values(by='percent_null',inplace=True)
        return df_nullish
