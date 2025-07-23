require('dotenv').config();
const bot = require('./bot');
const { initializeMonitoring } = require('./monitoring');

// Initialize Grafana monitoring
initializeMonitoring();

// Start bot with error handling
bot.start().catch(err => {
  console.error('Bot fatal error:', err);
  process.exit(1);
});
