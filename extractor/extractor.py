import pandas as pd

df = pd.read_csv("212_Sample.csv")

# Todo: Write function to filter CSV
# - Remove unused columns (ISIN, Exchange Rate, Currency Result, <All rows after total>)
df = df.drop(columns=['ISIN', 'Exchange rate', 'Currency (Result)', 'Currency (Total)',  'Withholding tax', 'Currency (Withholding tax)',  'Charge amount', 'Currency (Charge amount)', 'ID', 'Currency conversion fee', 'Currency (Currency conversion fee)'])
# - Remove lines for funds added & interest added
market_df = df[df["Action"].str.contains("Market")]
# - Remove lines for dividens to separate dataframe
dividen_df = df[df["Action"].str.contains("Dividend")]
# - Remove lines containing GBX to separate dataframe
gbx_only = market_df[market_df["Currency (Price / share)"].str.contains("GBX")]
index_list = gbx_only.index.values.tolist()
no_gbx = market_df.drop(index_list)

# Todo: Write function to write out new CSV containing dividens, GBX, main CSV
no_gbx.to_csv('results/212/buysell_1.csv', index=False)
dividen_df.to_csv('results/212/dividen-deposit.csv', index=False)
gbx_only.to_csv('results/212/buysell_100.csv', index=False)