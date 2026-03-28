const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

/**
 * Artemis R: Mission Relay Server
 * Simulates real-time telemetry data streaming from the lunar orbit.
 */

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const PORT = process.env.PORT || 3000;

// Middleware for static files
app.use(express.static('public'));

// Simulated Telemetry Source
let mission_status = {
    phase: "Lunar Capture",
    position: { x: 71737.4, y: 15.2, z: -2.3 },
    velocity: { x: 0.1, y: 0.25, z: 0.01 },
    pnt_uncertainty: 0.0045,
    pilot_lock: true,
    mission_duration: "T-PLUS 00:04:12:45",
    telemetry_mode: "O2O_HIGH_BITRATE",
    bitrate_mbps: 260.0,
    live_cam_override: false,
    live_feed_url: "https://www.youtube.com/embed/21X5lGlDOfg?autoplay=1&mute=1",
    biometrics: {
        crew_1: { pulse: 72, oxygen: 98, stress: "LOW" },
        crew_2: { pulse: 75, oxygen: 99, stress: "LOW" },
        crew_3: { pulse: 68, oxygen: 98, stress: "LOW" },
        crew_4: { pulse: 80, oxygen: 97, stress: "NOMINAL" }
    },
    propulsion: {
        engine_status: "ACTIVE",
        fuel_level: 88.4,
        cam_status: "16/16 ONLINE"
    },
    warnings: [],
    data_source: "Live-Simulation-Bridge"
};

// Update Telemetry Every Second
setInterval(() => {
    // Add small random noise to simulate real-time sensors
    mission_status.position.x += (Math.random() - 0.5) * 0.1;
    mission_status.position.y += (Math.random() - 0.5) * 0.1;
    mission_status.velocity.y += (Math.random() - 0.5) * 0.01;
    
    // Update Biometrics
    mission_status.biometrics.crew_1.pulse = 70 + Math.floor(Math.random() * 5);
    mission_status.biometrics.crew_4.pulse = 78 + Math.floor(Math.random() * 10);
    
    // Critical Warning Simulation (Example: Random Radiation Spike)
    if (Math.random() > 0.98) {
        mission_status.warnings.push("RAD_SPIKE_DETECTED");
        setTimeout(() => { mission_status.warnings = []; }, 5000);
    }

    // Broadcast to all connected clients (Dashboard/Sim)
    io.emit('telemetry', mission_status);
}, 1000);

io.on('connection', (socket) => {
    console.log('[RELAY] New Mission Control Dashboard connected.');
    socket.emit('telemetry', mission_status);
});

app.get('/status', (req, res) => {
    res.json(mission_status);
});

server.listen(PORT, () => {
    console.log(`[RELAY] Artemis R Mission Data Relay active on port ${PORT}`);
    console.log(`[RELAY] Telemetry available at http://localhost:${PORT}/status`);
});
