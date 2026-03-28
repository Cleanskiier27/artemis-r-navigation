# Master Target: Moon & Earth Return

## Target: Moon (Lunar Orbit)
- **Target Orbit:** Distant Retrograde Orbit (DRO) or Near Rectilinear Halo Orbit (NRHO).
- **Altitude (DRO):** ~70,000 km.
- **Altitude (NRHO):** Perilune 3,000 km / Apolune 70,000 km.
- **Gravity Model:** Moon-J2-LOD (Lunar Orientation Data).
- **Orbital Velocity:** Approx. 0.9 - 1.2 km/s (Lunar Reference Frame).

## Target: Earth (Safe Return)
- **Return Trajectory:** Trans-Earth Injection (TEI).
- **Entry Velocity:** Approx. Mach 32 (39,000+ km/h).
- **Entry Angle:** -5.5 to -6.5 degrees (Skip Entry Corridor).
- **Heat Shield Limit:** 2,700°C (Avcoat Phenolic Epoxy).
- **Splashdown Window:** Pacific Ocean, 33°N / 118°W.

## Constraints
- **Pilot Input:** Immutable once TLI burn is initiated.
- **Spatial Awareness:** Redundant PNT from Earth-Star-Moon optical triangulation.
- **Sim-Validation:** Return trajectory must be 100% pre-validated by `src/simulation/return_trajectory.py`.
