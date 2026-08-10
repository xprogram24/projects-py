import pandas as pd
import numpy as np

def create_time_features(df):
    """Extract hour of day and day of week from relative TransactionDT."""
    df = df.copy()
    # 86400 seconds in a day
    df['hour'] = (df['TransactionDT'] // 3600) % 24
    df['day'] = (df['TransactionDT'] // (3600 * 24)) % 7
    return df

def create_amount_aggregated_features(df):
    """Compute relative transaction amount stats grouped by card identifier."""
    df = df.copy()
    
    # Calculate average amount spent per card1 identifier
    card_amt_mean = df.groupby('card1')['TransactionAmt'].transform('mean')
    card_amt_std = df.groupby('card1')['TransactionAmt'].transform('std').fillna(1)
    
    # Ratio and deviation features
    df['amt_to_card_mean'] = df['TransactionAmt'] / (card_amt_mean + 1e-5)
    df['amt_card_zscore'] = (df['TransactionAmt'] - card_amt_mean) / (card_amt_std + 1e-5)
    
    # Log transform amount to handle extreme skewness
    df['TransactionAmt_log'] = np.log1p(df['TransactionAmt'])
    return df

def build_feature_matrix(df):
    """Pipeline runner for feature generation."""
    print("Generating time features...")
    df = create_time_features(df)
    
    print("Generating amount aggregation features...")
    df = create_amount_aggregated_features(df)
    
    return df