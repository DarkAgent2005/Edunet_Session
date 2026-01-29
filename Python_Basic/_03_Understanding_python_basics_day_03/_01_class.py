# oops in python 

class Energysystem: 
# _init_() is used to build or set up your object when you create it 
    def __init__(self,building_name,energy_consumption,emission_factor):
        # initial attribute
        self.building_name=building_name
        self.energy_consumption=energy_consumption
        self.emission_factor=emission_factor

building_01 = Energysystem("building_01",1000,0.475)
print(f"building name is {building_01.building_name} and energy consuption is {building_01.energy_consumption} Emission factor is {building_01.emission_factor}")

def calculate_carbon_footprint(self):
    return self.energy_consumption * self.emission_factor

def energy_saving (self):
    return self.energy_consumption * 0.10

print(f"Carbon Footprint is  : {calculate_carbon_footprint(building_01)}")
print(f"Energy consumption is :  {energy_saving(building_01)}")

# Inheritance 

# super().__init__ is used to inherit properties from the parent class

class SolarEnergySystem(Energysystem):
    def __init__(self,building_name,energy_consumption,emission_factor,solar_production):
        super().__init__(building_name,energy_consumption,emission_factor)
        self.solar_production=solar_production

    def net_energy_consumption(self):
        return self.energy_consumption - self.solar_production
# building_01=SolarEnergySystem(500)

solar_building_01 = SolarEnergySystem("solar_building_01",5000,0.45,1500)
print(f"Building name is {solar_building_01.building_name} and net energy consumption is {solar_building_01.net_energy_consumption()}")
