
# * Stores energy consumption using appropriate variables and data types
buildings = {
    "Library": 1200,
    "Admin Block": 800,
    "Hostel": 2000,
    "Cafeteria": 1500,
    "Lab Complex": 900
}
# Function to compute total and average consumption
def compute_stats(consumptions):
    total = sum(consumptions)
    average = total / len(consumptions)
    return total, average


CRITICAL_LIMIT = 5000  


consumptions = []
report = []

# Loop through buildings
for building, consumption in buildings.items():
    consumptions.append(consumption)

    # Classification using if–elif–else
    if consumption < 1000:
        status = "Energy Efficient"
    elif 1000 <= consumption < 1500:
        status = "Moderate Consumption"
    else:
        status = "Energy Intensive"

    report.append(f"{building}: {consumption} kWh → {status}")

    # Break if critical grid limit exceeded
    total_so_far = sum(consumptions)
    if total_so_far > CRITICAL_LIMIT:
        print("\nCritical grid limit exceeded! Stopping analysis...\n")
        break

# Compute total and average
total, average = compute_stats(consumptions)

# Sustainability Report
print("===== Sustainability Report =====")
for line in report:
    print(line)

print("\nSummary:")
print(f"Total Consumption: {total} kWh")
print(f"Average Consumption per Building: {average:.2f} kWh")




