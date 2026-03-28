import numpy as np

class OpNavFilter:
    """
    Extended Kalman Filter (EKF) for Artemis R Optical Navigation.
    Fuses Earth-Moon-Star triangulation data for autonomous PNT.
    """
    def __init__(self, dt=1.0):
        self.dt = dt
        # State: [x, y, z, vx, vy, vz]
        self.x = np.zeros(6)
        self.P = np.eye(6) * 1000.0  # Initial uncertainty
        
        # Process Noise
        self.Q = np.eye(6) * 0.1
        
        # Measurement Noise (Optical sensors)
        self.R = np.eye(3) * 1.0  # Position measurements from triangulation
        
    def predict(self, acceleration=np.zeros(3)):
        """Predict next state using simple Newtonian physics."""
        F = np.eye(6)
        F[0, 3] = self.dt
        F[1, 4] = self.dt
        F[2, 5] = self.dt
        
        # State Transition
        self.x = F @ self.x
        # Add acceleration (e.g. burns or gravity)
        self.x[3:6] += acceleration * self.dt
        self.x[0:3] += 0.5 * acceleration * (self.dt ** 2)
        
        # Covariance Prediction
        self.P = F @ self.P @ F.T + self.Q
        
    def update(self, z_pos):
        """Update state with optical measurement (Earth/Moon/Stars triangulation)."""
        # Measurement Matrix (H) - we only measure position directly from triangulation
        H = np.zeros((3, 6))
        H[0:3, 0:3] = np.eye(3)
        
        # Innovation
        y = z_pos - (H @ self.x)
        
        # Innovation Covariance
        S = H @ self.P @ H.T + self.R
        
        # Kalman Gain
        K = self.P @ H.T @ np.linalg.inv(S)
        
        # Update State
        self.x = self.x + (K @ y)
        
        # Update Covariance
        self.P = (np.eye(6) - (K @ H)) @ self.P
        
    def get_pnt(self):
        """Return Position, Navigation, and Timing data."""
        return {
            "position": self.x[0:3].tolist(),
            "velocity": self.x[3:6].tolist(),
            "uncertainty": np.trace(self.P)
        }

if __name__ == "__main__":
    # Simple simulation of EKF tracking
    filter = OpNavFilter(dt=1.0)
    print("Initializing OpNav EKF...")
    
    for i in range(10):
        # Simulate constant velocity movement
        true_pos = np.array([1000.0 + i*10, 500.0, 200.0])
        # Simulate noisy measurement
        noisy_measurement = true_pos + np.random.normal(0, 1.0, 3)
        
        filter.predict()
        filter.update(noisy_measurement)
        
        pnt = filter.get_pnt()
        print(f"Step {i}: Pos={pnt['position']}, Uncertainty={pnt['uncertainty']:.4f}")
