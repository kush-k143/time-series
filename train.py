#Importing Libraries
import pandas as pd
from fbprophet import Prophet
import pickle

#Reading the dataset
df = pd.read_excel('Prices.xlsx', sheet_name='Daily', skiprows=8, usecols='D:E', index_col='Name')

#Preprocessing the dataset
df.rename_axis('ds',inplace=True)
df.rename(columns={'US dollar':'y'}, inplace=True)
df.reset_index(inplace=True)

prophet_model = Prophet()
prophet_model.fit(df)

#Saving the model

with open('fbprophet.pkl', 'wb') as fout: # saving the model in models directory
    pickle.dump(prophet_model, fout)