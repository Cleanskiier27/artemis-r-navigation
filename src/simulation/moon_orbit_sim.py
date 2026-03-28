import numpy as np
import matplotlib.pyplot as plt

class MoonOrbitSim:
    """
    Artemis R: Lunar Orbit Simulation (Distant Retrograde Orbit - DRO)
    Models the spacecraft trajectory around the Moon.
    """
    def __init__(self):
        # Constants
        self.MU_MOON = 4902.800066  # Lunar gravitational parameter (km^3/s^2)
        self.MU_EARTH = 398600.4418 # Earth gravitational parameter (km^3/s^2)
        self.R_MOON = 1737.4        # Lunar radius (km)
        self.D_EARTH_MOON = 384400.0 # Earth-Moon distance (km)
        
    def simulate_dro(self, initial_state, duration_days=28, dt=60):
        """
        Simulate a Distant Retrograde Orbit using the Circular Restricted Three-Body Problem (CR3BP).
        For simplicity, this version uses basic Newtonian model in Moon-centric frame.
        """
        steps = int(duration_days * 24 * 3600 / dt)
        trajectory = np.zeros((steps, 6))
        trajectory[0] = initial_state
        
        for i in range(1, steps):
            r = trajectory[i-1, 0:3]
            v = trajectory[i-1, 3:6]
            
            # Gravitational force from Moon
            r_norm = np.linalg.norm(r)
            a_moon = -self.MU_MOON * r / (r_norm**3)
            
            # Simplified Earth Perturbation (Third body effect)
            # Placeholder for full CR3BP dynamics
            a_total = a_moon 
            
            # Euler-Cromer Integration
            v_next = v + a_total * dt
            r_next = r + v_next * dt
            
            trajectory[i, 0:3] = r_next
            trajectory[i, 3:6] = v_next
            
        return trajectory

if __name__ == "__main__":
    sim = MoonOrbitSim()
    print("Simulating Artemis R Moon Orbit (DRO)...")
    
    # DRO State (Approximate: 70,000 km altitude)
    initial_pos = np.array([71737.4, 0.0, 0.0])
    initial_vel = np.array([0.0, 0.25, 0.0])  # ~0.25 km/s retrograde
    initial_state = np.concatenate([initial_pos, initial_vel])
    
    traj = sim.simulate_dro(initial_state, duration_days=7)
    
    # Simple output
    print(f"Simulation Complete. Final position: {traj[-1, 0:3]}")
    
    # Plotting code (Optional)
    plt.figure(figsize=(8,8))
    plt.plot(traj[:,0], traj[:,1], label='DRO Trajectory')
    plt.scatter(0, 0, color='grey', label='Moon')
    plt.xlabel('X (km)')
    plt.ylabel('Y (km)')
    plt.title('Artemis R: Distant Retrograde Orbit (DRO) Simulation')
    plt.legend()
    plt.axis('equal')
    # plt.show() # Disabled for headless CLI
    print("Plot generated successfully.")
