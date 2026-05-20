import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build new features from existing columns:
    - Aggregate duplicate games by Name (sum sales, combine platforms)
    - Calculate sales coverage ratio
    """
    
    # Aggregate by game name to handle duplicates across platforms
    df_clean = df.copy().groupby('Name', as_index=False).agg({
        'Platform': lambda x: ', '.join(sorted(x.unique())),
        'Genre': 'first',
        'Publisher': 'first',
        'Year': 'first',
        'NA_Sales': 'sum',
        'EU_Sales': 'sum',
        'JP_Sales': 'sum',
        'Other_Sales': 'sum',
        'Global_Sales': 'sum'
    })
    
    return df_clean