import pandas as pd
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df=pd.read_csv(url_or_path_to_csv_file)
    dfclean=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).reset_index(drop=True)
    df_time_int=pd.to_numeric(dfclean["TIME"])
    dfclean["TIME"]=df_time_int
   

      

    # Method Chain 2 (Create new columns, drop others, and do processing)


    # Make sure to return the latest dataframe
    return dfclean


   

def load_ENRG(df):
    dfenergy=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).loc[df['SUBJECT'] == "ENRG"].reset_index(drop=True)
    df_time_int=pd.to_numeric(dfenergy["TIME"])
    dfenergy["TIME"]=df_time_int
    return dfenergy


def load_FOOD(df):
    dffood=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).loc[dfclean['SUBJECT'] == "FOOD"].reset_index(drop=True)
    df_time_int=pd.to_numeric(dffood["TIME"])
    dffood["TIME"]=df_time_int
    return dffood


def load_TOT(df):
    dftot=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).loc[dfclean['SUBJECT'] == "TOT"].reset_index(drop=True)
    df_time_int=pd.to_numeric(dftot["TIME"])
    dftot["TIME"]=df_time_int
    return dftot

