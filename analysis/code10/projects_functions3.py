import pandas as pd
def load_and_process(csv_file):
    df = pd.read_csv('./../data/raw/Inflationdataset.csv')
    return df
def clean1(df):
    df_cleaned = df.copy().drop(['INDICATOR','MEASURE','FREQUENCY', 'Flag Codes'], axis=1)
    return df_cleaned
def cleanTime(df):
    (
    df_cleaned=df.copy().drop(df_cleaned.index[6075:293470]))
    return df_cleaned
def subFood(df):
    (df_F = df.loc[df_cleaned['SUBJECT']=="FOOD"].reset_index())
    return df_F
def subEnrg(df):
    df_energy = df.loc[df_cleaned['SUBJECT'] == "ENRG"].reset_index()
    return df_energy
def subCanEnrg(df):
    df_CAN_E = (df.loc[df_cleaned['LOCATION']=="CAN"].reset_index())
    return df_CAN_E
def subTurEnrg(df):
    df_TUR_E= (df.loc[df_cleaned['LOCATION']=="TUR"].reset_index())
    return df_TUR_E
def subCanFood(df):
    df_CAN_F = (df.loc[df_cleaned['LOCATION']=="CAN"].reset_index())
    return df_CAN_F
def subTurFood(df):
    df_TUR_F = (df.loc[df_cleaned['LOCATION']=="TUR"].reset_index())
    return df_TUR_F
