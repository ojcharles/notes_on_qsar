# a set of helper functions to keep noteboks clean
import pandas as pd
import numpy as np


def hello():
    return("hello")

def import_data():
    ###
    # returns a dataframe of hiv1 proteae inhibitor data
    ###

    
    # data cleaning - not all chembl entries are created equal
    df = pd.read_table('lib/data/2_hiv_protease.tsv')

    # some entries are missing label values
    df = df[df['Standard Value'] > 0]

    # there are duplicate values, let's get the mean Ki per smiles
    df = pd.DataFrame( df.groupby(['Smiles'])['Standard Value'].mean() )

    # now the Ki values are very diverse, let's take the log10 transform
    data = {'smiles': df['Standard Value'].index,
            'pKi': np.log10(df['Standard Value'].values)}
    df = pd.DataFrame(data)
    return df