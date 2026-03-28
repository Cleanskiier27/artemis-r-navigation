# Artemis R Mission: Master Index

## Mission Phases
- **Phase 1: Pre-Launch / T-Minus:** Launch window calculations and real-time environment checks.
- **Phase 2: Trans-Lunar Injection (TLI):** Initial burn and Earth-Moon transit.
- **Phase 3: Lunar Capture & Orbit (DRO/NRHO):** Establishing a stable lunar orbit.
- **Phase 4: Moon Operations:** Real-time spatial awareness and mission telemetry.
- **Phase 5: Trans-Earth Injection (TEI):** Escape burn and return trajectory.
- **Phase 6: Re-entry & Recovery:** Earth atmosphere skip entry and landing.

## Data Streams
- **Telemetry Relay:** `src/server/mission_relay_server.js` (Simulated or Live NASA API).
- **Spatial Awareness Dashboard:** `src/server/dashboard_api.js`.
- **Live NASA Streams:** 
    - [NASA TV Live](https://www.nasa.gov/nasatv)
    - [Artemis I Real-Time Data (Archival Example)](https://www.nasa.gov/specials/trackartemis/)

## Master Target (Destination)
- **Primary:** Moon (Lunar Orbit)
- **Secondary:** Earth (Safe Return)
