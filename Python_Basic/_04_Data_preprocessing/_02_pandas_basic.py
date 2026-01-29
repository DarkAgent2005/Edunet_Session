import pandas as pd

renewable_sources = ["wind","solar","hydro","biomass","geothermal","nuclear","other_renewable","other_fossil"]

renewable_sources = pd.Series(renewable_sources)

print("Renewable Energy Sources : ")
# print(renewable_sources)

renewable_sources = ["Solar", "Wind", "Hydropower",  "Geothermal", "Biomass"]

data = {
    "Project": ["Solar Farm A", "Wind Turbine X", "Hydropower Y", "Solar Roof Z", "Geothermal Plant P"],
    "Technology": ["Solar", "Wind", "Hydropower", "Solar", "Geothermal"],
    "Capacity (MW)": [150, 300, 200, 50, 100],  # Megawatts
    "Cost (Million $)": [200, 400, 350, 100, 250],  # Project cost
    "Location": ["California", "Texas", "Washington", "Nevada", "Idaho"],
    "Completion Year": [2023, 2024, 2022, 2025, 2023]
}

# Create a DataFrame
projects_df = pd.DataFrame(data)

# print(projects_df)

# print("\n Green Technology projects dataframe : ")
# print(projects_df.head(3))

# print(projects_df.tail(2))

# print(projects_df[3:5])

# print(projects_df.dtypes)

# print(projects_df.shape)

# print(projects_df.index)

# print(projects_df.size)

# print(projects_df.info)

# print(projects_df.columns)

# print(projects_df.describe())

# print(projects_df.isnull())

# print(projects_df.isnull().sum())



# print(projects_df[["Project", "Capacity (MW)"]])

# print(projects_df.iloc[:3, 1:4])

# filter the projects_df based on capacity > 100 mw
high_capacity_projects_df = projects_df[projects_df["Capacity (MW)"] > 100]
# print("\n High capacity projects with capacity greater than 100 MW : ")
# print(high_capacity_projects_df)

# feature engineering 

projects_df["Cost per MW"] = projects_df["Cost (Million $)"] / projects_df["Capacity (MW)"]
# print("\n Projects dataframe with cost per MW : ")
# print(projects_df.head(3))

# Aggregation = sum mean mod 


