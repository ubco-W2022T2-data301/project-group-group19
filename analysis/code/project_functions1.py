Class project_funtions1: 
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .rename(...)
          .dropna(...)
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(...)
      )

    # Make sure to return the latest dataframe

    return df2 

def load_clean(path):
    df = pd.read_csv(path)
    dfclean=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).reset_index(drop=True)
    df_time_int=pd.to_numeric(dfclean["TIME"])
    dfclean["TIME"]=df_time_int
    return dfclean
path ='./../data/raw/Inflationdataset.csv'
load_clean(path)

def load_ENRG(path):
    df = pd.read_csv('./../data/raw/Inflationdataset.csv')
    dfenergy=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).loc[df['SUBJECT'] == "ENRG"].reset_index(drop=True)
    df_time_int=pd.to_numeric(dfenergy["TIME"])
    dfenergy["TIME"]=df_time_int
    return dfenergy
path ='./../data/raw/Inflationdataset.csv'
load_clean(path)

def load_FOOD(path):
    df = pd.read_csv('./../data/raw/Inflationdataset.csv')
    dffood=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).loc[dfclean['SUBJECT'] == "FOOD"].reset_index(drop=True)
    df_time_int=pd.to_numeric(dffood["TIME"])
    dffood["TIME"]=df_time_int
    return dffood
path ='./../data/raw/Inflationdataset.csv'
load_clean(path)

def load_TOT(path):
    df = pd.read_csv('./../data/raw/Inflationdataset.csv')
    dftot=df.drop(columns=["Flag Codes", "FREQUENCY","INDICATOR", "MEASURE"]).drop(df.index[6075:293470]).loc[dfclean['SUBJECT'] == "TOT"].reset_index(drop=True)
    df_time_int=pd.to_numeric(dftot["TIME"])
    dftot["TIME"]=df_time_int
    return dftot
path ='./../data/raw/Inflationdataset.csv'
load_clean(path)
