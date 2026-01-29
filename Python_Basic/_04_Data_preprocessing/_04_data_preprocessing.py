import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}
# print(data)

# Create a DataFrame

energy_df = pd.DataFrame(data)
print(energy_df)
ec_m = energy_df["Energy Consumption (MWh)"].mean()
c_m = energy_df["Cost (Million $)"].mean()
energy_df["Energy Consumption (MWh)"] = energy_df["Energy Consumption (MWh)"].fillna(ec_m)
energy_df["Cost (Million $)"] = energy_df["Cost (Million $)"].fillna(c_m)

scaler = MinMaxScaler()

energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]] = scaler.fit_transform(
    energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]]
)

# print("\n Data after normalization : ")
# print(energy_df)


# min max when we kno range
# standard scaler used when we don't know the range 

scalar = StandardScaler()

# print("\n Data after standard scaler : ")
energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]] = scalar.fit_transform(
    energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]]
)
# print(energy_df)

# one bot encode the energy source column 
energy_encoded_df = pd.get_dummies(energy_df,columns=["Energy Source"])

print("\n Data after one hot encoding : ")
print(energy_encoded_df)


