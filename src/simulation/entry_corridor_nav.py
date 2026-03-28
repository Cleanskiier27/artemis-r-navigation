import numpy as np

class EntryCorridorNav:
    """
    Artemis R: Earth Entry Corridor Navigation.
    Calculates trajectory from Entry Interface (EI) to Splashdown.
    Target: 121.92 km altitude @ -6.0 degrees.
    """
    def __init__(self):
        self.EI_ALTITUDE = 121.92  # km
        self.TARGET_ANGLE = -6.0   # degrees
        self.CORRIDOR_TOLERANCE = 0.5 # +/- 0.5 degrees
        
    def validate_entry(self, current_altitude, current_angle):
        """Verifies if the spacecraft is within the safe entry corridor."""
        status = "NOMINAL"
        warning = ""
        
        if current_altitude <= self.EI_ALTITUDE:
            dev = abs(current_angle - self.TARGET_ANGLE)
            if dev > self.CORRIDOR_TOLERANCE:
                status = "CRITICAL"
                warning = "ENTRY_ANGLE_DEVIATION_DETECTED"
            elif dev > 0.2:
                status = "WARNING"
                warning = "APPROACHING_CORRIDOR_LIMIT"
                
        return {
            "status": status,
            "warning": warning,
            "angle_deviation": current_angle - self.TARGET_ANGLE
        }

if __name__ == "__main__":
    nav = EntryCorridorNav()
    # Simulate a safe entry
    print("Testing Nominal Entry Interface...")
    res = nav.validate_entry(121.92, -6.1)
    print(f"Result: {res}")
    
    # Simulate a dangerous entry (too steep)
    print("\nTesting Critical Entry (Too Steep)...")
    res = nav.validate_entry(121.92, -7.2)
    print(f"Result: {res}")
