"""
produce the following dictionary of the top employer in each country
"""

import pandas as pd
import numpy as np

f500 = pd.read_csv('f500.csv')

f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

top_employer_by_country = {}

countries = f500['country'].unique()

for c in countries:
    top_employer_by_country[c] = f500[f500['country'] == c].sort_values("employees", ascending=False).iloc[0].loc['company']

print(top_employer_by_country)


