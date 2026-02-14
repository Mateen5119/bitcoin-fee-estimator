# Satoshi Fee Estimator

A Python CLI tool that fetches real-time Bitcoin network fees and calculates transaction costs in USD.

## How it Works
- Fetches live Bitcoin price via CoinGecko API.
- Fetches current block fee rates via Mempool.space API.
- Estimates the cost of a standard SegWit transaction (140 vBytes).

## How to Run
1. Install dependencies:
   ```bash
   pip install requests
