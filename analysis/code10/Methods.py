
from ctypes import Union
import numpy as np
import pandas as pd


def extract_data(data: pd.DataFrame, country='CAD', data_type='ENRG', year_range=[2018, 2022]) -> pd.DataFrame:
    '''
    extracts particular data in a format of choosing

    ------
    #### COUNTRY PARAM
    ------
    ['AUS' 'AUT' 'BEL' 'CAN' 'CZE' 'DNK' 'FIN' 'FRA' 'DEU' 'GRC' 'HUN' 'ISL'
 'IRL' 'ITA' 'JPN' 'KOR' 'LUX' 'MEX' 'NLD' 'NZL' 'NOR' 'POL' 'PRT' 'SVK'
 'ESP' 'SWE' 'CHE' 'TUR' 'GBR' 'USA' 'BRA' 'CHL' 'CHN' 'EST' 'IND' 'IDN'
 'ISR' 'RUS' 'SVN' 'ZAF' 'OECD' 'OECDE' 'G-7' 'COL' 'LVA' 'SAU' 'EA19'
 'ARG' 'LTU' 'CRI' 'G-20' 'EU27_2020']

    -------
    ####  DATA TYPE PARAM
    -------
    ['ENRG' 'FOOD' 'TOT' 'TOT_FOODENRG']

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
    df: pd.DataFrame = (
        data
        .groupby('LOCATION')
        .get_group(country)
        .groupby('SUBJECT')
        .get_group(data_type)
        .set_index('FREQUENCY')
        .drop(index=[freq for freq in data['FREQUENCY'].unique() if freq != 'M'])
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


def save(data: pd.DataFrame, name):
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
    data.to_csv(f"./../data/processed/wrangled/{name}.csv")


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


def _extract_data_by_year(df: pd.DataFrame, start_year, end_year):
    '''
    extracts date range in years to and from start and end year
    and returns the filtered DataFrame
    '''
    if start_year < 1962:
        raise IndexError('smallest year possible is 1962')
    if end_year > 2022:
        raise IndexError('year is to large. largest possible year is 2022')

    df['date'] = pd.to_datetime(df['TIME'], format='%b-%Y')

    filtered_df = df.loc[(df['date'].dt.year >= start_year)
                         & (df['date'].dt.year <= end_year)]
    filtered_df['date'] = filtered_df['date'].dt.strftime('%b-%Y')

    filtered_df.drop('date', axis=1, inplace=True)
    filtered_df.reset_index(drop=True)

    return filtered_df

def dateAll(df : pd.DataFrame) -> pd.DataFrame:
    '''
    takes a dataframe and drop all none month-year dates 
    and then parses them into month-####
    
    --------
    #### params
    -------    
    df - dataFrame
    : the data frame to apply constraint
    
    ------
    #### returns
    -------
    dataframe
    '''
    df = df[df['TIME'].str.contains('M')]    
    df = df.reset_index(drop=True)
    df['TIME'] = _convertDateTime(df['TIME'])

    return df
