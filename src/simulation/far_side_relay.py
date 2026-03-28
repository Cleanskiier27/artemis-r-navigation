import numpy as np
import json
import time
import os

class FarSideRelaySim:
    """
    Artemis R: Lunar Far Side Navigation & Relay Simulation.
    Models PNT (Position, Navigation, Timing) data sharing per OST Article XI.
    """
    def __init__(self):
        self.relay_pos = np.array([0.0, 0.0, 65000.0]) # L2 Lagrange Point approx
        self.lander_pos = np.array([1737.4, 0.0, 0.0]) # Far side surface
        
    def generate_navigation_frame(self):
        """Generates a 'Live' navigation frame for the far side."""
        # Add orbital drift
        self.relay_pos += np.random.normal(0, 0.05, 3)
        
        frame = {
            "source": "QUEQIAO-REDUNDANT-RELAY",
            "compliance": "ARTEMIS-ACCORDS-SECTION-8",
            "legal_basis": "OST-ARTICLE-XI",
            "telemetry": {
                "relay_coords": self.relay_pos.tolist(),
                "signal_latency_ms": 1.25,
                "radio_quiet_zone_status": "PROTECTED"
            },
            "timestamp": time.time()
        }
        return frame

    def archive_frame(self, frame):
        """Saves frame to the International Open Data Archive."""
        filename = f"mission_archive/FAR_SIDE_NAV_{int(frame['timestamp'])}.json"
        # Adjusted path for script location
        archive_path = os.path.join(os.getcwd(), "artemis-r-navigation", filename)
        # Check if running inside artemis-r-navigation or root
        if "artemis-r-navigation" in os.getcwd():
            archive_path = filename
            
        with open(archive_path, 'w') as f:
            json.dump(frame, f, indent=4)
        print(f"[ARCHIVE] Far Side Navigation Frame Persisted: {filename}")

if __name__ == "__main__":
    sim = FarSideRelaySim()
    print("Initializing Lunar Far Side Navigation Stream (Open Data Compliance)...")
    for _ in range(3):
        frame = sim.generate_navigation_frame()
        sim.archive_frame(frame)
        time.sleep(1)
