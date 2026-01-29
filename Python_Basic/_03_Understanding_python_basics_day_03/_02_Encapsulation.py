class Energysystem: 
# _init_() is used to build or set up your object when you create it 
    def __init__(self,building_name,energy_consumption,emission_factor):
        # initial attribute
        self.building_name=building_name
        self._energy_consumption=energy_consumption # protected attribute
        self._emission_factor=emission_factor # protected attribute

    def get_energy_consuption(self):
        return self._energy_consumption
    
    def calculate_carbon_footprint(self):
        return self._energy_consumption * self._emission_factor
    
building = Energysystem("Building A",5000,0.45)
print(f"Building name is {building.building_name} and energy consumption is {building.get_energy_consuption()}")
