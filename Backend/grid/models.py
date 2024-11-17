# models.py
class EnergyManagementSystem:
    def __init__(self):
        self.battery_level = 80  # Assume battery is at 80% for initialization
        self.grid_connected = True

    def manage_energy_sharing(self, energy_to_share):
        if self.battery_level > 20 and self.grid_connected:  # Ensure battery retains some charge
            self.battery_level -= energy_to_share
            return f"Shared {energy_to_share}% energy with the grid."
        return "Insufficient battery level or grid is not available."

    def get_battery_status(self):
        return self.battery_level
