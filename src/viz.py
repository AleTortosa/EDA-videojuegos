import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(df: pd.DataFrame) -> None:
    """
    Generate key visualizations for the videogames dataset.
    """
    # Set style
    sns.set_style('whitegrid')
    # Histogram

    df[df['EU_Sales'] < 1]['EU_Sales'].hist(bins=30)

    plt.title('Distribución de ventas en Europa (< 1M)')
    plt.xlabel('Ventas en Europa (millones)')
    plt.ylabel('Número de juegos')
    plt.show()

    # Boxplot

    df.boxplot(column='Year')

    plt.title('Boxplot de años de salida de videojuegos')
    plt.ylabel('Año de salida')
    plt.show()

    plt.figure(figsize=(10,5))
    df['Genre'].value_counts().plot(kind='bar')

    plt.title('Distribución de géneros')
    plt.xlabel('Género')
    plt.ylabel('Número de juegos')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df,
                    x='NA_Sales', 
                    y='EU_Sales', 
                    hue='Genre')
    plt.title('NA_Sales vs EU_Sales')
    plt.xlabel('NA Sales (millones)')
    plt.ylabel('EU Sales (millones)')
    plt.tight_layout()
    plt.show()

    corr = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
    plt.title('Correlación entre variables numéricas')
    plt.show()
        
    print('\nVisualizaciones completadas.')
