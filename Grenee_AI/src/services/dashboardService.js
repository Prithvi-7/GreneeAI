const API = "http://127.0.0.1:8000";

// Dashboard Summary
export async function getDashboard() {
  const response = await fetch(`${API}/dashboard/`);

  if (!response.ok) {
    throw new Error("Failed to fetch dashboard data");
  }

  return await response.json();
}

// Carbon Trend
export async function getTrends() {
  const response = await fetch(`${API}/dashboard/trends`);

  if (!response.ok) {
    throw new Error("Failed to fetch trends");
  }

  return await response.json();
}

// Heat Map
export async function getHeatMap() {
  const response = await fetch(`${API}/dashboard/heatmap`);

  if (!response.ok) {
    throw new Error("Failed to fetch heatmap");
  }

  return await response.json();
}

// Carbon Flow
export async function getCarbonFlow() {
  const response = await fetch(`${API}/dashboard/carbon-flow`);

  if (!response.ok) {
    throw new Error("Failed to fetch carbon flow");
  }

  return await response.json();
}

// ESG Scorecard
export async function getScorecard() {
  const response = await fetch(`${API}/dashboard/esg-scorecard`);

  if (!response.ok) {
    throw new Error("Failed to fetch ESG scorecard");
  }

  return await response.json();
}

// Analytics
export async function getAnalytics() {
  const response = await fetch(`${API}/dashboard/analytics`);

  if (!response.ok) {
    throw new Error("Failed to fetch analytics");
  }

  return await response.json();
}

// Business Intelligence
export async function getBusinessIntelligence() {
  const response = await fetch(`${API}/dashboard/business-intelligence`);

  if (!response.ok) {
    throw new Error("Failed to fetch business intelligence");
  }

  return await response.json();
}

// Predictions
export async function getPredictions() {
  const response = await fetch(`${API}/dashboard/predictions`);

  if (!response.ok) {
    throw new Error("Failed to fetch predictions");
  }

  return await response.json();
}