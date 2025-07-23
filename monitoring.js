const { faro } = require('@grafana/faro-web-sdk');
const { initializeFaro } = faro;

function initializeMonitoring() {
  if (process.env.GRAFANA_API_KEY) {
    initializeFaro({
      url: 'https://iamtemam.grafana.net',
      apiKey: process.env.GRAFANA_API_KEY,
      app: { 
        name: 'EagleNet',
        version: process.env.VERSION || '1.0.0'
      },
      instrumentations: []
    });
    console.log('Grafana monitoring initialized');
  }
}

module.exports = { initializeMonitoring };
