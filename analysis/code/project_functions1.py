{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efba4559-3ca2-4912-8706-efd62579ec00",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import matplotlib.axes as ax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58c80728-4eea-4386-96a2-e15d732805d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_clean(path):\n",
    "    df = pd.read_csv(path)\n",
    "    dfclean=df.drop(columns=[\"Flag Codes\", \"FREQUENCY\",\"INDICATOR\", \"MEASURE\"]).drop(df.index[6075:293470]).reset_index(drop=True)\n",
    "    df_time_int=pd.to_numeric(dfclean[\"TIME\"])\n",
    "    dfclean[\"TIME\"]=df_time_int\n",
    "    return dfclean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a44ccd42-283c-4845-9cec-311057b9d9e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_ENRG(path):\n",
    "    df = pd.read_csv('./../data/raw/Inflationdataset.csv')\n",
    "    dfenergy=df.drop(columns=[\"Flag Codes\", \"FREQUENCY\",\"INDICATOR\", \"MEASURE\"]).drop(df.index[6075:293470]).loc[df['SUBJECT'] == \"ENRG\"].reset_index(drop=True)\n",
    "    df_time_int=pd.to_numeric(dfenergy[\"TIME\"])\n",
    "    dfenergy[\"TIME\"]=df_time_int\n",
    "    return dfenergy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c46538a1-c250-4aa5-b0d6-8e20fac3f760",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_FOOD(path):\n",
    "    df = pd.read_csv('./../data/raw/Inflationdataset.csv')\n",
    "    dffood=df.drop(columns=[\"Flag Codes\", \"FREQUENCY\",\"INDICATOR\", \"MEASURE\"]).drop(df.index[6075:293470]).loc[dfclean['SUBJECT'] == \"FOOD\"].reset_index(drop=True)\n",
    "    df_time_int=pd.to_numeric(dffood[\"TIME\"])\n",
    "    dffood[\"TIME\"]=df_time_int\n",
    "    return dffood"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71516c0f-83aa-4c44-be40-fd640eff3f77",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_TOT(path):\n",
    "    df = pd.read_csv('./../data/raw/Inflationdataset.csv')\n",
    "    dftot=df.drop(columns=[\"Flag Codes\", \"FREQUENCY\",\"INDICATOR\", \"MEASURE\"]).drop(df.index[6075:293470]).loc[dfclean['SUBJECT'] == \"TOT\"].reset_index(drop=True)\n",
    "    df_time_int=pd.to_numeric(dftot[\"TIME\"])\n",
    "    dftot[\"TIME\"]=df_time_int\n",
    "    return dftot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b927d00-0231-459b-a9e2-43b7d5f9ef74",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data and deal with missing data)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv(url_or_path_to_csv_file)\n",
    "          .rename(...)\n",
    "          .dropna(...)\n",
    "          # etc...\n",
    "      )\n",
    "\n",
    "    # Method Chain 2 (Create new columns, drop others, and do processing)\n",
    "\n",
    "    df2 = (\n",
    "          df1\n",
    "          .assign(...)\n",
    "      )\n",
    "\n",
    "    # Make sure to return the latest dataframe\n",
    "\n",
    "    return df2 \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
