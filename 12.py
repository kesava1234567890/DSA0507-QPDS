import pandas as pd
import numpy as np

# Create a DataFrame with random values
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

# Introduce some NaN values
df.loc[2:4, 'A'] = np.nan
df.loc[5:7, 'C'] = np.nan

# Function to highlight NaN values
def highlight_nan(value):
    if pd.isna(value):
        return 'background-color: yellow'
    else:
        return ''

# Apply the highlight function to the DataFrame using Styler.map
styled_df = df.Stylermap(highlight_nan)

# Display the styled DataFrame
styled_df
