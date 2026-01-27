# Renewable Energy Decision Engine: A smart grid integrates solar, wind, and hydro energy sources.

# Task:
# * Using Object-Oriented Programming:
# * Create a base class EnergySource done
# * Derive subclasses for Solar, Wind, and Hydro

# Implement:
# * Encapsulation for power output
# * Inheritance for shared behavior
# * Polymorphism for calculating energy availability
# * Use conditional logic to decide which source to prioritize
# * Simulate energy allocation using loops

import random
# Base Class
class EnergySource:
    def __init__(self, name):
        self._name = name           # protected attributes 
        self._power_output = 0     

    def generate_power(self):
        """Polymorphism for calculating energy availability"""
        

    def get_power_output(self):
        """Encapsulation for power output"""
        return self._power_output

    def __str__(self):
        return f"{self._name}: {self._power_output:.2f} kWh"


# Subclasses for solar wind and hydro
class Solar(EnergySource):
    def __init__(self):
        super().__init__("Solar")

    def generate_power(self):
        # Simulate solar output depending on sunlight (0–1000 kWh)
        self._power_output = random.uniform(200, 1000)


class Wind(EnergySource):
    def __init__(self):
        super().__init__("Wind")

    def generate_power(self):
        # Simulate wind output depending on wind speed (0–800 kWh)
        self._power_output = random.uniform(100, 800)


class Hydro(EnergySource):
    def __init__(self):
        super().__init__("Hydro")

    def generate_power(self):
        # Simulate hydro output depending on water flow (500–1200 kWh)
        self._power_output = random.uniform(500, 1200)


# Decision Engine
def prioritize_source(sources):
    """Conditional logic to decide which source to prioritize"""
    # Choosethe source with maximum power output
    best_source = max(sources, key=lambda s: s.get_power_output())
    return best_source


def simulate_energy_allocation(iterations=5):
    solar = Solar()
    wind = Wind()
    hydro = Hydro()

    for i in range(iterations):
        print(f"\n--- Simulation Round {i+1} ---")

        # Generate power for each source
        solar.generate_power()
        wind.generate_power()
        hydro.generate_power()

        # Print outputs
        print(solar)
        print(wind)
        print(hydro)

        # Decide priority
        best = prioritize_source([solar, wind, hydro])
        print(f" Prioritized Source: {best._name} with {best.get_power_output():.2f} kWh")



simulate_energy_allocation(5)