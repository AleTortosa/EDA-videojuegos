import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the videogames dataset:
    - Fill missing Publisher values with 'Unknown'
    - Remove rows with missing Year values
    - Convert Year to integer
    """
    df = df.copy()
    
    # Fill missing Publisher values
    df['Publisher'] = df['Publisher'].fillna('Unknown')
    
    # Remove rows with missing Year values
    df = df.dropna(subset=['Year'])
    
    # Convert Year to integer
    df['Year'] = df['Year'].astype(int)
    
    return df
