# -*- coding: utf-8 -*-
import random, time

# === STRATEGY MODULES ===
def spatial_arbitrage(bot_id, gasless):
    base = round(random.uniform(0.2, 3.0), 4)
    modifier = 1.1 if gasless else 1.0
    return round(base * modifier, 4), random.randint(60, 240)

def triangular_arbitrage(bot_id, gasless):
    base = round(random.uniform(0.1, 2.0), 4)
    modifier = 1.08 if gasless else 1.0
    return round(base * modifier, 4), random.randint(80, 250)

def statistical_arbitrage(bot_id, gasless):
    base = round(random.uniform(0.15, 2.5), 4)
    modifier = 1.05 if gasless else 1.0
    return round(base * modifier, 4), random.randint(100, 300)

def assign_strategy(bot_id):
    idx = int(bot_id.split("_")[1])
    if idx <= 50:
        return "Spatial Arbitrage", spatial_arbitrage
    elif idx <= 75:
        return "Triangular Arbitrage", triangular_arbitrage
    else:
        return "Statistical Arbitrage", statistical_arbitrage

# === BOT REGISTRY ===
bots = []
for i in range(1, 101):
    bot_id = f"bot_{i:03}"
    strategy_name, logic_fn = assign_strategy(bot_id)
    gasless_mode = random.random() > 0.5  # Simulate gasless flag
    profit_eth, latency_ms = logic_fn(bot_id, gasless_mode)
    bots.append({
        "bot_id": bot_id,
        "strategy": strategy_name,
        "gasless_mode": gasless_mode,
        "activated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "profit_eth": profit_eth,
        "latency_ms": latency_ms,
        "wallet_balance": round(random.uniform(1000, 8000), 2),
        "withdrawal_mode": "AUTO" if random.random() > 0.5 else "MANUAL"
    })

# === EXPORT FUNCTION ===
def get_bot_metrics():
    return bots
