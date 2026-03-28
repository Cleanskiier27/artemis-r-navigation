# Artemis R Navigation System

## Overview
Open-source spatial awareness and navigation system for the Artemis R mission. This repository implements realistic lunar orbital mechanics, multi-sensor fusion (IMU, Star Tracker, Optical Navigation), and immutable flight control logic to ensure a safe moon-to-earth trajectory, mitigating human error through simulation-validated paths.

## Mission Architecture
- **Target:** Moon (DRO/NRHO) and return to Earth.
- **Goal:** Spatial awareness for aircraft/spacecraft with pilot controls locked based on validated simulation outcomes.
- **Redundancy:** Multi-language (Python, C++, Node.js) sensor fusion and simulation layers.

## Tech Stack
- **Python:** Extended Kalman Filters (EKF), Orbital Mechanics Simulation.
- **C++:** High-rate IMU processing, Immutable Control Logic.
- **Node.js:** Real-time telemetry relay and dashboard APIs.

## Open Source
The spatial awareness element of the aircraft is open-sourced under the MIT License.
