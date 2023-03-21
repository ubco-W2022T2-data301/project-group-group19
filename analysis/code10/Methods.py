
from ctypes import Union
import numpy as np
import pandas as pd


def extract_data(data, country='CAD', data_type='ENRG', year_range=[2018, 2022]) -> pd.DataFrame:
    '''
    extracts particular data in a format of choosing

    ------------- 
    #### params
    -------------
    data - dataFrame
    : trasnforms anything passed into it as a data frame

    country - string
    :  the three letter country code default is 'CAD'

    data_type - string
    : three letter type code default is 'ENRG'

    year_range - list
    : the range as a length 2 list to and from that will be extracted default 2018-2022
    
    ------
    #### returns
    -------    
    A data frame that has been processed to specifications
    '''
    if data is not pd.DataFrame:
        data = pd.DataFrame(data)
    print(data['SUBJECT'].unique())
    print(data_type == data['SUBJECT'].unique()[0])
    df = (
        data[data['LOCATION'] == country]
        .groupby('SUBJECT')
        .get_group(data_type)
        .groupby('FREQUENCY')
        .get_group('M')
        .reset_index(drop=True)
    )

    df['TIME'] = _convertDateTime(df['TIME'])
    df = _extract_data_by_year(df, year_range[0], year_range[1])
    return df


def load(data_file_path) -> pd.DataFrame:
    '''
    loads data from file path and returns a DataFrame
    only loads file in the .scv format
    -----
    #### param
    ------
    data_file_path
    : the relative file path to the .scv file
    
    ------
    #### returns
    ------
    DataFrame of .scv file
    '''
    df1 = pd.read_csv(data_file_path).drop(axis=1, columns='Flag Codes')
    return df1

def save(data, name):
    '''
    save data frame to file with specified name
   
    -----
    #### params
    -----
    data - DataFrame
    : the data you wish to save
    
    name - str
    : the name without file extenstion of you want file to be named
    : the file type is of .scv
    '''
    data.to_scv(f"./../../data/processed/{name}.scv")
    


def _convertDateTime(dataFrame_col):
    '''
    convert Month-YY -> month-YYYY
    '''
    date = list()
    for time in dataFrame_col:
        f = str.split(time, '-')
        n = int(f[1])
        if (n <= 22 and n < 1000):
            n += 2000
        elif (n > 22 and n < 1000):
            n += 1900
        date.append(f"{f[0]}-{n}")
    return date


def _extract_data_by_year(df, start_year, end_year):
    '''
    extracts date range in years to and from start and end year
    and returns the filtered DataFrame
    '''
    if start_year < 1962:
        raise IndexError('smallest year possible is 1962')
    if end_year > 2022:
        raise IndexError('year is to large. largest possible year is 2022')

    df['date'] = pd.to_datetime(df['TIME'], format='%b-%Y')
    filtered_df = df[(df['date'].dt.year >= start_year)
                     & (df['date'].dt.year <= end_year)]
    filtered_df['date'] = filtered_df['date'].dt.strftime('%b-%Y')

    return filtered_df
