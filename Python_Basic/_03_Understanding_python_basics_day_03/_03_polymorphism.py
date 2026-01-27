# same fucntion name but different behaviour is polymorphism
class Energysystem: 
    def __init__(self,building_name,energy_consumption,emission_factor):
        # initial attribute
        self.building_name=building_name
        self._energy_consumption=energy_consumption # protected attribute
        self._emission_factor=emission_factor # protected attribute
    def calculate_carbon_footprint(self):
        return self.energy_consumption * self.emission_factor

class SolarEnergySystem(Energysystem):
    def __init__(self,building_name,energy_consumption,emission_factor,solar_production):
        super().__init__(building_name,energy_consumption,emission_factor)
        self.solar_production=solar_production

    def calculate_carbon_footprint(self):
        net_consumption=self._energy_consumption - self.solar_production
        return net_consumption * self._emission_factor
    
solar_building = SolarEnergySystem("Building A",5000,0.45,2000)
carbon_footprint = solar_building.calculate_carbon_footprint()

print(f"Adjusted carbon footprint (after solar production ) : {carbon_footprint:.2f} kg CO2 per year")

