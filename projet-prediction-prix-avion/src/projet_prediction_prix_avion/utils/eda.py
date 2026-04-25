import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

def univ_analysis_discrete(df, col_name, max_unique=20):
    """_summary_
    Analyse une variable catégorielle

    Args:

        df (df): DataFrame contennant les données.
        col_name (str): Nom de la colonne à analyser
        max_unique (int, optional): Nombre maximum de modalités à afficher si la variable à trop de catégorie. 
        Defaults to 20.
    """
    print(f"\n===={col_name}===")
    print(df[col_name].describe())
    
    #bar plot
    plt.figure(figsize=(10,5))
    if df[col_name].nunique() <= max_unique:
        df[col_name].value_counts().plot(kind='bar')
        plt.title(f"Distribution of {col_name}")
        plt.xlabel(col_name)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
    else:
        df[col_name].value_counts().nlargest(max_unique).plot(kind='bar')
        plt.title(f"Distribution of {col_name}")
        plt.xlabel(col_name)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
    plt.show()

def univ_analysis_continue(df, col_name, nbins=30):
    """_summary_
    Analyse une variable continue

    Args:
        df (df): DataFrame contenant les données
        col_name (str): Nom de la colonne à analyser
        nbins (int, optional): _description_. Defaults to 30.
    """
    print(f"\n/----{col_name}----/")
    display(df[col_name].describe())
    
    #box plot and histogram
    
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    df[col_name].plot(kind="box")
    plt.title(f"Distribution {col_name}")
    # plt.xlabel(col_name)
    plt.ylabel("Count")
    plt.subplot(1,2,2)
    df[col_name].hist(bins=nbins)
    plt.title(f"Histograme pour {col_name}")
    plt.xlabel(col_name)
    plt.ylabel("Fréquence")
    plt.tight_layout()
    plt.show()