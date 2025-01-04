import pandas as pd
import os

# Load CMS data (example: NH_ProviderInfo.csv)
cms_provider_info = pd.read_csv('data/NH_ProviderInfo_Nov2024.csv')

# Load cost of living data
col_data = pd.read_csv('data/cost_of_living_data.csv')

# Load minimum wage data
min_wage_data = pd.read_csv('data/min_wage.csv')

# Load BLS earnings data
bls_data = pd.read_csv('data/bls_earnings_2023.csv')