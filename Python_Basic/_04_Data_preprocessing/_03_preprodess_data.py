import pandas as pd
import numpy as np
data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}

# Create a DataFrame

energy_df = pd.DataFrame(data)
print(energy_df)

# checking if null value exist
# print(energy_df.isnull())
# print(energy_df.isnull().sum())

# deleting the data 
cleaned_df = energy_df.dropna(axis=0)
# print("\n Cleaned dataframe : ")
# print(cleaned_df)


# impute missing values with the mean 

ec_m = energy_df["Energy Consumption (MWh)"].mean()
c_m = energy_df["Cost (Million $)"].mean()
# print("mean of energy consumption : ",ec_m)
# print("mean of cost : ",c_m)

# impute missing values in energy consumption with mean
energy_df["Energy Consumption (MWh)"] = energy_df["Energy Consumption (MWh)"].fillna(ec_m)
# energy_df["Energy Consumption (MWh)"].fillna(ec_m, inplace=True)

# impute missing values in cost with mean
# energy_df["Cost (Million $)"].fillna(c_m, inplace=True)

energy_df["Cost (Million $)"] = energy_df["Cost (Million $)"].fillna(c_m)









energy_df = pd.DataFrame(data)
# forward filling and backward filling 

forward_filled_df = energy_df.ffill()
backward_filled_df = energy_df.bfill()
print("\n Data after forwrard filling : ")

print(forward_filled_df)
backward_filled = energy_df["Cost (Million $)"].fillna(method="bfill")

print("\n Data after backward filling : ")
print(backward_filled_df)









