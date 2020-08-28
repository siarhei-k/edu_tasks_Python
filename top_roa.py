"""
find the company with the highest ROA from each sector
"""

import pandas as pd
import numpy as np

f500 = pd.read_csv('f500.csv')

f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500['roa'] = f500['profits'] / f500['assets']

top_roa_by_sector = {}


sectors = f500['sector'].unique()

for s in sectors:
    top_roa_by_sector[s] = f500[f500['sector'] == s].sort_values('roa', ascending=False).iloc[0].loc['company']

print(top_roa_by_sector)