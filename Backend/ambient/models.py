# models.py
class AmbientControlSystem:
    def __init__(self):
        self.lighting_color = 'Warm White'  # Default lighting
        self.temperature = 22  # Default temperature (Celsius)
        self.audio_volume = 5  # Default audio volume level

    def set_lighting(self, color):
        self.lighting_color = color
        return f"Lighting set to {color}."

    def set_temperature(self, temp):
        self.temperature = temp
        return f"Temperature set to {temp}°C."

    def set_audio_volume(self, volume):
        self.audio_volume = volume
        return f"Audio volume set to {volume}."
