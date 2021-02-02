import tensorflow as tf
from tensorflow import keras 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

def main():
    df = pd.read_csv('pokemon_alopez247.csv')

    df = df[['isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed','Color','Egg_Group_1','Height_m','Weight_kg','Body_Style']]

    df['isLegendary'] = df['isLegendary'].astype(int) #Convert from boolean to numerical

    #explore(df)    

    #Create dummy variables that represent type of pokemon
    #This prevents from implying any patterm or direction among the types
    df = dummy_creation(df, ['Egg_Group_1', 'Body_Style', 'Color','Type_1', 'Type_2'])

    #Split data for training and testing
    df_train, df_test = train_test_splitter(df, 'Generation')

    #To separate the labels (the 'islegendary' category) from the rest of the data.
    label = 'isLegendary'
    train_data, train_labels, test_data, test_labels = label_delineator(df_train, df_test, label)

    print('Alles gut')
    print(train_data[1])
          
def explore(df):
    print(f'Here are all the columns: {df.columns.values}')

    
    for i in df.columns.values:
        print(f'Column: {i}')
        try:
            print(f'Values: {np.unique(df[i].values)} \n')
            #print(np.unique(df.Type_2.values.astype(str))) #When TypeError: '<' not supported between instances of 'float' and 'str' appears, make all values of the same type.
        except:
            print('!!!Ups. Something\'s up with this column')
                  
def dummy_creation(df,dummy_categories):
    for i in dummy_categories:
        #create a dummy DataFrame of that category
        df_dummy = pd.get_dummies(df[i])
        #As it's a seperate DataFrame, we'll need to concatenate it to our original DataFrame
        df = pd.concat([df,df_dummy], axis=1)
        #drop original column
        df = df.drop(i,axis=1)

        return(df)

def train_test_splitter(df, column):
    #any Pokémon whose "Generation" label is equal to 1 goes into the test set
    df_train = df.loc[df[column] != 1]
    df_test = df.loc[df[column] == 1]

    df_train = df_train.drop(column, axis=1)
    df_test = df_test.drop(column, axis=1)

    return(df_train, df_test)

def label_delineator(df_train, df_test, label):
    
    train_data = df_train.drop(label, axis=1).values
    train_labels = df_train[label].values
    test_data = df_test.drop(label,axis=1).values
    test_labels = df_test[label].values
    return(train_data, train_labels, test_data, test_labels)
                           
if __name__== "__main__":
  main()

