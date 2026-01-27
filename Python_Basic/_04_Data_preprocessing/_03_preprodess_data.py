import pandas as pd
import numpy as np
data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}

# Create a DataFrame
energy_df = pd.DataFrame(data)

# checking if null value exist
print(energy_df.isnull())
print(energy_df.isnull().sum())

cleaned_df = energy_df.dropna(axis=0)
print("\n Cleaned dataframe : ")
print(cleaned_df)


# impute missing values with the mean 
energy_df["energy consumption (MWH)"].fillna(ec_m,inplace=True)

energy_df["Cost (Million $)"].fillna(c_m,inplace=True)

# Tod







