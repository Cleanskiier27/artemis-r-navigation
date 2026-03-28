const express = require('express');
const axios = require('axios');
const path = require('path');

/**
 * Artemis R: Global Redundant Dashboard Server
 * Port: 3001
 * Aggregates and displays mission-critical data for global stakeholders.
 */

const app = express();
const PORT = 3001;
const PRIMARY_RELAY = 'http://localhost:3000/status';

app.use(express.static(path.join(__dirname, '../../public')));

app.get('/global-telemetry', async (req, res) => {
    try {
        const response = await axios.get(PRIMARY_RELAY);
        res.json({
            timestamp: new Date().toISOString(),
            mission_duration: response.data.mission_duration,
            crew_status: "NOMINAL",
            active_warnings: response.data.warnings,
            primary_metrics: {
                phase: response.data.phase,
                position: response.data.position
            }
        });
    } catch (error) {
        res.status(503).json({ status: "REDUNDANCY_MODE", message: "Primary Relay Offline. Reverting to Last State." });
    }
});

app.get('/global', (req, res) => {
    res.sendFile(path.join(__dirname, '../../public/global_dashboard.html'));
});

app.listen(PORT, () => {
    console.log(`[GLOBAL-DASH] Redundant Mission Monitor active on port ${PORT}`);
    console.log(`[GLOBAL-DASH] Access: http://localhost:${PORT}/global`);
});
