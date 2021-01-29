import tensorflow as tf
from tensorflow import keras 
import numpy as no
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

def main():
    df = pd.read_csv('pokemon_alopez247.csv')

    df = df[['isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed','Color','Egg_Group_1','Height_m','Weight_kg','Body_Style']]

    df['isLegendary'] = df['isLegendary'].astype(int) #Convert from boolean to numerical

    #Create dummy variables that represent type of pokemon
    #This prevents from implying any patterm or direction among the types
    df = dummy_creation(df, ['Egg_Group_1', 'Body_Style', 'Color','Type_1', 'Type_2'])

def dummy_creation(df,dummy_categories):
    for i in dummy_categories:
        #create a dummy DataFrame of that category
        df_dummy = pd.get_dummies(df[i])
        #As it's a seperate DataFrame, we'll need to concatenate it to our original DataFrame
        df = pd.concat([df,df_dummy], axis=1)
        #drop original column
        df = df.drop(i,axis=1)

        return(df)
                           
if __name__== "__main__":
  main()

