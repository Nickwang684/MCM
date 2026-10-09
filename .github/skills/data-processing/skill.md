---
name: data-processing
description: Data processing and cleaning toolkit for handling various data formats. Use when asked to clean, transform, preprocess, or analyze data.
version: 1.0.0
---

# Data Processing Skill

## When to Use This Skill
- Loading various data formats
- Data cleaning and preprocessing
- Feature engineering
- Missing value handling
- Data transformation and normalization

## Supported Formats

| Format | Library | Function |
|--------|---------|----------|
| CSV | pandas | `pd.read_csv()` |
| Excel | pandas | `pd.read_excel()` |
| JSON | pandas | `pd.read_json()` |
| SQL | pandas | `pd.read_sql()` |
| Parquet | pandas | `pd.read_parquet()` |
| HDF5 | pandas | `pd.read_hdf()` |

## Data Cleaning Pipeline

```python
import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Standard data cleaning pipeline."""
    
    # 1. Remove duplicates
    df = df.drop_duplicates()
    
    # 2. Handle missing values
    # For numerical columns: impute with median
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    
    # For categorical columns: impute with mode
    cat_cols = df.select_dtypes(include=['object']).columns
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])
    
    # 3. Remove outliers (IQR method)
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        mask = (df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)
        df = df[mask]
    
    return df
```

## Feature Engineering

```python
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Feature engineering pipeline."""
    
    # Date features
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['dayofweek'] = df['date'].dt.dayofweek
    
    # Normalization
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    
    # One-hot encoding
    df = pd.get_dummies(df, columns=cat_cols)
    
    return df
```

## Best Practices
1. Always set random seeds for reproducibility
2. Document all transformations
3. Keep raw data unchanged
4. Validate data after each step
5. Log data quality metrics
