import json
import numpy as np
import os

class VerificationEngine:
    """
    Artemis R: Open-Source Verification Engine.
    Compares Artemis R simulation outcomes against Legacy Artemis I Flight Data.
    """
    def __init__(self, legacy_data_path, sim_data_path=None):
        self.legacy_data_path = legacy_data_path
        self.sim_data_path = sim_data_path
        
    def load_legacy_data(self):
        """Loads curated Artemis I legacy flight parameters."""
        with open(self.legacy_data_path, 'r') as f:
            return json.load(f)
            
    def run_verification(self, sim_data):
        """Calculates RMS error between simulation and legacy data."""
        legacy = self.load_legacy_data()
        results = {}
        
        # Phase 1: DRO Insertion Comparison
        legacy_dro = legacy["phases"]["DRO_Insertion"]
        sim_dro = sim_data.get("DRO_Insertion", {})
        
        if sim_dro:
            results["DRO_VALIDATION"] = {
                "legacy_pos_x": legacy_dro["pos_x"],
                "sim_pos_x": sim_dro["pos_x"],
                "delta_km": abs(legacy_dro["pos_x"] - sim_dro["pos_x"]),
                "integrity_status": "VALIDATED" if abs(legacy_dro["pos_x"] - sim_dro["pos_x"]) < 5.0 else "DEVIATION_DETECTED"
            }
            
        # Phase 2: Entry Interface Comparison
        legacy_ei = legacy["phases"]["Entry_Interface"]
        sim_ei = sim_data.get("Entry_Interface", {})
        
        if sim_ei:
            results["REENTRY_VALIDATION"] = {
                "legacy_angle": legacy_ei["angle_deg"],
                "sim_angle": sim_ei["angle_deg"],
                "delta_deg": abs(legacy_ei["angle_deg"] - sim_ei["angle_deg"]),
                "integrity_status": "VALIDATED" if abs(legacy_ei["angle_deg"] - sim_ei["angle_deg"]) < 0.2 else "FAIL_CORRIDOR_VERIFICATION"
            }
            
        return results

if __name__ == "__main__":
    # Mock Simulation Data for Testing
    sim_data = {
        "DRO_Insertion": { "pos_x": 71738.2, "vel_y": 0.248 },
        "Entry_Interface": { "altitude_km": 121.92, "angle_deg": -6.05 }
    }
    
    legacy_path = "artemis-r-navigation/src/mission_data/artemis_i_legacy_data.json"
    if not os.path.exists(legacy_path):
        legacy_path = "src/mission_data/artemis_i_legacy_data.json"
        
    engine = VerificationEngine(legacy_path)
    print("Artemis R: Running Open-Source Verification Suite...")
    integrity_report = engine.run_verification(sim_data)
    
    print("\n--- MISSION INTEGRITY REPORT ---")
    print(json.dumps(integrity_report, indent=4))
